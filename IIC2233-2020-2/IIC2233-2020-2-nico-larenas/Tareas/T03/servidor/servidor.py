import json
import socket
import threading
from jugadores import Jugador, leer_nombres
from logica import Logica
from math import ceil


class Servidor:

    lista_jugadores_lock = threading.Lock()

    def __init__(self, host, port, log_activado=True):
        self.host = host
        self.port = port
        self.log_activado = log_activado
        self.lista_nombres = leer_nombres()

        self.lista_jugadores = []

        self.log("Inicializando servidor...")

        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket_server.bind((self.host, self.port))

        self.socket_server.listen()
        self.log(f"Servidor escuchando en {self.host}:{self.port}")
        self.log("Servidor aceptando conexiones")

        self.logica = Logica()

        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        while len(self.lista_nombres) > 0:
            socket_cliente, address = self.socket_server.accept()
            self.log(f"Un nuevo cliente con dirección {address} ha sido aceptado.")
            nombre = self.lista_nombres.pop(0)
            player = Jugador(nombre, socket_cliente, address)
            self.lista_jugadores.append(player)
            self.log(f"El nombre del cliente aceptado es {nombre}")

            thread_cliente = threading.Thread(target=self.escuchar_cliente,
                                              args=(player,), daemon=True)
            thread_cliente.start()

            actualizar = self.logica.actualizar_jugadores(self.lista_jugadores)
            self.enviar_a_todos(actualizar)

        print("Sala llena")
        inicio = self.logica.comenzar_partida(self.lista_jugadores)
        tablero = self.logica.crear_tablero()
        self.enviar_lista_respuestas(tablero)
        self.enviar_a_todos(inicio)

    def enviar_lista_respuestas(self, tup):
        msg = tup[0]
        if tup[0] == "individual":
            self.enviar(msg, jugador.socket_cliente)
        elif tup[0] == "broadcast":
            self.enviar_a_todos(msg)

    def escuchar_cliente(self, jugador):
        try:
            while True:
                mensaje = self.recibir(jugador.socket_cliente)
                self.log(f"Mensaje recibido desde {jugador.username}: {mensaje}")

                lista_respuestas = self.logica.manejar_mensaje(mensaje,
                                                               jugador, self.lista_jugadores)
                self.enviar_lista_respuestas(jugador, lista_respuestas)

        except ConnectionResetError:
            self.log(f"Error: conexión con {jugador.username} fue reseteada.")
            self.log(f"Cerrando conexión con {jugador.username}.")
            self.eliminar_cliente(jugador)

    def enviar(self, mensaje, socket_cliente):
        try:
            bytes_mensaje = self.codificar_mensaje(mensaje)
            largo_mensaje_bytes = len(bytes_mensaje).to_bytes(4, byteorder="big")
            mensaje_final = bytearray(largo_mensaje_bytes)
            for i in range(0, len(bytes_mensaje), 60):
                num_bloque = (ceil(i/60)).to_bytes(4, byteorder="little")
                mensaje_final.extend(num_bloque)
                mensaje_final.extend(bytes_mensaje[i: i+60])

            ceros = 60 - len(bytes_mensaje) % 60
            mensaje_final.extend((0).to_bytes(ceros, byteorder="little"))
            socket_cliente.sendall(mensaje_final)
        except ConnectionError:
            socket_cliente.close()

    def enviar_a_todos(self, mensaje):

        for jugador in self.lista_jugadores:

            try:
                if jugador.socket_cliente is not None:
                    self.enviar(mensaje, jugador.socket_cliente)
            except ConnectionError:
                self.eliminar_cliente(jugador)

    def recibir(self, socket_cliente):
        largo_mensaje_bytes = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_mensaje_bytes, byteorder="big")
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            numero_bloque = socket_cliente.recv(4)
            numero_bloque = int.from_bytes(numero_bloque, byteorder="little")
            bytes_mensaje.extend(socket_cliente.recv(60))

        bytes_mensaje = bytes_mensaje[numero_bloque*60:]

        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def log(self, mensaje_consola):
        if self.log_activado:
            print(mensaje_consola)

    def eliminar_cliente(self, jugador):
        self.lista_jugadores_lock.acquire()
        self.log(f"Borrando socket del cliente {jugador.username}.")
        self.lista_nombres.append(jugador.username)
        self.lista_jugadores.remove(jugador)
        jugador.socket_cliente.close()
        self.lista_jugadores_lock.release()

    @staticmethod
    def codificar_mensaje(mensaje):
        try:
            json_mensaje = json.dumps(mensaje)
            bytes_mensaje = json_mensaje.encode()

            return bytes_mensaje
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    @staticmethod
    def decodificar_mensaje(bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()
