import random
import time
from threading import Thread, Event, Lock, Timer

from parametros import (PROB_IMPOSTOR, PROB_ARREGLAR_SABOTAJE,
                        TIEMPO_ENTRE_TAREAS, TIEMPO_TAREAS, TIEMPO_SABOTAJE,
                        TIEMPO_ENTRE_ACCIONES, TIEMPO_ESCONDITE)

from funciones import (elegir_accion_impostor, print_progreso, print_anuncio,
                       print_sabotaje, cargar_sabotajes, print_explosión)


class Tripulante(Thread):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas):
        # No modificar
        super().__init__(daemon=True)
        self.color = color
        self.tareas = tareas
        self.esta_vivo = True
        self.diccionario_tareas = diccionario_tareas
        self.evento_sabotaje = evento_sabotaje
        # Si quieres agregar lineas, hazlo desde aca

    def run(self):
        while self.esta_vivo and len(self.tareas) > 0:
            if not self.evento_sabotaje.is_set():
                self.hacer_tarea()
                time.sleep(TIEMPO_ENTRE_TAREAS)
            if self.evento_sabotaje.is_set():
                PROB_ARREGLAR_SABOTAJE
                self.arreglar_sabotaje()


    def hacer_tarea(self):
        tarea = random.choice(self.tareas)
        info_tarea = self.diccionario_tareas[tarea]["nombre"]
        with Lock():
            tiempo_1 = random.randint(*TIEMPO_TAREAS)/5
            for iteracion in range(5):
                if self.esta_vivo:
                    print_progreso(self.color, "Realizando "+info_tarea, 25*iteracion)
                    time.sleep(tiempo_1)
        
        
        self.tareas.remove(tarea)
        self.diccionario_tareas[tarea]["realizado"] == True
        pass
                       

    def arreglar_sabotaje(self):
        print_anuncio(self.color, "Está arreglando el sabotaje")
        tiempo_2 = random.randint(TIEMPO_SABOTAJE)/4
        for it in range (4):
            if self.esta_vivo:
                print_progreso(self.color, "Arreglando el sabotaje", 25*it)
                time.sleep(tiempo_2)
        
        if self.esta_vivo:
            self.evento_sabotaje.clear()

        
        if self.evento_sabotaje.is_set():
            print_anuncio(self.color, "Ha logrado arreglar el sabotaje")



class Impostor(Tripulante):

    def __init__(self, color, tareas, evento_sabotaje, diccionario_tareas, tripulantes, evento_termino):
        # No modificar
        super().__init__(color, tareas, evento_sabotaje, diccionario_tareas)
        self.tripulantes = tripulantes
        self.evento_termino = evento_termino
        self.sabotajes = cargar_sabotajes()
        # Si quieres agregar lineas, hazlo desde aca

    def run(self):
        if len(self.tripulantes) > 0 and not self.evento_termino:
            accion = elegir_accion_impostor()
            if accion == "Matar":
                self.matar_jugador()
            elif accion == "Sabotear":
                self.sabotear()
            elif accion == "Esconderse":
                time.sleep(TIEMPO_ESCONDITE)


    def matar_jugador(self):
        tripulante = random.choice(self.tripulantes)
        tripulante.esta_vivo = False
        print_anuncio(tripulante.color, "Ha muerto, quedan: ", str(len(self.tripulantes)))


    def sabotear(self):
        posible = self.evento_sabotaje.is_set()
        if posible:
            sabotaje = random.choice(self.sabotajes)
            tiempo_3 = random.randint(TIEMPO_SABOTAJE)
            timer = Timer(tiempo_3, self.terminar_sabotaje)
            timer.start()
            self.evento_sabotaje.set()
            print_sabotaje(sabotaje)

    def terminar_sabotaje(self):
        if not self.evento_sabotaje.is_set():
            for vivo in range (len(self.tripulantes)):
                self.tripulantes(vivo).esta_vivo = False
                vivo += 1
            print_explosión()



if __name__ == "__main__":
    print("\n" + " INICIANDO PRUEBA DE TRIPULANTE ".center(80, "-") + "\n")
    # Se crea un diccionario de tareas y un evento sabotaje de ejemplos.
    ejemplo_tareas = {
            "Limpiar el filtro de oxigeno": {
                "lock": Lock(),
                "realizado": False,
                "nombre": "Limpiar el filtro de oxigeno"
            }, 
            "Botar la basura": {
                "lock": Lock(),
                "realizado": False,
                "nombre":  "Botar la basura"
            }
        }
    ejemplo_evento = Event()

    # Se intancia un tripulante de color ROJO
    rojo = Tripulante("Rojo", list(ejemplo_tareas.keys()), ejemplo_evento, ejemplo_tareas)

    rojo.start()

    time.sleep(5)
    # ==============================================================
    # Descomentar las siguientes lineas para probar el evento sabotaje.

    # print(" HA COMENZADO UN SABOTAJE ".center(80, "*"))
    # ejemplo_evento.set()

    rojo.join()

    print("\n-" + "="*80 + "\n")
    print(" PRUEBA DE TRIPULANTE TERMINADA ".center(80, "-"))
    if sum((0 if x["realizado"] else 1 for x in ejemplo_tareas.values())) > 0:
        print("El tripulante no logró completar todas sus tareas. ")
    elif ejemplo_evento.is_set():
        print("El tripulante no logró desactivar el sabotaje")
    else:
        print("El tripulante ha GANADO!!!")
