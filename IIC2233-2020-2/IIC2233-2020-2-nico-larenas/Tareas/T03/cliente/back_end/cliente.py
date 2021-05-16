import json
import threading
import socket
from back_end.interfaz import Controlador
from math import ceil


class Cliente:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.controlador = Controlador()

        try:
            self.socket_cliente.connect((self.host, self.port))

            thread = threading.Thread(
                target=self.escuchar_servidor, daemon=True
            )
            thread.start()

        except ConnectionRefusedError:
            print(f"No se pudo conectar a {self.host}:{self.port}")
            self.socket_cliente.close()

        self.controlador.conectar_señales(self)

    def escuchar_servidor(self):
        try:
            while True:
                mensaje = self.recibir()
                print("Mensaje recibido:", mensaje)
                self.controlador.manejar_mensaje(mensaje)

        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def enviar(self, mensaje):
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
            print(mensaje_final)
            self.socket_cliente.sendall(mensaje_final)
        except ConnectionError:
            self.socket_cliente.close()

    def recibir(self):
        largo_mensaje_bytes = self.socket_cliente.recv(4)

        largo_mensaje = int.from_bytes(largo_mensaje_bytes, byteorder="big")
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            numero_bloque = self.socket_cliente.recv(4)
            numero_bloque = int.from_bytes(numero_bloque, byteorder="little")
            bytes_mensaje.extend(self.socket_cliente.recv(60))
        bytes_mensaje = bytes_mensaje[:largo_mensaje]
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

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
