from threading import Lock
from random import choice
from prep_mapa import Hexagono, Nodo, Camino
import generador_de_cartas
import os
import json
with open("parametros.json") as p:
    params = json.loads(p.read())

with open("grafo.json") as g:
    graf = json.loads(g.read())


class Logica:
    partida_lock = Lock()

    def __init__(self):
        self.partida_en_progreso = False
        self.hexagonos = []
        self.nodos = []
        self.caminos = []

    def manejar_mensaje(self, mensaje, jugador, lista_jugadores):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return []
        lista_respuestas = []

        if comando == "comenzar_partida":
            self.comenzar_partida(lista_jugadores)

        elif comando == "send_chat_message":
            respuesta = {
                "comando": "receive_chat_message",
                "text": ">" + str(jugador.username) + ": " + mensaje["text"]
            }
            tup = ("broadcast", respuesta)
            lista_respuestas.append(tup)

        return lista_respuestas

    def actualizar_jugadores(self, lista_jugadores):
        usuarios = list(map(lambda x: x.username, lista_jugadores))
        dict_ = {
            "comando": "actualizar_jugadores",
            "jugadores": usuarios
        }
        return dict_

    def comenzar_partida(self, lista_jugadores):
        self.partida_lock.acquire()
        if self.partida_en_progreso:
            return
        else:
            dict_ = {
                "comando": "comenzar_partida",
            }

        return(dict_)
        self.partida_lock.release()

    def crear_tablero(self):
        lista_respuestas = []
        for nodo in graf["nodos"].keys():
            self.nodos.append(Nodo(nodo))
        for nodo_id, vecinos in graf["nodos"].items():
            for indice_v in vecinos:
                self.nodos[int(nodo_id)].agregar_vecino(int(indice_v))

        materias = params["MATERIAS"].copy()
        dict_con = {
            "arcilla": 0,
            "madera": 0,
            "trigo": 0
        }
        fichas = params["FICHAS"].copy()
        i = 0
        while len(materias) > 0:
            mat = choice(materias)
            if int(dict_con[mat]) <= 2 and i < 9:
                (dict_con[mat]) += 1
                num = choice(fichas)
                fichas.remove(num)
                lista_nodos = self.nodos[i].vecinos
                self.hexagonos.append(Hexagono(mat, i, num, lista_nodos))
                i += 1

            else:
                materias.remove(mat)

        mat = choice(params["MATERIAS"])
        num = choice(fichas)
        lista_nodos = self.nodos[9].vecinos
        self.hexagonos.append(Hexagono(mat, 9, num, lista_nodos))

        respuesta = {
            "comando": "hexagonos",
            "lista_hexagonos": self.hexagonos
        }
        tup = ("broadcast", respuesta)
        lista_respuestas.append(tup)
        return lista_respuestas

    def generar_cartas(self, condiciones, cantidad):
        if "comando" == "carta desarrollo":
            if condiciones:
                carta = generador_de_cartas.sacar_cartas(cantidad)
        return carta

    def carretera_mas_larga(self, grafo, inicio):
        conectados = set()
        stack = [inicio]
        while len(stack) > 0:
            vertice = stack.pop()
            if vertice in visitados:
                continue
            visitados.add(vertice)

            for vecino in grafo[vertice]:
                if vecino not in visitados:
                    stack.append(vecino)

        return list(visitados)
