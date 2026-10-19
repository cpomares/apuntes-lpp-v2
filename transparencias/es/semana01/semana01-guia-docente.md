# Semana 1: guía docente para unas dos horas

Presentación: [semana01.html](semana01.html).
Fuente editable: [semana01.md](semana01.md).

La revisión sigue la secuencia de `notas-clase/semana01/semana01.md`.
La presentación tiene 39 diapositivas. El objetivo es que las reglas y los
resultados se puedan justificar, alternando proyección, pizarra y ejecución.
Las preguntas y respuestas también están en los comentarios de Marp.
Los tiempos son una propuesta de ensayo, no un ritmo obligatorio por pantalla.

## Ritmo de la sesión

| Tiempo orientativo | Diapositivas | Trabajo principal |
| --- | --- | --- |
| 0–12 min | 1–7 | Organización de la asignatura. Tema 1 como estudio independiente. |
| 12–32 min | 8–18 | Función pura, composición y contraste con estado mutable. |
| 32–55 min | 19–24 | Evaluación y funciones. Resolver la expresión anidada en pizarra. |
| 55–80 min | 25–30 | Reglas de sustitución y comparación de trazas. |
| 80–115 min | 31–39 | Formas especiales, símbolos, listas y construcción. |

La diapositiva 6 presenta el tema 1 como estudio no presencial en casa.
La 7 introduce historia, genealogía y paradigmas, con un enlace a TIOBE sin
reproducir clasificaciones ni capturas.
El tema 2 comienza en la diapositiva 8.

## Qué desarrollar en pizarra o editor

- **10, función pura:** `(cuadrado 4)`, `(* 4 4)`, `16`. Una llamada que además
  modificase un contador externo tendría un efecto lateral.
- **14, composición:** relacionar las variables intermedias del ejemplo C con
  las llamadas anidadas. Los resultados son `64`, `128` y `16384`.
- **15, mutación:** separar asignación de definición. El error de definir `a`
  dos veces se observa en un módulo `#lang racket`, no es una demostración
  de que Scheme carezca de mutación.
- **16, referencias:** dibujar un único objeto con dos referencias. Cambiar
  su campo `x` una sola vez, no dibujar dos copias del objeto.
- **17–18, transparencia referencial:** comparar `cuadrado` con `contador()`.
  El resultado del segundo depende del estado que conservan llamadas previas.
- **20–21, evaluación:** dejar un intento individual antes de pasar a la
  solución. Resultado `5`. La traza elige un orden válido entre cálculos
  independientes; no establece un orden universal izquierda–derecha en Scheme.
- **22–23, funciones:** señalar nombre, parámetro formal, argumento y cuerpo.
  En `(suma-cuadrados 3 4)`, primero se obtienen `9` y `16`, y después `25`.
- **24, composición de funciones:** explicar el paso de los datos entre funciones. El código
  es conceptual; sus operaciones necesitan implementaciones para ejecutarse.
- **27–29, sustitución:** mantener las definiciones en la pizarra mientras
  cambia la diapositiva. En orden aplicativo, `x` recibe `4`. En orden normal,
  se duplica `(cuadrado a)`. Ambas trazas del ejemplo terminan en `8`.
- **30, impureza:** contar llamadas a `random`. Scheme utiliza orden aplicativo,
  de modo que `(zero (random 10))` devuelve `0`. El otro caso es una comparación
  del modelo, no una segunda ejecución con distinta configuración de Scheme.
- **34–35, selección:** pedir una predicción antes de ejecutar. El ejemplo de
  `if` devuelve `"la"` y no ejecuta la división por cero. En `cond`, una vez
  seleccionada una cláusula se omiten las posteriores.
- **36–38, código y datos:** con `x` ligado a `12`, `(symbol? 'x)` da `#t` y
  `(symbol? x)` da `#f`. En las dos listas de la diapositiva 38 hay tres
  elementos exteriores; el segundo es `2/3` en una y la lista `(/ 2 3)` en otra.
- **39, listas anidadas:** `(cons '(1 2) '(3 4))` tiene tres elementos exteriores;
  `(append '(1 2) '(3 4))` tiene cuatro. Una lista puede ser un solo elemento.

## Relación con las notas originales

| Apartado de las notas | Diapositivas |
| --- | --- |
| Tema 0: temario, recursos, prácticas, evaluación y consejos | 2–5 |
| Tema 1: estudio en casa | 2, 6–7 |
| Tema 2 y «Veremos hoy» | 8–9 |
| Definición, características y lenguajes funcionales | 10–12 |
| Declarativa frente a imperativa; pasos, mutación, estado y resumen | 13–18 |
| Evaluación de expresiones | 19–21 |
| Definición, funciones auxiliares y composición | 22–24 |
| Modelo de sustitución y órdenes de evaluación | 25–30 |
| Funciones y formas especiales; `define`, `if`, `cond` | 31–35 |
| `quote`, símbolos, expresiones y listas | 36–38 |
| `cons` y `append` | 39 |

Los ejemplos y nombres de funciones proceden de las notas de clase en
castellano. Se corrigen la cabecera C de `contador`, los paréntesis de la
traza de orden normal y la cadena de una cláusula de `cond`. Los comentarios
de cada diapositiva identifican su apartado de origen y recogen respuestas
y apoyos para pizarra. Las lecturas complementarias y el desarrollo del
Tema 1 permanecen en las notas.

## Precisiones conceptuales

- La presentación aplica un modelo funcional puro a los ejemplos. Scheme
  también permite estado y efectos laterales.
- La comparación de órdenes debe distinguir valor y terminación. El ejemplo
  de clase termina en ambos casos; la pureza por sí sola no garantiza que
  ambos órdenes terminen en cualquier programa.
- `quote` produce datos. Un identificador en código, un símbolo como dato y
  una cadena de caracteres no son conceptos intercambiables.
- Los ejemplos de `cons` y `append` trabajan con listas propias. Los pares
  y las listas impropias se desarrollan en la semana siguiente.

Fuentes de contraste para las reglas y precisiones:

- [SICP: modelo de sustitución](https://sicp.sourceacademy.org/chapters/1.1.5.html).
- [Racket: definiciones](https://docs.racket-lang.org/guide/define.html).
- [Racket: condicionales](https://docs.racket-lang.org/guide/conditionals.html).
- [Racket: quote](https://docs.racket-lang.org/guide/quote.html).
- [Racket: pares y listas](https://docs.racket-lang.org/guide/Pairs__Lists__and_Racket_Syntax.html).

## Datos del curso que confirmar

Antes de impartir la presentación, contrastar los porcentajes y las normas de evaluación con la planificación del curso
nuevo. No se han trasladado fechas concretas de cursos anteriores.
