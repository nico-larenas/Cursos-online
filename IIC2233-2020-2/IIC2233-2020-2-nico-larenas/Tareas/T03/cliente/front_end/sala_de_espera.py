import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
import os
import json

with open("parametros.json") as p:
    params = json.loads(p.read())

window_name, base_class = uic.loadUiType("front_end\sala_de_espera.ui")


class SalaEspera(window_name, base_class):

    actualizar_jugadores_signal = pyqtSignal(dict)
    close_window_signal = pyqtSignal(bool)
    comenzar_partida_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        v_box = QVBoxLayout()
        self.labels = []
        for _ in range(params["CANTIDAD_JUGADORES_PARTIDA"]):
            jugador_label = QLabel("----------", self.jugadores)
            jugador_label.setAlignment(Qt.AlignCenter)
            estado_label = QLabel("Esperando...", self.jugadores)
            estado_label.setAlignment(Qt.AlignCenter)
            self.labels.append((jugador_label, estado_label))
            h_box = QHBoxLayout()
            h_box.addWidget(jugador_label)
            h_box.addWidget(estado_label)
            v_box.addLayout(h_box)
        self.jugadores.setLayout(v_box)

    def actualizar_jugadores(self, jugadores):
        for labels, jugador in zip(self.labels, jugadores):
            labels[0].setText(jugador)
            labels[1].setText("Conectado")

    def showEvent(self, event):
        dict_ = {
            "comando": "actualizar_jugadores"
        }
        self.actualizar_jugadores_signal.emit(dict_)
        super().showEvent(event)

    def closeEvent(self, event):
        self.close_window_signal.emit(True)
        super().closeEvent(event)

    def comenzar_partida(self):
        dict_ = {
            "comando": "comenzar_partida"
        }
        self.comenzar_partida_signal.emit(dict_)


if __name__ == "__main__":
    app = QApplication([])
    window = SalaEspera()
    window.show()
    sys.exit(app.exec_())
