from PyQt5.QtCore import QObject, pyqtSignal

class Inicial(QObject):
    senal_resultado_nombre = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def comparar_codigo(self, nombre):
        if not nombre.isalnum() :
            self.senal_resultado_nombre.emit(False)
        else:
            self.senal_resultado_nombre.emit(True)

