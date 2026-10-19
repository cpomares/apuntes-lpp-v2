# Semana 7: guía de las transparencias

Presentación: [semana07.html](semana07.html).
Fuente editable: [semana07.md](semana07.md).
Fuente de contenido: [notas de clase de la semana 7](../../../notas-clase/semana07/semana07.md).

La presentación contiene 39 diapositivas. Se ha rehecho en castellano
siguiendo el orden de las notas, con la terminología y los nombres de sus
ejemplos. Conserva el diseño de la semana 1. Los ejemplos largos se separan
para mantener el código legible. Las funciones de apoyo y las definiciones
alternativas se señalan en los comentarios de Marp.

Las preguntas se plantean antes de proyectar o ejecutar la solución. Los
comentarios contienen respuestas y precisiones para la explicación. El número
de diapositivas no fija un tiempo por pantalla: algunos ejemplos están
pensados para resolverse en pizarra o en el editor.

| Diapositiva | Contenido | Referencia en las notas |
| --- | --- | --- |
| 1 | Árboles y árboles binarios | notas-clase/semana07/semana07.md. Diseño: semana 1, tema lpp-light. --> |
| 2 | Veremos hoy | Veremos hoy. Notas de clase de la semana 7. |
| 3 | Definición de árbol | Secuencia de la semana 7 |
| 4 | Raíz, hijos y hojas | Raíz, hijos y hojas. Notas de clase de la semana 7. |
| 5 | Representación mediante listas | Representación mediante listas. Notas de clase de la semana 7. |
| 6 | Un árbol representado en Scheme | Un árbol representado en Scheme. Notas de clase de la semana 7. |
| 7 | Un árbol representado en Scheme (continuación) | Un árbol representado en Scheme. Notas de clase de la semana 7. |
| 8 | La barrera de abstracción | La barrera de abstracción. Notas de clase de la semana 7. |
| 9 | Selectores y predicado de hoja | ejemplo del bloque de código que comienza en la línea 141. Notas de clase de la semana 7. |
| 10 | Usar los selectores | ejemplo del bloque de código que comienza en la línea 168. Notas de clase de la semana 7. |
| 11 | Combinar los dos niveles de abstracción | ejemplo del bloque de código que comienza en la línea 202. Notas de clase de la semana 7. |
| 12 | Árbol, lista de árboles y dato | Barreras de abstracción. Notas de clase de la semana 7. |
| 13 | Constructor `construye-arbol` | ejemplo del bloque de código que comienza en la línea 233. Notas de clase de la semana 7. |
| 14 | Construir una hoja y un árbol | Construir una hoja y un árbol. Notas de clase de la semana 7. |
| 15 | Construir una hoja y un árbol (continuación) | Construir una hoja y un árbol. Notas de clase de la semana 7. |
| 16 | Recursión entre árbol y bosque | Secuencia de la semana 7 |
| 17 | Suma de datos: dos funciones | Suma de datos: dos funciones. Notas de clase de la semana 7. |
| 18 | Suma de datos: dos funciones (continuación) | Suma de datos: dos funciones. Notas de clase de la semana 7. |
| 19 | Recorrido del bosque | Función suma-datos-arbol. Notas de clase de la semana 7. |
| 20 | Suma con funciones de orden superior | ejemplo del bloque de código que comienza en la línea 359. Notas de clase de la semana 7. |
| 21 | Resultados de las llamadas a los hijos | ejemplo del bloque de código que comienza en la línea 371. Notas de clase de la semana 7. |
| 22 | Obtener los datos en preorden | ejemplo del bloque de código que comienza en la línea 398. Notas de clase de la semana 7. |
| 23 | Preorden con `map` y `foldr` | ejemplo del bloque de código que comienza en la línea 417. Notas de clase de la semana 7. |
| 24 | Elevar los datos al cuadrado | ejemplo del bloque de código que comienza en la línea 442. Notas de clase de la semana 7. |
| 25 | Cuadrados con funciones de orden superior | ejemplo del bloque de código que comienza en la línea 460. Notas de clase de la semana 7. |
| 26 | Generalizar la transformación: `map-arbol` | ejemplo del bloque de código que comienza en la línea 483. Notas de clase de la semana 7. |
| 27 | Versión con `map` | ejemplo del bloque de código que comienza en la línea 499. Notas de clase de la semana 7. |
| 28 | Altura de un árbol | ejemplo del bloque de código que comienza en la línea 516. Notas de clase de la semana 7. |
| 29 | Altura mediante recursión mutua | ejemplo del bloque de código que comienza en la línea 521. Notas de clase de la semana 7. |
| 30 | Altura con funciones de orden superior | ejemplo del bloque de código que comienza en la línea 541. Notas de clase de la semana 7. |
| 31 | Árboles binarios | Secuencia de la semana 7 |
| 32 | Dos posiciones para los hijos | Dos posiciones para los hijos. Notas de clase de la semana 7. |
| 33 | Representación de un árbol binario | Representación de un árbol binario. Notas de clase de la semana 7. |
| 34 | Selectores y árbol vacío | ejemplo del bloque de código que comienza en la línea 605. Notas de clase de la semana 7. |
| 35 | Constructor de árboles binarios | ejemplo del bloque de código que comienza en la línea 623. Notas de clase de la semana 7. |
| 36 | Construir un árbol de tres nodos | ejemplo del bloque de código que comienza en la línea 632. Notas de clase de la semana 7. |
| 37 | Sumar los datos del árbol binario | ejemplo del bloque de código que comienza en la línea 672. Notas de clase de la semana 7. |
| 38 | Preorden de un árbol binario | ejemplo del bloque de código que comienza en la línea 689. Notas de clase de la semana 7. |
| 39 | Construir un árbol binario transformado | ejemplo del bloque de código que comienza en la línea 703. Notas de clase de la semana 7. |

## Revisión de los ejemplos

Véanse las [correcciones y precisiones](../revision.md). Los apuntes originales
no se han modificado. El formato del código se ha ajustado para proyectarlo
sin cambiar los nombres ni las operaciones, salvo las erratas documentadas.
