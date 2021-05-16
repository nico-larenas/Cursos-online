from threading import Lock
from random import shuffle
import os
import json

with open("parametros.json") as p:
    params = json.loads(p.read())

jugadores = params["CANTIDAD_JUGADORES_PARTIDA"]


class Jugador:
    def __init__(self, username, socket, addres):
        self.username = username
        self.socket_cliente = socket
        self.address = addres


def leer_nombres():
    lista_nombres = []
    nombres = params["NOMBRES"]
    for nombre in nombres:
        lista_nombres.append(nombre.strip())
    shuffle(lista_nombres)
    return lista_nombres[:jugadores]
