# Semana 3: guía de las transparencias

Presentación: [semana03.html](semana03.html).
Fuente editable: [semana03.md](semana03.md).
Fuente principal: [notas de clase de la semana 3](../../../notas-clase/semana03/semana03.md).

La presentación revisada contiene 39 diapositivas, frente a las 44 de la
versión anterior. Conserva el orden de explicación de las notas y el diseño
acordado en las semanas 1 y 2. El pie identifica el tema 2, parte 3.

Se recuperan los dos intentos previos a la llamada correcta de `mi-append`,
el razonamiento de `mi-reverse`, las asociaciones de parámetros y argumentos,
las cuatro propiedades de los datos de primera clase y la comparación de
expresiones lambda en otros lenguajes. Algunas pantallas con una sola
expresión se reúnen para explicar juntos sintaxis, ejemplo y significado.
Las preguntas de diseño preceden a las definiciones completas.

La mascota alterna señalamiento, reflexión y pregunta con signo de
interrogación. Sus intervenciones refuerzan una idea o plantean una pregunta;
no sustituyen las aclaraciones existentes. Se conserva la imagen original
sobre identificadores y funciones y el dibujo de la recursión con `apply`.
No se añade una transparencia final de repaso.

El ejemplo de `primo?` se presenta de pasada en una sola transparencia.
Las funciones auxiliares completas se conservan en las notas de clase y en
los comentarios docentes de la presentación.

Se añade una representación visual de la función como valor, siguiendo la
metáfora de máquina de las notas: creación con lambda e invocación con un
argumento. La mascota utiliza una varita y una lambda para señalar la creación.

| Diapositiva | Contenido | Referencia en las notas |
| --- | --- | --- |
| 1 | Construcción de listas y funciones como valores | notas-clase/semana03/semana03.md. Diseño: semana 1, tema lpp-light.  |
| 2 | Veremos hoy | Veremos hoy. |
| 3 | Construir listas con recursión | Separador del bloque |
| 4 | Recordatorio: diseño recursivo | Recordatorio: diseño de funciones recursivas. |
| 5 | Objetivo de `mi-append` | Función mi-append, objetivo y formulación del caso general. |
| 6 | Elegir la llamada recursiva | Función mi-append, los dos intentos de llamada recursiva que no permiten completar fácilmente el resultado. |
| 7 | La llamada recursiva de `mi-append` | Función mi-append, llamada correcta y caso base. |
| 8 | Definición de `mi-append` | Definición de `mi-append`. |
| 9 | Invertir una lista | Función mi-reverse, idea recursiva y añade-al-final. |
| 10 | Definición de `mi-reverse` | Función mi-reverse, definición completa. |
| 11 | Construir una lista desde un número | Función lista-desde. Dominio: enteros positivos, como en las notas. |
| 12 | Filtrar los números pares | Filtrar los números pares. |
| 13 | Ejemplo: comprobar si un número es primo | Ejemplo final primo? y funciones auxiliares. |
| 14 | Número variable de argumentos | Separador del bloque |
| 15 | Notación de punto | Funciones con número variable de argumentos, notación de punto y ejemplo de llamada. |
| 16 | Todos los argumentos en una lista | Todos los argumentos en una lista. |
| 17 | Ejemplo: `mi-suma` | Funciones con número variable de argumentos, mi-suma. Requiere suma-lista, de la semana 2. |
| 18 | Funciones de primera clase | Separador del bloque |
| 19 | Funciones como tipos de datos de primera clase | Funciones como tipos de datos de primera clase. |
| 20 | Forma especial `lambda` | Forma especial lambda y sintaxis. Se recupera la analogía con las cadenas anónimas. |
| 21 | Funciones anónimas | Funciones anónimas. |
| 22 | Crear, nombrar e invocar una función | Semántica de lambda y asignar el procedimiento a un identificador. |
| 23 | Semántica de la forma especial `lambda` | Semántica de lambda e invocación directa; imagen funcion-cuadrado.png. |
| 24 | Invocación directa de una función anónima | Podemos invocar a la función anónima directamente. |
| 25 | Expresiones lambda en otros lenguajes | Expresiones lambda en distintos lenguajes. Se ajustan las erratas sintácticas de Java y Objective-C; son fragmentos de expresiones, no programas completos. |
| 26 | Identificadores y funciones | Identificadores y funciones. La imagen suma.png procede de las notas. |
| 27 | `define` y azúcar sintáctico | `define` y azúcar sintáctico. |
| 28 | Predicado `procedure?` | Predicado `procedure?`. |
| 29 | Funciones como tipos de datos de primera clase | Cuatro propiedades y transición al paso de funciones como argumentos |
| 30 | Función `aplica` | Función aplica y ejemplos. Se conserva la corrección del producto 4 por 5, que da 20. |
| 31 | Pasar distintas funciones a `aplica` | Función aplica, ejemplos con cadenas. |
| 32 | Pasar una expresión lambda | Pasar una expresión lambda. |
| 33 | Composición con `aplica-2` | Composición con `aplica-2`. |
| 34 | Ejemplos de composición | Función aplica-2, ejemplos. Respuesta de la pregunta: 16. |
| 35 | Función `apply` | Función `apply`. |
| 36 | La aridad debe coincidir | Función apply, error de aridad. Mensaje de error abreviado, sin cambiar los datos de esperado y recibido. |
| 37 | Sumar un número variable de parejas | Función apply y funciones recursivas, objetivo de suma-parejas y función auxiliar. |
| 38 | Recursión con argumentos variables | Función apply y funciones recursivas, solución. |
| 39 | Cómo se combina el resultado | Función apply y funciones recursivas, representación gráfica original. |

## Comprobaciones y precisiones

Se han comprobado con Racket 38 casos: las funciones recursivas, sus casos
base, filtros y divisores, argumentos variables, funciones anónimas,
`aplica`, composición, `apply`, el error de aridad y la suma recursiva de
parejas. `mi-suma` necesita la función `suma-lista` de la semana 2.

Se mantienen las correcciones ya documentadas: el producto de 4 por 5 vale
20 y `divisores` genera la lista en orden descendente. Los ejemplos con
`lista-desde` se plantean para enteros positivos. Las expresiones en Java
y Objective-C se muestran con las erratas sintácticas corregidas, como
fragmentos de expresión y sin presentarlas como programas completos.

Las notas originales no se modifican. Véanse también las
[correcciones de la revisión](../revision.md).
