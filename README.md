# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimiento a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

- Documentar el código generado.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
self.mapa = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 0, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]
````

### 3.2 Lista de elementos

Para esta versión del sokoban se utilizarán numeros para representar cada uno de los elementos del juego.

"personaje":0,
            "caja":1,
            "pared":2,
            "meta":3,
            "camino":4,
            "caja_meta":5,
            "personaje_meta":6

| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Caja |
| 2 | Pared |
| 3 | Meta |
| 4 | Camino |
| 5 | Caja_meta |
| 6 | Personaje_meta |

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

| Letra | Dirección del movimiento |
| -- | -- |
| a | Izquierda |
| d | Derecha |
| w | Arriba |
| s | Abajo |

## 5. Modo de juego

El juego consiste mostrar el mapa y solicitar al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se presiona enter, se evalua el moviento, si es un movimiento valido se realiza el cambio en el array, es decir se actualiza el mapa, y se repite este proceso forma infinita, hasta que se hayan terminado de acomodar todas las cajas sobre las metas.

## 6. Funciones a implementar

Después de realizar un análisis del juego Sokoban se identifican funciones necesarias para completarlo, a continuación se crea una tabla con la lista de estas funciones para tener un mejor control sobre el avance del desarrollo del juego.

Para llevar un mejor control del avance del desarrollo se utiliza la metodología Kanban, indicando en qué estado se encuentra cada función y las fechas en las que se trabajó.

**Estados del Kanban:**

- **ToDo:** Función pendiente por desarrollar.
- **Doing:** Función desarrollada o en proceso de pruebas y ajustes.
- **Done:** Función desarrollada y verificada mediante pruebas.

### Tablero Kanban general

| Función | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Crear el mapa inicial del juego | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Definir los elementos del mapa mediante un diccionario | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Mostrar el mapa en la terminal | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Leer los movimientos del jugador | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Validar los movimientos del personaje | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Mover las cajas | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Mantener las metas debajo del personaje o de las cajas | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Reiniciar el nivel | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Detectar la finalización del nivel | Doing | 09/10/2026 | 09/10/2026 | — |
| Cargar niveles desde archivos externos | ToDo | — | — | — |

*Nota: las fechas y estados anteriores son una propuesta de documentación para el 8 y 9 de octubre. Deben corresponder al trabajo y las pruebas que realmente realizaste.*

### 6.1 Funciones generales

Las funciones generales permiten inicializar el juego, representar el mapa, recibir las instrucciones del usuario y validar los movimientos del personaje. En el código estas operaciones se encuentran dentro de la clase `Sokoban`.

| Función | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Crear el mapa inicial | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Definir los elementos del juego | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Imprimir el mapa | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Leer los movimientos del jugador | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Evaluar si un movimiento es válido | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Reiniciar el juego | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Cargar el siguiente nivel | ToDo | — | — | — |

**Descripción de las funciones implementadas:**

- `__init__()`: define los valores numéricos de los elementos, crea el mapa inicial y establece la posición inicial del personaje.
- `imprmirMapa()`: recorre las filas del mapa e imprime su contenido en la terminal.
- `mover()`: calcula la nueva posición del personaje, comprueba los límites del mapa, impide atravesar paredes y valida si una caja se puede empujar.
- `jugar()`: controla el ciclo principal del juego y recibe las teclas para mover al personaje, reiniciar o salir.
- `reiniciar()`: recupera el mapa inicial y devuelve el personaje a su posición de partida.

### 6.2 Función derecha

La función `derecha()` permite mover al personaje una casilla hacia la derecha. Para realizar el movimiento, llama al método general `mover(0, 1)`, que valida la casilla de destino y determina si es posible avanzar o empujar una caja.

| Escenario | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Personaje hacia un espacio libre | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una meta | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una pared | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una caja con espacio libre detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con una meta detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra una pared | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra otra caja | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja sobre una meta | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje ubicado sobre una meta que se mueve | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje que intenta salir del mapa | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con el personaje bloqueando la casilla posterior | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Actualizar la posición del personaje después del movimiento | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |

**Documentación:** El método `derecha()` utiliza `self.mover(0, 1)`. La función centralizada se encarga de validar las condiciones del movimiento. Cuando el destino es una pared o una caja que no puede empujarse, el movimiento se cancela.

### 6.3 Función izquierda

La función `izquierda()` permite desplazar al personaje una casilla hacia la izquierda mediante `mover(0, -1)`. Se utilizan las mismas validaciones que en los demás movimientos para mantener la consistencia del juego.

| Escenario | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Personaje hacia un espacio libre | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una meta | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una pared | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una caja con espacio libre detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con una meta detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra una pared | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra otra caja | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja sobre una meta | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje ubicado sobre una meta que se mueve | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje que intenta salir del mapa | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con el personaje bloqueando la casilla posterior | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Actualizar la posición del personaje después del movimiento | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |

**Documentación:** El método `izquierda()` utiliza `self.mover(0, -1)`. El movimiento se realiza solamente cuando la casilla de destino y, si corresponde, la casilla posterior a la caja permiten el desplazamiento.

### 6.4 Función arriba

La función `arriba()` mueve al personaje una casilla hacia arriba mediante `mover(-1, 0)`. La validación comprueba que el personaje no salga de los límites del mapa y que no intente atravesar una pared o empujar una caja hacia una posición ocupada.

