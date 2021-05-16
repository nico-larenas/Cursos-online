import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal

window_name, base_class = uic.loadUiType("frontend/ventana_inicio.ui")

class VentanaInicial(window_name, base_class):
    senal_revisar_nombre = pyqtSignal(str)
    senal_abrir_ventana_principal = pyqtSignal()
    senal_abrir_ranking = pyqtSignal()
    senal_volver_inicio = pyqtSignal()

    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.boton_inicio.clicked.connect(self.revisar_nombre)
            self.boton_ranking.clicked.connect(self.cambiar_ranking)
            self.senal_volver_inicio.connect(self.show)

    def revisar_nombre(self):
        # Ver si el nombre cumple con las indicaciones:
        nombre = self.usuario.text()
        self.senal_revisar_nombre.emit(nombre)


    def recibir_nombre(self, son_iguales):
        if not son_iguales:
            self.usuario.clear()
            QMessageBox.about(self, "Alerta",
                              "Nombre inválido, deben ser solo caracteres alfanuméricos")
        else:
            self.hide()
            self.senal_abrir_ventana_principal.emit()

    def cambiar_ranking(self):
        self.hide()
        self.senal_abrir_ranking.emit()

if __name__ == "__main__":
    app = QApplication([])
    window = VentanaInicial()
    window.show()
    sys.exit(app.exec_())
