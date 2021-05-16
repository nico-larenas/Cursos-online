"""
Módulo principal del servidor
"""
from servidor import Servidor
import os
import json
with open("parametros.json") as p:
    params = json.loads(p.read())

if __name__ == "__main__":
    HOST = params["HOST"]
    PORT = params["PORT"]

    SERVIDOR = Servidor(HOST, PORT)

    try:
        while True:
            input("Presione Ctrl+C para cerrar el servidor...")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
