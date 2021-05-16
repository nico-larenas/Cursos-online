import os
import json


class Nodo:
    def __init__(self, id_):
        self.id_ = id_
        self.vecinos = []

    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)


class Hexagono:
    def __init__(self, materia, id_, num, nodos):
        self.materia = materia
        self.id_ = id_
        self.num = num
        self.nodos = nodos


class Camino:
    def __init__(self, ver_1, ver_2):
        self.ver_1 = ver_1
        self.ver_2 = ver_2
