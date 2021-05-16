import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal

window_name, base_class = uic.loadUiType("frontend/ranking.ui")

class Ranking(window_name, base_class):
    senal_abrir_ranking = pyqtSignal()
    senal_volver_inicio = pyqtSignal()
    senal_seguir_jugando = pyqtSignal()
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.senal_abrir_ranking.connect(self.show)
            self.boton_volver.clicked.connect(self.volver_inicio)

    def ordenar_puntajes(self):
        ruta_puntajes = "ranking.txt"
        with open(ruta_puntajes, 'rt') as puntajes:
            lineas = puntajes.readlines()
            tabla_puntajes = []
            for puntaje in lineas:
                jugador = puntaje.strip().split(",")
                tabla_puntajes.append(jugador)
            sorted(tabla_puntajes, key=lambda student: student[1])


    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()


