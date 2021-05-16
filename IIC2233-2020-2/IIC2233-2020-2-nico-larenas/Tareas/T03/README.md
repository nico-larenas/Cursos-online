# Tarea 03: DCColonos :game_die:

## Consideraciones generales :octocat:
El código primero se corre desde el servidor, ahí se pueden conectar los clientes necesarios para que se llene la sala y empiece el juego. 

Cuando se llena la sala de espera se abre la ventana de juego.

La verdad intenté hacer lo mejor que pude el juego, pero no logré hacer que funcionaran algunas cosas, tuve bastantes complicaciones en el camino.

### Cosas implementadas y no implementadas :white_check_mark: :x:

1. Se implementó el Networking casi en su totalidad. El único problema es cuando se desconectan jugadores.
2. Se implementó totalmente la arquitectura del cliente y del servidor. Los logs se muestran en la terminal del servidor.
3. El manejo de bytes se implementó en su totalidad, además de ser totalmente funcional y seguir las especificaciones del enunciado. Esto se encuentra en ```cliente.py``` y ```servidor.py```.
4. Existe una interfaz grpafica para la sala de espera y para la sala de juego. En cliente se encuentra separado el frontend y el backend. La funcionalidad de la sala de espera está completa, mientras que la ventana principal no se logró implementar correctamente.
5. El grafo se instancia correctamente y se trata de actualizar y manejar en ```logica.py```, pero no se logra en su totalidad.
6. Las reglas no se implementaron en casi ningún momento, en ```logica.py``` están creados los hexágonos con sus respectivas características en aleatorio, pero no logre conectarlo con cliente para que se muestre en la ventana de juego :(.
7. En general se importan correctamente todos los archivos .json
8. Como bonus se trató de implementar el chat, pero los mensajes no se muestran, solo se envían.
9. Como extra, se definió la función para sacar cartas de desarrollo en ```logica```, donde si se cumplen las condiciones definidad en parametros, se saca la cantidad de cartas que quiera el jugador. También se intentó definir carretera más larga, donde teóricamente habría un grafo donde se guardan las carreteras que posee el jugador, y se recorren para crear una lista. Finalmente la lista más larga corresponde a la carretera más larga. Esta parte final se debería instanciar en cliente, pero no logré conectarlos.



## Ejecución :computer:
Esta tarea se divide en dos grandes carpetas: ```cliente``` y ```servidor```. 

En esta tarea se debe correr el código del **servidor**, donde el módulo principal a ejecutar es ```main.py```. Este código se debe correr solo una vez en la terminal.

El resto de los archivos en esta carpeta son:
1. ```generador_de_cartas.py``` en ```T03\servidor```
2. ```generador_grilla.py``` en ```T03\servidor```
3. ```grafo.json``` en ```T03\servidor```
4. ```jugadores.py``` en ```T03\servidor```
5. ```logica.py``` en ```T03\servidor```
6. ```parametros.json``` en ```T03\servidor```
7. ```prep_mapa.py``` en ```T03\servidor```
8. ```servidor.py``` en ```T03\servidor```

Por otro lado para que los clientes se conecten se debe correr en distintas terminales el código ```main.py``` que se encuentra en **cliente**. Se puede correr en la cantidad de terminales necesarias para que los espacios del juego se llenen.

El resto de los archivos en esta carpeta son:
1. ```cliente.py``` en ```T03\cliente\back_end```
2. ```interfaz.py``` en ```T03\cliente\back_end```
3. ```sprites``` en ```T03\cliente\front_end```
4. ```sala_de_espera.py``` en ```T03\cliente\front_end```
5. ```sala_de_espera.ui``` en ```T03\cliente\front_end```
6. ```sala_juego.py``` en ```T03\cliente\front_end```
7. ```sala_juego.ui``` en ```T03\cliente\front_end```
8. ```parametros.json``` en ```T03\cliente```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```json```
2. ```threading```: ```Lock```
3. ```socket```
4. ```functools```: ```partial```
5. ```PyQt5.QtCore```: ```pyqtSignal```, ```QObject```
6. ```sys```
7. ```PyQt5.QtWidgets```: ```QApplication```, ```QLabel```, ```QVBoxLayout```, ```QHBoxLayout```, ```QMainWindow```, ```QWidget```, ```QMessageBox```, ```QPushButton```
8. ```os```
9. ```random```: ```shuffle```, ```choice```
10. ```math```: ```ceil```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

En **servidor**:
1. ```jugadores```: Contiene a ```Jugador```
2. ```logica```: Contiene a ```Logica```
3. ```prep_mapa```: Contiene a ```Nodo```, ```Hexagono``` y a ```Camino```
4. ```servidor```: Contiene a ```Servidor```

En **cliente**:
1. ```back_end.cliente```: Contiene a ```Cliente```
2. ```back_end.interfaz```: Contiene a ```Controlador```
3. ```front_end.sala_de_espera```: Contiene ```SalaEspera```
4. ```front_end.sala_juego```: Contiene ```SalaJuego```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. La cantidad máxima de jugadores conectados es 4. 
2. El tamaño del tablero es constante

-------

## Referencias de código externo :book:
En esta tarea no utilicé código de intenet, solo me basé en el código de la ```AF05``` y en los contenidos. 
