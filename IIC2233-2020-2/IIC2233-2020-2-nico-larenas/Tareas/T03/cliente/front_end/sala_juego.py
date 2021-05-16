import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout)
from PyQt5.QtCore import Qt, pyqtSignal
import os
import json
from front_end.chat import ChatWidget

with open("parametros.json") as p:
    params = json.loads(p.read())


window_name, base_class = uic.loadUiType("front_end\sala_juego.ui")

class SalaJuego(window_name, base_class):
    close_window_signal = pyqtSignal(bool)
    recibir_chat_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__init_ui()
        self.__connect_events()
    
    def __init_ui(self):
        self.chat_widget = ChatWidget()
        self.enviar_texto_signal = self.chat_widget.enviar_texto_signal
        
    def __connect_events(self):
        self.recibir_chat_signal.connect(self.chat_widget.add_message)

    def closeEvent(self, event):
        self.close_window_signal.emit(True)
        super().closeEvent(event)
            

if __name__ == "__main__":
    app = QApplication([])
    window = SalaJuego()
    window.show()
    sys.exit(app.exec_())
