import funciones_tablero
from tablero import print_tablero
import os
import random
from parametros import NUM_BARCOS
barcos = NUM_BARCOS

# Menú de inicio
opcion = 0
while opcion != 2:
    print("***** Menú de Inicio *****")
    print("Selecciona una opción:")
    print("[0] Iniciar una partida")
    print("[1] Ver Ranking de Puntajes")
    print("[2] Salir")
    opcion =int(input("Indique su opción (0, 1 o 2): "))

    if opcion == 0:
        apodo = input("Inserte su apodo: ")
        apodo_valido = 0
        while apodo_valido == 0:
            if len(apodo) >= 5 and apodo.isalnum():
                apodo_valido = 1
            elif (len(apodo) < 5 or not apodo.isalnum()):
                print("Apodo inválido, no es alfanumérico o más corto que 5 caracteres")
                apodo = input("Inserte un apodo nuevo o 0 para volver: ")
                if apodo == "0":
                    break
        if apodo == "0":
            #continue sacado de https://www.programiz.com/python-programming/break-continue
            continue    
            


        filas = int(input("Ingrese número de filas del tablero: "))
        columnas = int(input("Ingrese el número de columnas del tablero: "))
        tamano_valido = 0
        while tamano_valido == 0:
            if (filas and columnas) >= 3 and (filas and columnas) <= 15:
                tamano_valido = 1
            else:
                filas = int(input("Ingrese número de filas del tablero: "))
                columnas = int(input("Ingrese el número de columnas del tablero: "))

    #Funciones del tablero:
        funciones_tablero.Tablero
        tablero_propio = funciones_tablero.Tablero(filas, columnas)
        tablero_enemigo = funciones_tablero.Tablero(filas, columnas)
        eleccion = 0
        especiales = 1

        while (tablero_propio.barcos and tablero_enemigo.barcos) > 0 and eleccion != 2:
            print("***** Menú de Juego *****")
            print_tablero(tablero_enemigo.tab, tablero_propio.tab)
            print("[0] Rendirse")
            print("[1] Lanzar una bomba")
            print("[2] Salir del programa")
            eleccion =int(input("Indique su opción (0, 1 o 2): "))

            #Mi turno:
            barcos_e_actuales = tablero_enemigo.barcos
            barcos_actuales = tablero_propio.barcos + 1
            if eleccion == 1:
                tipo = int(input("Bomba normal[0] o especial[1]? "))              
                if tipo == 1 and especiales == 1:
                    especial = int(input("Bomba cruz[0], bomba en x[1], bomba diamante[2]? "))
                elif tipo == 1 and especiales == 0:
                    tipo = 0
                    print("Bomba especial ya lanzada, se usará bomba normal")
                letra = int(input("Introduzca el número de la columna según la letra, ej. A = 0 "))
                num = int(input("Introduzca el número de la fila "))

                if tipo == 0:
                    tablero_enemigo.bombas(letra,num)
                if tipo == 1 and especiales == 1:
                    especiales = 0
                    if especial == 0:
                        tablero_enemigo.bomba_cruz(letra,num)
                    if especial == 1:
                        tablero_enemigo.bomba_x(letra,num)
                    if especial == 2:
                        tablero_enemigo.bomba_diam(letra,num)
                
                if barcos_e_actuales != tablero_enemigo.barcos:
                    continue

                #Turno enemigo
                while barcos_actuales != tablero_propio.barcos:
                    barcos_actuales = tablero_propio.barcos
                    coord_uno = random.randrange(0,filas)
                    coord_dos = random.randrange(0,columnas)
                    tab_1 = tablero_propio.tab[coord_uno][coord_dos]
                    while tab_1 != " " and tab_1 != "B":
                        coord_uno = random.randrange(0,filas)
                        coord_dos = random.randrange(0,columnas)
                        tab_1 = tablero_propio.tab[coord_uno][coord_dos]   
                    indice = "ABCDEFGHIJKLMNO"             
                    tablero_propio.bombas(coord_dos, coord_uno)
                    print("Tu oponente ha disparado en la coordenada "+str(coord_uno)+indice[coord_dos])
                    print("El tablero actual es:")
                    print_tablero(tablero_enemigo.tab, tablero_propio.tab)
            
            if eleccion == 2:
                opcion = 2

        print("JUEGO TERMINADO")
        print(" ")
        
        #Puntaje:
        encontrados = (barcos - tablero_enemigo.barcos)
        hundidos = (barcos-tablero_propio.barcos)
        puntos = max(0, filas * columnas * barcos * (encontrados - hundidos))
        final = apodo+","+str(puntos)
        ruta_puntajes = "puntajes.txt"
        with open(ruta_puntajes, 'a') as puntajes:
            puntajes.write(final+"\n")
        


    if opcion == 1:
        ruta_puntajes = "puntajes.txt"
        with open(ruta_puntajes, 'rt') as puntajes:
            lineas = puntajes.readlines()
            tabla_puntajes = []
            for puntaje in lineas:
                jugador = puntaje.strip().split(",")
                tabla_puntajes.append(jugador)
            #Para esta parte se usó ayuda de https://docs.python.org/3/howto/sorting.html
            sorted(tabla_puntajes, key=lambda student: student[1])       
            print("***** Ranking de Puntajes *****")
            n = 0
            while n < len(tabla_puntajes):
                print(str(n+1)+") "+tabla_puntajes[n][0]+": "+tabla_puntajes[n][1]+" Pts")
                n += 1
            if len(tabla_puntajes) == 0:
                print("No hay puntajes registrados")

    



            

        


