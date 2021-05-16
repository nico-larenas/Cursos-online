# Tarea 01: DCCumbre olímpica

## Consideraciones generales 
En general mi tarea no hace muchas cosas, casi todas las entidades están completas, pero el código principal no tiene mucha funcionalidad. 

En el código principal se abre el menú y se dan dos opciones, las cuales ambas funcionan, luego si se decide empezar un campeonato se piden distintos datos y después nos lleva atres opciones, menú entrenador, simular competencia o mostrar estado. Hasta aquí funciona perfectamente el código.

Todas las entidades están casi completas y son funcionales, pero no las alcancé a implementar en el menú.

Delegaciones funciona pero los tipos de delegaciones no.
Deportistas funciona completamente.
Deportes funcionan todos los deportes, pero la acción de válidad competencia no.
Campeonato no lo entendí ni alcancé a completarlo, solo puse el código de cómo se escribiría en el .txt

### Cosas implementadas y no implementadas

* <Menú de Inicio <sub>3.1</sub>>: Hecho completamente
* <Menú Principal <sub>3.2</sub>>: Hecha una parte del menú entrenador, nada de simular competencia y nada de mostrar estado.
    * <Menú Entrenador <sub>3.2.1</sub>>: Funciona en parte Entrenar, Sanar y Comprar tecnología.
    * <Simular Competencias <sub>3.2.2</sub>>: No lo hice
    * <Mostrar estado <sub>3.2.3</sub>>: No lo hice
* <Delegaciones <sub>4.1</sub>>: Me faltó hacer los tipos de delegaciones 
    * <Acciones de las delegaciones <sub>4.1.1</sub>>: Hecho completo 
    * <Tipos de delegaciones <sub>4.1.2</sub>>: Me faltó hacer casi  todo
    
* <Deportistas <sub>4.2</sub>>: Hecho completo
* <Deportes <sub>4.3</sub>>: Me falto hacer la acción de validar la competencia.
    * <Atletismo <sub>4.3.1</sub>>: Hecha completa 
    * <Ciclismo <sub>4.3.2</sub>>: Hecha completa
    * <Gimnasia <sub>4.3.3</sub>>: Hecha completa 
    * <Natación <sub>4.3.4</sub>>: Hecha completa
* <Campeonato <sub>4.4 </sub>>: Falta hacer todo
* <Resultados <sub>5.3</sub>>: Falta hacer todo
* <Parametros <sub>5.4</sub>>: Completo con todos los parámetros de la tarea.

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```campeonato.py``` en ```T01```
2. ```cargar_datos.py``` en ```T01```
3. ```delegaciones.csv``` en ```T01```
4. ```delegaciones.py``` en ```T01```
5. ```deportes.py``` en ```T01```
6. ```deportistas.csv``` en ```T01```
7. ```deportistas.py``` en ```T01```
8. ```parametros.py``` en ```T01```


## Librerías
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: ```ABC``` y ```abstractmethod```
2. ```random```: ```uniform``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```delegaciones```: Contiene a ```Delegaciones```(clase abstracta), ```IEEEsparta```, ```DCCrotona```
2. ```deportes```: Contiene a ```Deporte```(clase abstracta), ```Atletismo```, ```Ciclismo```, ```Gimnasia```, ```Natacion```.
3. ```deportistas```
4. ```Campeonato```
5. ```cargar_datos```
6. ```parametros```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se supone que si la probabilidad de lesionarse es mayor a una probabilidad aleatoria, entonces el deportista se lesiona, esto es válido porque es el mismo método utilizado para calcular si el deportista se recupera de dicha lesión.
