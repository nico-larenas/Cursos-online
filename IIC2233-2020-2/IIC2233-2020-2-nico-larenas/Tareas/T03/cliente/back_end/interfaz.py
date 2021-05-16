from functools import partial
from PyQt5.QtCore import pyqtSignal, QObject
from front_end.sala_de_espera import SalaEspera
from front_end.sala_juego import SalaJuego
from front_end.chat import ChatWidget


class Controlador(QObject):
    mostrar_sala_espera_signal = pyqtSignal()
    mostrar_sala_juego_signal = pyqtSignal()
    actualizar_jugadores_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.sala_espera = SalaEspera()
        self.sala_juego = SalaJuego()
        self.chat = ChatWidget()
        self.partida_terminada = False

        self.mostrar_sala_espera_signal.connect(self.mostrar_sala_espera)

        self.mostrar_sala_espera_signal.emit()

    def manejar_mensaje(self, mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return []

        if comando == "actualizar_jugadores":
            self.actualizar_jugadores_signal.emit(mensaje["jugadores"])

        elif comando == "comenzar_partida":
            self.mostrar_sala_juego_signal.emit()
        
        elif comando == "receive_chat_message":
            self.sala_juego.recibir_chat_signal.emit(mensaje["text"])

    def conectar_señales(self, parent):
        self.actualizar_jugadores_signal.connect(self.sala_espera.actualizar_jugadores)
        self.sala_espera.actualizar_jugadores_signal.connect(parent.enviar)
        self.sala_espera.comenzar_partida_signal.connect(parent.enviar)
        self.mostrar_sala_juego_signal.connect(self.mostrar_principal)
        self.sala_juego.enviar_texto_signal.connect(parent.enviar)

    def mostrar_sala_espera(self):
        self.sala_espera.show()

    def mostrar_principal(self):
        self.sala_espera.close()
        if not self.partida_terminada:
            self.sala_juego.show()
            self.chat.show()
