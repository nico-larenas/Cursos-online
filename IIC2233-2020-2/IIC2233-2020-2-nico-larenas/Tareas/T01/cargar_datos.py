def leer_delegaciones(delegaciones):
    with open(delegaciones, 'r') as archivo:
        lineas = archivo.readlines()
    dic_delegaciones = {}
    for linea in lineas:
        dic_parcial = {}
        if linea == lineas[0]:
            caracteristicas = linea.strip().replace("\n", "").split(",")
        else:
            elementos = linea.strip().replace("\n", "").split(",")
    
            for valor in range(len(caracteristicas)):
                dic_parcial[caracteristicas[valor]] = elementos[valor]

            if dic_parcial["Delegacion"] == "IEEEsparta":
                dic_delegaciones["IEEEsparta"] = dic_parcial

            if dic_parcial["Delegacion"] == "DCCrotona":
                dic_delegaciones["DCCrotona"] = dic_parcial
    return dic_delegaciones


def leer_deportistas(deportistas):
    with open(deportistas, 'r') as archivo:
        lineas = archivo.readlines()
    dic_deportistas = {}
    for linea in lineas:
        dic_parcial = {}
        if linea == lineas[0]:
            caracteristicas = linea.strip().replace("\n", "").split(",")
        else:
            elementos = linea.strip().replace("\n", "").split(",")
    
            for valor in range(len(caracteristicas)):
                dic_parcial[caracteristicas[valor]] = elementos[valor]
                
            dic_deportistas[dic_parcial["nombre"]] = dic_parcial
    return dic_deportistas

