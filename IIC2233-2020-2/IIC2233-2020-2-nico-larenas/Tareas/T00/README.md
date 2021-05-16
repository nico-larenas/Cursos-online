# Tarea 00: DCCombate Naval

## Consideraciones generales: 
Al iniciar se muestra se muestra el Menú principal, donde se dan tres opciones, empezar un juego, ver los puntajes o salir del programa. 
La opción de ver los puntajes funciona, pero no cumple el requisito de que se muestren solo los 5 primeros puntajes. Esto se arreglaría en la línea 132, agregando un contador para que solo se imprimieran 5 resultados en vez de todos.

La función de salir del juego también funciona. 

Al iniciar el juego pide un apodo, en el caso de que este no cumpla las condiciones da la opcion de volver al menú o ingresar otro, esto funciona correctamente, y luego pide número de filas y columnas del tablero.

Cuando termina esto nos lleva al menú del juego, donde volvemos a tener tres opciones, rendirse, lanzar una bomba o salir del programa.
En este caso la opción rendirse no funciona, solo vuelve a cargarse el menú del juego, no vuelve al menú de inicio. Esto se arreglaría poniendo una condición en la línea 105: 
```python
            if eleccion == 0:
                continue
```
La opción de salir del juego si funciona.

Al elegir lanzar una bomba se llama a distintas funciones y todas las opciones funcionan, por lo que se puede jugar hasta que alguno gane y se guarda en el archivo de puntajes.

### Cosas implementadas y no implementadas:
* 3.1 Menú de Inicio: Hecha completa, pero hay un pequeño fallo en el ranking de los puntajes
* 3.2 Menú de juego: Me faltó hacer que el jugador pueda rendirse
* 5.1 Tablero: Hecha completa
    * 5.1.1 Mapa del Jugador: Hecha completa
    * 5.1.2 Mapa del Oponente: Hecha completa
* 5.2 Barcos: Hecha completa
* 5.3 Bombas: Hecha completa
    * 5.3.1 Bombas Regulares: Hecha completa
    * 5.3.3 Bomba Cruz: Hecha completa
    * 5.3.4 Bomba X : Hecha completa
    * 5.3.5 Bomba Diamante: Hecha completa, con un pequeño fallo si es lanzada en la esquina
* 6 Partida: Hecha completa
    * 6.2 Oponente: Hecha completa
* 7 Puntajes: Hecha completa

## Ejecución:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```TOO```
2. ```funciones_tablero.py``` en ```TOO```
3. ```parametros.py``` en ```TOO```
4. ```tablero.py``` en ```TOO```


## Librerías:
### Librerías externas utilizadas:
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randrange()```
2. ```os```

### Librerías propias:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones_tablero.py```: Contiene a ```Class Tablero```, hecha para contener todas las funciones que se utilizan al momento de crear un tablero y lanzar las bombas.

## Supuestos y consideraciones adicionales:
En esta tarea no considero que haya considerado supuestos adicionales a los especificados en el enunciado.


-------
## Referencias de código externo:

Para realizar mi tarea saqué código de:
1. <https://docs.python.org/3/howto/sorting.html>: este hace que se puedan ordenar listas de listas y está implementado en el archivo ```main.py``` en la línea 129 y hace que se pueda ordenar la lista de puntajes de acuerdo al puntaje.

2. <https://www.programiz.com/python-programming/break-continue>: este hace que se pueda volver al inicio de un loop y está implementado en el archivo ```main.py``` en la línea 31 y en la línea 85 y hace que se pueda volver a empezar el while en el que se encuentra.


