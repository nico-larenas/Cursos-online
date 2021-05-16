# Actividad Bonus IIC2233 2020-2

import pyrematch as re

# -------------------------------------------------------------------
# DEFINIR AQUI LOS PATRONES PARA CONSTRUIR CADA EXPRESION REGULAR
# NO CAMBIAR LOS NOMBRES DE LAS VARIABLES
PATRON1 = "== !nombre{[^=\n]+} ==\n"
PATRON2 = "=== !nombre{[^=\n]+} ===\n"
PATRON3 = "==== !nombre{[^=\n]+} ====\n"
PATRON4 = "== !nombre{[^=\n]+} ==\n!cont{[^=]+}(\n== |$)"
PATRON5 = "=== !nombre{[^=\n]+} ===\n!cont{([^=]|====)+}(\n=== |$|\n== )"
PATRON6 = "=== !nombre{[^=\n]+} ===\n!cont{([^=]*(==== [^=\n]+ ====\n)+[^=]*)+}(\n=== |$|\n== )"


# -------------------------------------------------------------------
# Complete a continuación el código de cada consulta.
# Cada consulta recibe el patrón correspondiente para construir la expresión
# regular, y el texto sobre el cual se aplicará.
# Cada consulta debe retornar una lista de tuplas, donde cada tupla contiene
# el match encontrado, su posición de inicio y su posición de término.


# CONSULTA 1

def consulta1(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("nombre"))
        fin.append(tuple(tup))
    return fin


# CONSULTA 2

def consulta2(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("nombre"))
        fin.append(tuple(tup))
    return fin


# CONSULTA 3

def consulta3(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("nombre"))
        fin.append(tuple(tup))
    return fin



# CONSULTA 4

def consulta4(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("cont"))
        fin.append(tuple(tup))
    return fin



# CONSULTA 5

def consulta5(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("cont"))
        fin.append(tuple(tup))
    return fin



# CONSULTA 6

def consulta6(texto, patron):
    regex = re.compile(patron)
    fin = []
    for match in regex.finditer(texto):
        tup = []
        tup.append(match.group("nombre"))
        tup.extend(match.span("cont"))
        fin.append(tuple(tup))
    return fin

