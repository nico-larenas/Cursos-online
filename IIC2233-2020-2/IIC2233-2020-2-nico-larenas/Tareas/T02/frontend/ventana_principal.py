import sys
import parametros as p
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal, QCoreApplication


window_name, base_class = uic.loadUiType("frontend/ventana_juego.ui")

class VentanaPrincipal(window_name, base_class):
    senal_abrir_ventana_principal = pyqtSignal()
    senal_salir_juego = pyqtSignal
    def __init__(self):
            super().__init__()
            self.setupUi(self)

            # Botones
            self.senal_abrir_ventana_principal.connect(self.show)
            self.salir.clicked.connect(self.salir_juego)
            self.pausa.clicked.connect(self.pausar_juego)
            self.canciones.currentIndexChanged.connect(self.elegir_cancion)
            self.dificultad.currentIndexChanged.connect(self.elegir_dificultad)

            # Tienda
            self.valor.setText("Valor pinguino:   " + str(p.PRECIO_PINGUIRIN))
            self.dinero.setText("Dinero:  $" + str(p.DINERO))

            # Flechas
            self.izquierda.setText(p.FLECHA_IZQUIERDA)
            self.derecha.setText(p.FLECHA_DERECHA)
            self.abajo.setText(p.FLECHA_ABAJO)
            self.arriba.setText(p.FLECHA_ARRIBA)

            
    
    def salir_juego(self):
        self.close()

    def pausar_juego(self):
        pass

    def elegir_cancion(self):
        pass
        

    def elegir_dificultad(self):
        pass

    def puntajes(self, nombre, puntaje):
        final = nombre+","+str(puntaje)
        ruta_puntajes = "ranking.txt"
        with open(ruta_puntajes, 'a') as puntajes:
            puntajes.write(final+"\n")



