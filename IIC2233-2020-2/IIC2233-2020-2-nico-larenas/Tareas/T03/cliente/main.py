import sys
from back_end.cliente import Cliente
from PyQt5.QtWidgets import QApplication
import os
import json
with open("parametros.json") as p:
    params = json.loads(p.read())

if __name__ == "__main__":
    HOST = params["HOST"]
    PORT = params["PORT"]

    APP = QApplication([])
    # Se instancia el Cliente.
    CLIENTE = Cliente(HOST, PORT)

    # Se inicia la app de PyQt.
    ret = APP.exec_()
    sys.exit(ret)