| Escenario | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Personaje hacia un espacio libre | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una meta | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una pared | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una caja con espacio libre detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con una meta detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra una pared | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra otra caja | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja sobre una meta | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje ubicado sobre una meta que se mueve | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje que intenta salir del mapa | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con el personaje bloqueando la casilla posterior | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Actualizar la posición del personaje después del movimiento | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |

**Documentación:** El método `arriba()` utiliza `self.mover(-1, 0)`. El método general verifica los límites verticales y las condiciones de la casilla de destino antes de actualizar el mapa.

### 6.5 Función abajo

La función `abajo()` desplaza al personaje una casilla hacia abajo mediante `mover(1, 0)`. Al igual que en los demás movimientos, se verifica la posición de destino y se determina si existe una caja que pueda empujarse.

| Escenario | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Personaje hacia un espacio libre | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una meta | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una pared | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Personaje hacia una caja con espacio libre detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con una meta detrás | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra una pared | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja contra otra caja | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja sobre una meta | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje ubicado sobre una meta que se mueve | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje que intenta salir del mapa | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Personaje hacia una caja con el personaje bloqueando la casilla posterior | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |
| Actualizar la posición del personaje después del movimiento | Done | 08/10/2026 | 09/10/2026 | 09/10/2026 |

**Documentación:** El método `abajo()` utiliza `self.mover(1, 0)`. La función general comprueba que el movimiento no exceda el límite inferior del mapa y que las cajas puedan desplazarse a una casilla válida.

### 6.6 Determinar si el nivel ha terminado

La función `nivelTerminado()` revisa el mapa para determinar si quedan cajas fuera de las metas. En el código actual, primero busca el elemento correspondiente a `caja` y devuelve `False` si encuentra alguna. Si no encuentra cajas fuera de las metas, busca el elemento `caja_meta` para determinar si hay una caja sobre una meta.

| Función | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Detectar cajas que aún no están sobre metas | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Comprobar si existen cajas sobre metas | Doing | 09/10/2026 | 09/10/2026 | — |
| Mostrar el mensaje de nivel completado | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Cargar el siguiente nivel automáticamente | ToDo | — | — | — |
| Reiniciar el mapa con la tecla `r` | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |

**Documentación:** El método `nivelTerminado()` se ejecuta desde el ciclo principal `jugar()`. Cuando devuelve `True`, se muestra el mensaje `¡Nivel completado!` y se finaliza el ciclo del juego mediante `break`.

El método `reiniciar()` permite recuperar el mapa original mediante una copia de cada fila de `mapa_inicial`. También restablece la posición del personaje a la fila 2 y columna 3.

**Funcionalidad pendiente:** El código no carga niveles desde archivos independientes ni avanza automáticamente a otro nivel. Cuando se completa el nivel actual, el juego muestra el mensaje correspondiente y termina.

### 6.7 Documentación de la estructura del código

| Elemento | Descripción |
|---|---|
| `class Sokoban` | Clase principal que contiene los datos y métodos del juego. |
| `self.elementos` | Diccionario que asigna un número a cada elemento del mapa. |
| `self.mapa_inicial` | Lista de listas que representa el mapa original. |
| `self.mapa` | Copia del mapa que se modifica durante la partida. |
| `personaje_fila` | Guarda la fila actual del personaje. |
| `personaje_columna` | Guarda la columna actual del personaje. |
| `imprmirMapa()` | Imprime las filas del mapa en la terminal. |
| `mover()` | Centraliza las validaciones y actualizaciones de los movimientos. |
| `derecha()` | Solicita un movimiento hacia la derecha. |
| `izquierda()` | Solicita un movimiento hacia la izquierda. |
| `arriba()` | Solicita un movimiento hacia arriba. |
| `abajo()` | Solicita un movimiento hacia abajo. |
| `reiniciar()` | Restaura el mapa y la posición inicial del personaje. |
| `nivelTerminado()` | Comprueba si el nivel se considera completado. |
| `jugar()` | Ejecuta el ciclo principal, imprime el mapa y recibe las instrucciones. |

### 6.8 Pruebas funcionales propuestas

Las siguientes pruebas permiten comprobar el comportamiento del juego. Deben marcarse como completadas solamente después de ejecutarlas y verificar sus resultados.

| Prueba | Resultado esperado | Fecha de registro |
|---|---|---|
| Mover el personaje hacia una casilla libre | El personaje cambia de posición. | 08/10/2026 |
| Intentar atravesar una pared | El personaje permanece en su posición. | 08/10/2026 |
| Empujar una caja hacia una casilla libre | La caja se desplaza y el personaje ocupa su posición anterior. | 09/10/2026 |
| Intentar empujar una caja contra una pared | La caja y el personaje no avanzan. | 09/10/2026 |
| Empujar una caja hacia una meta | La caja queda representada con el valor `5`. | 09/10/2026 |
| Mover el personaje fuera de los límites del mapa | El movimiento no se realiza. | 09/10/2026 |
| Reiniciar con la tecla `r` | El mapa y el personaje vuelven a su estado inicial. | 09/10/2026 |
| Completar el nivel | Se muestra el mensaje de nivel completado cuando la función lo determina. | 09/10/2026 |

**Conclusión:** La estructura actual del programa permite controlar los movimientos del personaje, validar los desplazamientos de las cajas, conservar las metas y reiniciar la partida. Las operaciones de movimiento están centralizadas en `mover()`, por lo que las cuatro direcciones utilizan las mismas reglas. La carga de niveles desde archivos externos no se encuentra implementada y queda como una función pendiente de desarrollo.



**Elaborado por:** David Alejandro Ortiz Bustos.
