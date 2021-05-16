import os
from random import choice, sample

from bolsillo import BolsilloCriaturas
from entidades import Criatura, Entrenador


def cargar_criaturas(archivo_criaturas):
    with open(archivo_criaturas, 'rt') as archivo:
        lineas = archivo.readlines()
    dic_criaturas = {}
    for criaturas in lineas[1:]:
        criaturas = criaturas.split(",")
        dic_criaturas[criaturas[0]] = Criatura(criaturas[0],criaturas[1],int(criaturas[2]),int(criaturas[3]),int(criaturas[4]),int(criaturas[5][:-1]))
    return dic_criaturas
    

def cargar_rivales(archivo_rivales):
    criaturas = cargar_criaturas("criaturas.csv")
    with open(archivo_rivales, 'rt') as archivo:
        lineas = archivo.readlines()
    rivales_list = []
    for rivales in lineas[1:]:
        rivales = rivales.split(",")
        criaturas_r = rivales[1].strip().split(";")
        bolsillo_r = BolsilloCriaturas()
        for criaturas_riv in criaturas_r:
            bolsillo_r.append(criaturas[criaturas_riv])
        riv = Entrenador(rivales[0],bolsillo_r)
        rivales_list.append(riv)
    return rivales_list


def crear_jugador(nombre):
    criaturas = cargar_criaturas("criaturas.csv")
    # Completar


if __name__ == "__main__":
    # NO MODIFICAR
    # El siguiente codigo te ayudara a debugear este archivo.
    # Simplemente corre este archivo (cargar_datos.py)

    # Aquí revisamos si te encuentras en la ruta adecuada, para esto
    # vemos si el archivo criaturas.csv se encuentra dentro de la
    # carpera en la que estás trabajando
    if "criaturas.csv" not in list(os.walk(os.getcwd()))[0][2]:
        print(f"No estas en el directorio adecuado!")
    criaturas = cargar_criaturas("criaturas.csv")
    rivales = cargar_rivales("rivales.csv")
    jugador = crear_jugador("El Cracks")

    # Aquí revisamos si retornas lo adecuado, para esto se revisa si
    # lo retornado es una instancia de la clase correspondiente
    if (type(criaturas) is not dict or \
        not all(type(criatura) is Criatura for criatura in criaturas.values())):
            print("Recuerda: cargar_criaturas retorna un diccionario con Criatura")
    else:
        print("Lista de Criatura tiene formato correcto")
    if type(rivales) is not list or not all(type(rival) is Entrenador for rival in rivales):
        print("Recuerda: cargar_rivales retorna una lista de Entrenador")
    else:
        print("Lista de Entrenador tiene formato correcto")

    # Aquí revisamos que los datos que deben ser entregados como int
    # al __init__ de Criaturas se almacenen con el tipo correcto
    if type(criaturas) is dict:
        if not all(
            type(atributo) is int
            for criatura in criaturas.values()
            for atributo in [criatura.hp_base, criatura.atk, criatura.sp_atk, criatura.defense]
        ):
            print("Recuerda: los atributos de Criatura hp, atk, sp_atk y defensa deben ser int")
        else:
            print("Instancias de Criatura tienen atributos con tipo correcto")

    # Aquí revisamos que la cantidad de Criaturas en el Bolsillo del
    # Jugador sea la adecuada
    if type(jugador) is not Entrenador or len(jugador.bolsillo) < 6:
        print("Recuerda: debes agregar 6 Criaturas a tu bolsillo")
    else:
        print("Jugador tiene la cantidad correcta de Criatura en su Bolsillo")
