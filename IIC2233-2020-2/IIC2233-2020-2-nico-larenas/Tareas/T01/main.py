import delegaciones
import deportistas
import cargar_datos
datos_deportistas = cargar_datos.leer_deportistas('deportistas.csv')
datos_delegaciones = cargar_datos.leer_delegaciones('delegaciones.csv')

# Menú Inicial:
menu = 0
while menu != 2:
    print("*** Inicio DCCumbre Olímpica ***")
    print("")
    print("Elija la acción que desea realizar")
    print("[1] Comenzar nueva partida")
    print("[2] Salir del programa")
    menu = int(input("Ingrese el número de la opción que desea: "))
    while menu != 1 and menu != 2:
        menu = int(input("Ingrese una opción válida: "))
    
    if menu == 1: 
        usuario = str(input("Ingrese un usuario válido [solo números y letras]: "))
        rival = str(input("Ingrese un rival válido [solo números y letras]: "))
        if not usuario.isalnum():
            usuario = str(input("Ingrese un usuario válido [solo números y letras]: "))
        if not rival.isalnum():
            rival = str(input("Ingrese un rival válido [solo números y letras]: "))
        print(" ")
        print("Elija una delegación:")
        print("[0] DCCrotona")
        print("[1] IEEEsparta")
        delegacion = int(input("Ingrese el número de la delegación que desea: "))
        while delegacion != 0 and delegacion != 1:
            delegacion = int(input("Ingrese una opción válida: "))
        
        # Crear las delegaciones
        equipo_e = datos_delegaciones["IEEEsparta"]["Equipo"].split(";")
        medallas_e = datos_delegaciones["IEEEsparta"]["Medallas"]
        moral_e = datos_delegaciones["IEEEsparta"]["Moral"]
        dinero_e = datos_delegaciones["IEEEsparta"]["Dinero"]
        equipo_d = datos_delegaciones["DCCrotona"]["Equipo"].split(";")
        medallas_d = datos_delegaciones["DCCrotona"]["Medallas"]
        moral_d = datos_delegaciones["DCCrotona"]["Moral"]
        dinero_d = datos_delegaciones["DCCrotona"]["Dinero"]
        if delegacion == 1:
            principal = delegaciones.IEEEsparta(usuario, equipo_e, medallas_e,
                                                moral_e, dinero_e)
            rival_1 = delegaciones.DCCrotona(rival, equipo_d, medallas_d,
                                            moral_d, dinero_d)
        elif delegacion == 0:
            rival_1 = delegaciones.IEEEsparta(rival, equipo_e, medallas_e,
                                                moral_e, dinero_e)
            principal = delegaciones.DCCrotona(usuario, equipo_d, medallas_d,
                                               moral_d, dinero_d)

        print(" ")
        # Menú principal:
        menu_p = True
        if delegacion == 1 or delegacion == 0:
            while menu_p:
                print("*** Menú principal ***")
                print("")
                print("Elija la acción que desea realizar")
                print("[0] Menú entrenador")
                print("[1] Simular competencia")
                print("[2] Mostrar estado")
                print("[3] Salir del programa")
                dec = int(input("Ingrese el número de la opción que desea: "))
                while dec < 0 or dec > 3:
                    dec = int(input("Ingrese una opción válida: "))
                if dec == 3:
                    menu_p = False
                    menu = 2
                if dec == 0:
                    ent = True
                    while ent:
                        # Menu entrenador
                        print("")
                        print("*** Menú entrenador ***")
                        print("")
                        print("Elija la acción que desea realizar")
                        print("[0] Fichar")
                        print("[1] Entrenar")
                        print("[2] Sanar")
                        print("[3] Comprar tecnología")
                        print("[4] Usar habilidad especial")
                        print("[5] Volver al menú anterior")
                        print("[6] Salir del programa")
                        ele = int(input("Ingrese el número de la opción que desea: "))
                        while ele < 0 or ele > 6:
                            ele= int(input("Ingrese una opción válida: "))
                        if ele == 6:
                            ent = False
                            menu_p = False
                            menu = 2
                        if ele == 5:
                            ent = False
                            continue                     
                        # En caso de seleccionar Fichar, se deben mostrar todos los
                        #  deportistas disponibles, dar la opción de
                        # seleccionar alguno que no esté fichado por ninguna delegación
                        #  y luego agregarlo al equipo de la delegación del usuario.
                        if ele == 0:
                            pass

                        if ele == 1:
                            print(" ")
                            print("Estos son los deportistas de tu equipo:")
                            for i in range(len(principal.equipo)):
                                print(principal.equipo[i])
                                i += 1 
                            print("A quién desea entrenar?")
                            entrenado = input("Ingrese el nombre correspondiente: ")
                            if entrenado in principal.equipo:
                                print("[0] Velocidad"
                                      "[1] Resistencia"
                                      "[2] Flexibilidad"
                                      "[3] Moral")
                                atributo = input("Qué atributo desea entrenar?")
                                if atributo == 0:
                                    atributo = "Velocidad"
                                elif atributo == 1:
                                    atributo = "Resistencia"
                                elif atributo == 2:
                                    atributo = "Flexibilidad"
                                elif atributo == 3:
                                    atributo = "Moral"
                                vel = datos_deportistas[entrenado]["velocidad"]
                                res = datos_deportistas[entrenado]["resistencia"]
                                flex = datos_deportistas[entrenado]["flexibilidad"]
                                mor = datos_deportistas[entrenado]["moral"]
                                les = datos_deportistas[entrenado]["lesionado"]
                                precio = datos_deportistas[entrenado]["precio"]
                                ent = deportistas.Deportistas(vel, res, flex, mor, les, precio)
                                ent.entrenar(atributo)

                        if ele == 2:
                            print(" ")
                            print("Estos son los deportistas lesionados:")
                            for i in range(len(principal.equipo)):
                                if datos_deportistas[principal.equipo[i]]["lesionado"]:
                                    print(principal.equipo[i])
                                i += 1 
                            print("A quién desea sanar?")
                            entrenado = input("Ingrese el nombre correspondiente: ")
                            vel = datos_deportistas[entrenado]["velocidad"]
                            res = datos_deportistas[entrenado]["resistencia"]
                            flex = datos_deportistas[entrenado]["flexibilidad"]
                            mor = datos_deportistas[entrenado]["moral"]
                            les = datos_deportistas[entrenado]["lesionado"]
                            precio = datos_deportistas[entrenado]["precio"]
                            ent = deportistas.Deportistas(vel, res, flex, mor, les, precio)
                            principal.sanar_lesiones(ent)
                        
                        if ele == 3:
                            principal.comprar_tecnologia()
                        
                        # Finalmente, la opción de Usar habilidad especial sólo podrá utilizarse 
                        # una vez por part ida y sus resultados varían según el tipo de delegación.
                        # Puedes encontrar más información sobre estas acciones en la sección Delegaciones.
                        # Luego de realizarse cualquiera de las acciones antes mencionadas, 
                        # el programa debe volver a mostrar este menú.

                if dec == 1:
                    # Simular competencia
                    # Cuando el usuario estime conveniente, puede terminar los entrenamientos 
                    # del día y realizar la simulación de las competencias del día siguiente.
                    # En el caso que resten días de competencia, al entrar en este menú se 
                    # mostrará una lista de deportistas disponibles de su propia delegación 
                    # para competir en el primer deporte del día. Luego de escoger uno, la lista
                    # se volverá a mostrar y el usuario deberá nuevamente escoger un deportista 
                    # para participar en la segunda competencia del día. Esto debe repetirse hasta
                    # que se hayan seleccionado los deportistas para las cuatro competencias del día.
                    # En el caso de la delegación rival, esta seleccionará a sus deportistas para 
                    # cada competencia de forma aleatoria. Queda a tu criterio decidir si la 
                    # delegación rival usa o no sus días de entrenamiento fichando 
                    # deportistas, sanándolos ó entrenándolos.
                    # Luego se procederá a simular las competencias según lo especificado 
                    # en la sección Campeonato.
                    # Si es que ya no quedan más días para competir, se deben mostrar los 
                    # resultados finales de la DCCumbre Olímpica, mostrar qué delegación fue 
                    # la ganadora y dar la opción de Salir del programa o Realizar una nueva simulación.
                    pass
                if dec == 2:
                    # Mostrar estado
                    # Esta opción deberá imprimir en consola información sobre las delegaciones 
                    # y sus deportistas, además de algunos datos que permitirán conocer el estado
                    # actual de la competencia. Para mayor detalle de qué se debe mostrar en 
                    # este menú, revisar la sección Campeonato.
                    pass








    

