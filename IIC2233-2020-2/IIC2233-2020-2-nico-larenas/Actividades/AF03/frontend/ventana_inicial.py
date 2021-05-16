import os
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaInicial(QWidget):

    senal_comparar_codigo = pyqtSignal(str)
    senal_abrir_menu_principal = pyqtSignal()

    def __init__(self, ancho, alto, ruta_logo):
        """Es el init de la ventana del menú de inicio. Puedes ignorarlo."""
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)
        self.init_gui(ruta_logo)

    def init_gui(self, ruta_logo):
        self.setWindowTitle("Ventana inicial DCCrew")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(ruta_logo))
        self.label.resize(*self.size)
        self.label.setScaledContents(True)


        self.label1 = QLabel('Ingrese el código de su partida:', self)
        self.input_codigo = QLineEdit('Debe ser uno existente', self)
        self.input_codigo.resize(100, 20)
        
        self.boton = QPushButton('&Ingresar', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.comparar_codigo)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.input_codigo)
        hbox.addWidget(self.boton)
        hbox.addStretch(2)

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)


    def comparar_codigo(self):
        """Método que emite la señal para comparar el código. Puedes ignorarlo.
        Recuerda que el QLineEdit debe llamarse 'input_codigo'"""
        codigo = self.input_codigo.text()
        self.senal_comparar_codigo.emit(codigo)

    def recibir_comparacion(self, son_iguales):
        """Método que recibe el resultado de la comparación. Puedes ignorarlo.
        Recuerda que el QLineEdit debe llamarse 'input_codigo'"""
        if not son_iguales:
            self.input_codigo.clear()
            self.input_codigo.setPlaceholderText("¡Inválido! Debe ser un código existente.")
        else:
            self.hide()
            self.senal_abrir_menu_principal.emit()
    

