# Semana 2: guía de las transparencias

Presentación: [semana02.html](semana02.html).
Fuente editable: [semana02.md](semana02.md).
Fuente de contenido: [notas de clase de la semana 2](../../../notas-clase/semana02/semana02.md).

La presentación contiene 39 diapositivas y sigue el diseño revisado de la
semana 1. El contenido conserva los ejemplos y la terminología de las notas.
El personaje LPP aparece en la portada y señala aclaraciones concretas;
alterna las posturas de saludo, señalamiento, reflexión y pregunta. En las
preguntas lleva un signo de interrogación y dirige la mirada hacia él.

El diseño recursivo parte de confiar en el resultado de una llamada con un
problema más sencillo. Se conservan los dibujos originales de `suma-hasta`
y `suma-lista`. Las pruebas sobre parejas y listas se plantean antes de su
definición recursiva. Se recuperan los ejemplos de `cons` con listas y de
acceso con `car` y `cdr` que estaban demasiado resumidos.

Las preguntas se plantean antes de ejecutar los ejemplos. Los comentarios
incluyen respuestas y referencias para la explicación. No hay transparencia
final de repaso: la presentación termina con los niveles de abstracción,
como las notas.

| Diapositiva | Contenido | Referencia en las notas |
| --- | --- | --- |
| 1 | Recursión, parejas y listas | Diseño: semana 1, tema lpp-light. |
| 2 | Veremos hoy | Veremos hoy. |
| 3 | Confía en la recursión | Separador del bloque de las notas |
| 4 | Diseño de una función recursiva | Confía en la recursión; no utilizar el depurador ni hacer trazas para diseñar. |
| 5 | Sumar los números hasta `x` | Confía en la recursión. Dominio del ejemplo: enteros no negativos. |
| 6 | Diseño de `suma-hasta` | Diseño de `suma-hasta`. |
| 7 | Usar el resultado de la recursión | Confía en la recursión, ejemplo concreto con x igual a 5. No desplegar la llamada suma-hasta 4. |
| 8 | Construir el alfabeto hasta un carácter | Otro ejemplo de función recursiva alfabeto-hasta. Respuesta: #\a, con resultado "a". |
| 9 | El carácter anterior | El carácter anterior. |
| 10 | Definición de `alfabeto-hasta` | Solución final de alfabeto-hasta. Dominio: caracteres consecutivos desde a hasta el solicitado. |
| 11 | Selección de elementos: `first` y `rest` | Selección de elementos: `first` y `rest`. |
| 12 | Diseñar `suma-lista` | Diseñar `suma-lista`. |
| 13 | Definición de `suma-lista` | Definición de `suma-lista`. |
| 14 | Contar apariciones: `veces` | Contar apariciones: `veces`. |
| 15 | El tipo de dato pareja | Separador del bloque de las notas |
| 16 | Construcción con `cons` y con `quote` | Construcción con `cons` y con `quote`. |
| 17 | Funciones de acceso: `car` y `cdr` | Funciones de acceso: `car` y `cdr`. |
| 18 | Definición declarativa y predicado | Definición declarativa y predicado. |
| 19 | Parejas con datos de cualquier tipo | Las parejas pueden contener cualquier tipo de dato; las parejas son objetos inmutables. La mutación de parejas se estudiará con el paradigma imperativo. |
| 20 | Objetos de primera clase | Objetos de primera clase. |
| 21 | Parejas como argumentos y resultados | Paso como argumento y devolución como resultado. Respuesta: (4 . 6); las parejas recibidas no se modifican. |
| 22 | Una función con distintos tipos de datos | Ejemplo de función que recibe distintos tipos de datos. Las notas dicen débilmente tipado; la precisión es tipado dinámico. Resultados: 5, "hola mundo", símbolo error. suma-parejas debe estar definida. |
| 23 | Diagramas caja-y-puntero | Formar parte de otras parejas y diagramas caja-y-puntero. Las dos definiciones de p se muestran como alternativas. |
| 24 | De la expresión al diagrama | De la expresión al diagrama. Notas de clase de la semana 2. |
| 25 | Selectores compuestos | Funciones c????r. Se corrige la errata cadar de la explicación: la composición mostrada es cddar. |
| 26 | Listas en Scheme | Separador del bloque de las notas |
| 27 | Construir listas con `cons` | Relación entre listas y parejas, recordatorio de cons con listas. |
| 28 | ¿Pareja o lista? | ¿Pareja o lista?. Notas de clase de la semana 2. |
| 29 | Construir una pareja con una lista | Relación entre listas y parejas. Respuestas: 1, (2 3); #t, #t; p1 representa (1 1 2 3). |
| 30 | Definición de una lista | Definición de listas con parejas. La lista vacía no es un símbolo, como se comprueba después en las notas. |
| 31 | La lista de un elemento | La lista de un elemento. Notas de clase de la semana 2. |
| 32 | La lista `(1 2 3)` | La lista `(1 2 3)`. Notas de clase de la semana 2. |
| 33 | La lista vacía | Lista vacía. Los resultados se muestran sin el prefijo de quote que puede añadir la impresión de DrRacket. |
| 34 | Listas de asociación | Listas de asociación. Notas de clase de la semana 2. |
| 35 | Listas de listas | Listas de listas. Notas de clase de la semana 2. |
| 36 | Del diagrama a la expresión | Ejemplo inverso. Notas de clase de la semana 2. |
| 37 | Solución del ejemplo inverso | Ejemplo inverso, solución. El diagrama se plantea en la diapositiva anterior. |
| 38 | Impresión de parejas | Impresión de listas y parejas por el intérprete. print-pareja es una función de los apuntes, no una primitiva. |
| 39 | Distintos niveles de abstracción | Distintos niveles de abstracción. |

## Comprobación de ejemplos

Se han comprobado con Racket los casos base y generales de `suma-hasta`,
`alfabeto-hasta`, `suma-lista` y `veces`, las funciones `anterior`,
`suma-parejas` y `suma`, los selectores del ejercicio y las construcciones
con listas. Los diagramas sencillos de parejas se han redibujado en SVG,
sin modificar las imágenes originales de las notas.

Las precisiones sobre tipado dinámico, la lista vacía y el selector `cddar`
se recogen en [las correcciones de la revisión](../revision.md).
