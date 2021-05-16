from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt, QUrl, QObject, pyqtSignal
from PyQt5 import uic
import sys
import parametros as p
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

class Principal(QObject):
    def __init__(self):
        super().__init__()
        self.cancion =  None

    def elegir_cancion(self, nombre):
        self.path_canciones = path.join(p.CANCIONES[nombre])
        cancion = QMediaPlayer
        cancion.setMedia(QMediaContent(QUrl.fromLocalFile(self.path_canciones)))
        cancion.volume(50)
        self.cancion = cancion
        pass
    
    def comprar(self, cantidad):
        if cantidad == 0:
            dinero = p.DINERO
        else:
            dinero = p.DINERO - p.PRECIO_PINGUIRIN

    def aprobacion(self):
        pass

    def elegir_dificultad(self, dificultad):
        self.dificultad = dificultad
        self.par_dificultad = p.DIFICULTADES[dificultad]

    def calc_aprobacion(self, pasos_correctos, pasos_incorrectos, pasos_totales, dificultad):
        aprobado = False
        aprobacion = (p.APROBACION*((pasos_correctos - pasos_incorrectos)/pasos_totales))
        if aprobacion > p.DIFICULTADES[dificultad][2]:
            aprobado = True
        
    def calc_puntajes(self, max_combo, f_normales, f_x2, f_doradas, f_hielo):
        suma_flechas = (f_normales + p.FLECHAS_X2 * f_x2 + p.FLECHAS_DOR * f_doradas + f_hielo)
        puntaje = max_combo * suma_flechas * p.PUNTOS_FLECHA

# Flechas:
class Flechas(QThread):

    actualizar = pyqtSignal(QLabel, int, int)

    def __init__(self, parent, limite_x, limite_y):
        super().__init__()
        self.ruta_imagen = path.join("sprites", "flechas", "left_1.png")

        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setGeometry(-p.ALTO_FLECHA, -p.ALTO_FLECHA, p.ALTO_FLECHA, p.ALTO_FLECHA)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        self.limite_x = limite_x
        self.limite_y = limite_y

        self.__posicion = (0, 0)
        self.posicion = (0, 0)

        self.label.show()
        self.start()

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.label, *self.posicion)

    def run(self):
        while self.posicion[0] < self.limite_x and self.posicion[1] < self.limite_y:
            sleep(0.01)
            nuevo_x = self.posicion[0]
            nuevo_y = self.posicion[1] + 1
            self.posicion = (nuevo_x, nuevo_y)


class VentanaInicial(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.flechas_creada = 0

        self.timer_crea_flechas = QTimer(self)
        self.timer_crea_flechas.setInterval(1000)
        self.timer_crea_flechas.timeout.connect(self.creador_de_flechas)
        self.timer_crea_flechas.start()

        self.flechas = []

    def creador_de_flechas(self):
        nueva_flechas = Flechas(self, self.width(), self.height())
        nueva_flechas.actualizar.connect(self.actualizar_label)
        self.flechas.append(nueva_flechas)
        self.flechas_creada += 1

    def actualizar_label(self, label, x, y):
        label.move(x, y)

# Drag and Drop:
   