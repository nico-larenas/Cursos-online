import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QObject, pyqtSignal

window_name, base_class = uic.loadUiType("frontend/resumen.ui")

class Resumen(window_name, base_class):
    senal_volver_inicio = pyqtSignal()
    senal_aprobado = pyqtSignal()
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.volver.clicked.connect(self.volver_inicio)
            

    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()
    
    def cambio_mensaje(self, aprobado):
        if aprobado:
            self.mensaje_final = "Felicidades aprobaste, puedes seguir jugando :)"
            self.boton1 = QPushButton('&Seguir jugando', self)
            self.boton1.resize(self.boton1.sizeHint())
            self.boton1.clicked.connect(self.senal_aprobado)
        else:
            self.mensaje_final = "Te echan de DCCumbia por no tener suficiente aprobación :("
    
