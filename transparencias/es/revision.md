# Correcciones y precisiones de las transparencias

La fuente de contenido de cada presentación son las notas de clase de la
misma semana. Los originales se conservan sin cambios. Esta revisión afecta
únicamente a las transparencias en castellano.

## Semana 1

Se usan los ejemplos españoles: `cuadrado`, `doble`, `suma-cuadrados` y el
`if` que devuelve `"la"`. Se corrigen los paréntesis de la traza de orden
normal y la cabecera de la función C `contador`. Se distingue la definición
duplicada en un módulo Racket de la posibilidad de mutación en Scheme.
La coincidencia de valores entre órdenes de evaluación se formula para el
caso en que ambos terminan. No se arrastran fechas ni horarios de cursos
anteriores; la evaluación conserva los datos de las notas.

## Semana 2

Se distingue la lista vacía de una pareja y de un símbolo. El selector
compuesto del ejemplo es `cddar`, como indica su expresión desarrollada;
la mención a `cadar` en la explicación original es una errata. Se habla de
tipado dinámico al explicar la selección de operaciones según los datos.

## Semana 3

`(aplica * 4 5)` devuelve `20`. El algoritmo de `divisores` produce su lista
en orden descendente, coherente con `lista-desde`. El dominio de esta última
función son los enteros positivos; no se presenta como una solución para `0`.
En la comparación de expresiones lambda se ajusta la sintaxis de Java
a `(Integer x) -> x * x` y se incorpora `return` al bloque de Objective-C.
Son fragmentos de expresión, no programas completos.

## Semana 4

Se conservan la captura del ámbito léxico y los ejemplos de composición.
La definición de `aplica-funcs` sustituye al ejemplo equivalente con un
paréntesis sin cerrar. Se distingue el papel de transformación, selección y
plegado. En el `foldl` de Racket utilizado aquí, la función de combinación
recibe primero el dato y después el resultado acumulado.

## Semana 5

El Fibonacci recursivo tiene un número exponencial de llamadas, pero la
profundidad de la pila es lineal. No se atribuye espacio auxiliar exponencial
a esta ejecución. `O(2ⁿ)` es una cota superior del tiempo, no el número exacto
de llamadas. La recursión por la cola evita operaciones pendientes; no impide
que crezcan los datos construidos ni el tamaño de los números.

En el ejemplo del diccionario se corrige `dic` por `mi-dic`. `src/lpp.rkt`
implementa búsquedas sobre una lista de asociación: un número lineal de
subproblemas memoizados no garantiza por sí solo tiempo total lineal.
`crea-diccionario` sí existe como alias de `make-dic` en ese archivo.

## Semana 6

La versión `altura-fos` incorpora el caso de lista vacía para devolver `0`,
como la definición recursiva y el convenio de las notas. Se distingue una
hoja de una sublista, incluida la lista vacía. La explicación de una función
que recibe hojas y listas se basa en el tipado dinámico, sin afirmar que
esas estructuras sean imposibles de modelar con tipos estáticos.

## Semana 7

Se añade el paréntesis de cierre que falta en la construcción de `arbol4`.
Se mantienen separadas las operaciones sobre árboles y sobre bosques.
Una hoja del árbol genérico tiene altura `0`; un árbol binario vacío se
representa con `arbolb-vacio`.

## Semana 8

La función de ecuaciones de segundo grado divide entre `(2*a)`. La expresión
`/ 2*a` de las notas realiza otra operación cuando `a` es distinto de `1`.
Se indican sus condiciones de uso. Se distingue la semántica de valor de
la semántica de referencia: un nombre inmutable puede referirse a una
instancia mutable. Los arrays no se presentan como listas de parejas.

## Semana 9

Se corrige el resultado de `intercambia((10, 20))` a `(20, 10)`. Se distingue
el orden de argumentos de la combinación en Swift: `reduce` recibe primero
el resultado acumulado y después el elemento. La condición del ejemplo de
filtrado es mayor o igual que `100`, conforme al código. Los ejemplos que
usan lectura de usuario necesitan las funciones auxiliares correspondientes.

## Semana 10

El inicializador de `Rectangulo` calcula la coordenada vertical usando
`tamaño.alto / 2`, en lugar de repetir la anchura. Se distingue la propiedad
almacenada de instancia de una propiedad del tipo: las enumeraciones pueden
tener propiedades almacenadas del tipo. Se precisan las condiciones de
síntesis y herencia de inicializadores, evitando presentarlas como reglas
incondicionales.

## Semana 11

La función operadora del ejemplo se declara como miembro estático, de
acuerdo con el código. La biblioteca tiene dos películas y tres canciones.
El valor `9.3` está en el índice `3` del array del ejemplo de `findIndex`.
Se omite el bloque de prueba incompleto del generador lineal congruente,
mostrando su clase y el ejemplo de uso mediante `Dado` por separado.

Se distinguen las clausuras al final de la recursión por la cola. Se señalan
las precondiciones de `Stack.pop()`, del número de repeticiones y del acceso
por posición a una cadena. Las versiones alternativas de un mismo tipo se
presentan como ejemplos independientes.
