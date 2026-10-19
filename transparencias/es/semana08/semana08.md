---
marp: true
theme: lpp-light
title: "LPP: Semana 8"
lang: es
size: 16:9
paginate: true
footer: "LPP · Tema 5: Programación funcional con Swift · Parte 1"
---

<!-- _class: cover institutional-cover -->
<!-- _paginate: false -->
<!-- _footer: "" -->
<div class="system-week">Semana 8</div>

# Programación funcional<br>con Swift

<div class="system-topics">Inmutabilidad, funciones y tipos<br>Enumeraciones y datos recursivos</div>
<div class="system-author">Cristina Pomares Puig</div>
<div class="institutional-logos">
<img class="university-logo" src="imagenes/logo-ua.svg" alt="Universitat d’Alacant · Universidad de Alicante">
<img class="department-logo" src="imagenes/logo-dccia.jpg" alt="Departamento de Ciencia de la Computación e Inteligencia Artificial">
</div>
<div class="mascot-figure cover-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>

<!-- Fuente: notas-clase/semana08/semana08.md. Diseño: semana 1, tema lpp-light. -->

---

## Veremos hoy

1. Swift e inmutabilidad.
2. Definición y llamada de funciones.
3. Recursión y tipos función.
4. Tipos con nombre, tuplas y alias.
5. Tipos valor y tipos referencia.
6. Enumeraciones y estructuras recursivas.

<!--
Marcas institucionales: https://imagenycomunicacion.ua.es/es/identidad-visual-corporativa-y-logotipos-ua.html
Logo DCCIA: https://web.ua.es/es/dccia/imagenes/gestadm/logotipos/logodccia.jpg
-->

<!--
Fuente: Veremos hoy. Notas de clase de la semana 8.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# De Scheme a Swift

<p class="lead">Aplicar ideas funcionales en un lenguaje con tipos estáticos y varios paradigmas.</p>

---

## Swift y programación funcional

Swift permite combinar programación funcional, imperativa y orientada a objetos.

En esta parte retomamos:

- Valores inmutables.
- Funciones como objetos de primera clase.
- Composición y recursión.
- Tipos de datos recursivos.

<!--
Fuente: Swift y programación funcional. Notas de clase de la semana 8.
La instalación y ejecución se tratan en el seminario de Swift. No reutilizar instrucciones antiguas de instalación sin contrastarlas.
-->

---

## Tipos explícitos e inferidos

<div class="columns equal">
<div>

```swift
let n: Int = 10
let str: String = "Hola"
let array: [Int] = [1,2,3,4,5]
```

</div>
<div>

```swift
let n = 10
let str = "Hola"
let array = [1,2,3,4,5]
```

</div>
</div>

La inferencia permite omitir una anotación; el valor sigue teniendo un tipo comprobado por el compilador.

<!--
Fuente: Tipos explícitos e inferidos. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Inmutabilidad: `let` y `var`

```swift
var x = 10
x = 20 // x es mutable
let y = 10
y = 20 // error: y es inmutable
```

Usamos `let` si el valor asociado al nombre no se modifica. La asignación a `y` es un error intencionado.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 116. Notas de clase de la semana 8.

-->

---

## Un valor inmutable puede calcularse al ejecutar

`let` exige una única inicialización, pero su valor no tiene que conocerse en tiempo de compilación.

Si una variable local no cambia, podemos declararla con `let`. Esto hace explícita la intención del código.

<!--
Fuente: Un valor inmutable puede calcularse al ejecutar. Notas de clase de la semana 8.
Relacionar con el aviso del compilador en saluda(nombre:) de las notas.
-->

---

<!-- _class: lesson-code -->

## Ordenación con y sin mutación

```swift
// Código recomendable en programación funcional
// porque utiliza el método sorted que devuelve una
// copia del array original
let miArray = [10, -1, 3, 80]
let arrayOrdenado = miArray.sorted()
print(miArray)
print(arrayOrdenado)
// Imprime:
// [10, -1, 3, 80]
// [-1, 3, 10, 80]
```

<!--
Fuente: Ordenación con y sin mutación. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Ordenación con y sin mutación (continuación)

```swift
// Código no recomendable en programación funcional
// porque utiliza el método sort que muta el array original
var miArray = [10, -1, 3, 80]
miArray.sort()
print(miArray)
// Imprime:
// [-1, 3, 10, 80]
```

`sorted()` devuelve un array ordenado. `sort()` cambia el array sobre el que se llama.

<!--
Fuente: Ordenación con y sin mutación. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Añadir elementos a un array

```swift
// Código recomendable en programación funcional
let miArray = [10, -1, 3, 80]
let array2 = miArray + [100]
print(array2)
// Imprime:
// [10, -1, 3, 80, 100]
```

<!--
Fuente: Añadir elementos a un array. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Añadir elementos a un array (continuación)

```swift
// Código no recomendable en programación funcional
var miArray = [10, -1, 3, 80]
miArray.append(100)
print(miArray)
// Imprime:
// [10, -1, 3, 80, 100]
```

El operador `+` construye un nuevo valor. `append` modifica el array mutable.

<!--
Fuente: Añadir elementos a un array. Notas de clase de la semana 8.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# Definición de funciones

<p class="lead">Nombre, etiquetas de argumentos, parámetros y tipo del valor devuelto.</p>

---

## Función `saluda(nombre:)`

<div class="columns equal">
<div>

```swift
func saluda(nombre: String) -> String {
    let saludo = "Hola, " + nombre + "!"
    return saludo
}
```

</div>
<div>

```swift
print(saluda(nombre:"Ana"))
print(saluda(nombre:"Pedro"))
// Imprime "Hola, Ana!"
// Imprime "Hola, Pedro!"
```

</div>
</div>

La definición usa `func`. La flecha indica el tipo del resultado.

<!--
Fuente: Función `saluda(nombre:)`. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Etiqueta de argumento y nombre de parámetro

```swift
func concatena(palabra str1: String, con str2: String) -> String {
    return str1+str2
}
print(concatena(palabra:"Hola", con:"adios"))
```

En la llamada escribimos `palabra:` y `con:`. Dentro del cuerpo usamos `str1` y `str2`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 276. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Omitir una etiqueta con `_`

```swift
func divide(_ x:Double, entre y: Double) -> Double {
   return x / y
}
print(divide(30, entre:4))
```

El nombre completo es `divide(_:entre:)`. El primer argumento no lleva etiqueta y el segundo usa `entre:`.

<!--
Fuente: Etiquetas de argumentos y nombres de parámetros. Notas de clase de la semana 8.
Distinguir etiquetas externas de nombres locales.
-->

---

<!-- _class: lesson-code -->

## Las etiquetas distinguen funciones

```swift
func mitad(par: Int) -> Int{
    return par/2
}
func mitad(impar: Int) -> Int{
    return (impar+1)/2
}
print(mitad(par: 8))
// Imprime 4
print(mitad(impar: 9))
// Imprime 5
```

`mitad(par:)` y `mitad(impar:)` son funciones distintas. Las etiquetas forman parte de sus nombres completos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 324. Notas de clase de la semana 8.

-->

---

## Sin parámetros o sin resultado explícito

<div class="columns equal">
<div>

```swift
func diHolaMundo() -> String {
    return "hola, mundo"
}
print(diHolaMundo())
// Imprime "hola, mundo"
```

</div>
<div>

```swift
func diAdios(nombre: String) {
    print("Adiós, \(nombre)!")
}
diAdios(nombre:"Dave")
// Imprime "Adiós, Dave!"
```

</div>
</div>

La segunda función devuelve `Void` y produce un efecto lateral al imprimir.

<!--
Fuente: Sin parámetros o sin resultado explícito. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Devolver una tupla

```swift
func ecuacion(a: Double, b: Double, c: Double) -> (pos: Double, neg: Double) {
    let discriminante = b*b-4*a*c
    let raizPositiva = (-b + discriminante.squareRoot()) / (2*a)
    let raizNegativa = (-b - discriminante.squareRoot()) / (2*a)
    return (raizPositiva, raizNegativa)
}
```

La función devuelve dos raíces. Se supone `a ≠ 0` y discriminante no negativo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 371. Notas de clase de la semana 8.
Se corrige la precedencia del denominador: dividir entre (2*a), no dividir entre 2 y multiplicar por a.
-->

---

<!-- _class: lesson-code -->

## Acceso a los valores de una tupla

```swift
let resultado = ecuacion(a: 1, b: -5, c: 6)
print("Las raíces de la ecuación son \(resultado.0) y \(resultado.1)")
//Imprime "Las raíces de la ecuación son 3.0 y 2.0"
```

<!--
Fuente: Acceso a los valores de una tupla. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Acceso a los valores de una tupla (continuación)

```swift
let resultado = ecuacion(a: 1, b: -5, c: 6)
print("Las raíces de la ecuación son \(resultado.pos) y \(resultado.neg)")
//Imprime "Las raíces de la ecuación son 3.0 y 2.0"
```

Podemos acceder por posición o mediante las etiquetas del tipo devuelto.

<!--
Fuente: Acceso a los valores de una tupla. Notas de clase de la semana 8.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# Recursión en Swift

<p class="lead">Conservar el diseño recursivo y expresar los casos con tipos explícitos.</p>

---

<!-- _class: lesson-code -->

## Sumar los números hasta un límite

```swift
func suma(hasta x: Int) -> Int {
  if x == 0 {
    return 0
  } else {
    return x + suma(hasta: x - 1)
  }
}
print(suma(hasta: 5))
```

El caso base devuelve `0`. El caso general suma `x` al resultado del límite anterior.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 409. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Primer elemento y resto de un array

```swift
let a = [10, 20, 30, 40, 50, 60]
let primero = a[0]
let resto = Array(a.dropFirst())
```

`dropFirst()` devuelve una vista `ArraySlice`. `Array(...)` la convierte en un array.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 429. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Sumar los valores de un array

```swift
func sumaValores(_ valores: [Int]) -> Int {
    if (valores.isEmpty) {
        return 0
    } else {
        let primero = valores[0]
        let resto = Array(valores.dropFirst())
        return primero + sumaValores(resto)
    }
}
print(sumaValores([1,2,3,4,5,6,7,8])) 
// Imprime "36"
```

La lista vacía se corresponde aquí con `isEmpty`. El resto se obtiene con `dropFirst()`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 448. Notas de clase de la semana 8.
Los arrays no tienen la representación de parejas de Scheme. La construcción repetida de nuevos arrays puede añadir costes de copia.
-->

---

## Mínimo y máximo: contrato recursivo

Para un array no vacío:

- Un único elemento es a la vez mínimo y máximo.
- La recursión devuelve los límites del resto.
- Comparamos el primero con esos dos límites.

El resultado es una tupla `(min: Int, max: Int)`.

<!--
Fuente: Mínimo y máximo: contrato recursivo. Notas de clase de la semana 8.
El ejemplo no acepta un array vacío. Este caso se retomará al estudiar opcionales.
-->

---

<!-- _class: lesson-code -->

## Definición de `minMax(array:)`

```swift
func minMax(array: [Int]) -> (min: Int, max: Int) {
    if (array.count == 1) {
        return (array[0], array[0])
    } else {
        let primero = array[0]
        let resto = Array(array.dropFirst())
        let minMaxResto = minMax(array: resto)
        let minimo = min(primero, minMaxResto.min)
        let maximo = max(primero, minMaxResto.max)
        return (minimo, maximo)
    }
}
```

<!--
Fuente: Funciones recursivas sobre arrays. Notas de clase de la semana 8.
Se omiten únicamente líneas en blanco y el comentario para mostrar la definición completa.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# Funciones como valores

<p class="lead">El tipo de una función indica los tipos de sus argumentos y de su resultado.</p>

---

<!-- _class: lesson-code -->

## Tipo función `(Int, Int) -> Int`

```swift
func sumaDosInts(a: Int, b: Int) -> Int {
    return a + b
}
func multiplicaDosInts(a: Int, b: Int) -> Int {
    return a * b
}
```

Las dos funciones tienen el mismo tipo aunque calculan operaciones distintas.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 508. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Asignar una función a una variable

```swift
var f = sumaDosInts
print(f(2,3))
// Imprime "5"
f = multiplicaDosInts
print(f(2,3))
// Imprime "6"
```

La variable `f` puede recibir otra función del mismo tipo. Las llamadas a través de `f` no usan etiquetas.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 522. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Recibir una función como parámetro

```swift
func printResultado(funcion: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Resultado: \(funcion(a, b))")
}
printResultado(funcion: sumaDosInts, 3, 5)
// Prints "Resultado: 8"
```

El parámetro `funcion` se invoca con dos enteros. La impresión es un efecto lateral del ejemplo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 554. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Generalizar el sumatorio

```swift
func sumatorio(desde a: Int, hasta b: Int, func f: (Int) -> Int) -> Int {
   if a > b { 
      return 0 
   } else {
      return f(a) + sumatorio(desde: a + 1, hasta: b, func: f)
   }
}
```

El parámetro `f` transforma cada número del intervalo antes de sumarlo.

<!--
Fuente: Funciones que reciben otras funciones. Notas de clase de la semana 8.
Mismo patrón de generalización que sum-f-x en Scheme.
-->

---

<!-- _class: lesson-code -->

## Elegir la operación del sumatorio

```swift
func identidad(_ x: Int) -> Int {
   return x
}
func doble(_ x: Int) -> Int {
   return x + x
}
func cuadrado(_ x: Int) -> Int {
    return x * x
}
print(sumatorio(desde: 0, hasta: 10, func: identidad)) // Imprime 55
print(sumatorio(desde: 0, hasta: 10, func: doble)) // Imprime 110
print(sumatorio(desde: 0, hasta: 10, func: cuadrado)) // Imprime 385
```

<!--
Fuente: Ejemplos de sumatorio. Notas de clase de la semana 8.
Las funciones identidad, doble y cuadrado tienen tipo (Int) -> Int.
-->

---

<!-- _class: lesson-code -->

## Funciones en un array

```swift
let funciones = [identidad, doble, cuadrado]
print(funciones[0](10)) // 10
print(funciones[1](10)) // 20 
print(funciones[2](10)) // 100
```

El tipo es `[(Int) -> Int]`. Primero seleccionamos una función y después la invocamos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 612. Notas de clase de la semana 8.

-->

---

## Compatibilidad de los tipos función

Un array de tipo `[(Int) -> Int]` contiene funciones de un entero a un entero.

Una función de dos argumentos no tiene ese tipo. Para mezclar valores de tipos distintos sería necesario otro diseño, y no podríamos invocarlos todos con el mismo perfil.

<!--
Fuente: Compatibilidad de los tipos función. Notas de clase de la semana 8.
Precisar tipos estáticos frente a dinámicos; no describir Scheme como carente de comprobación de tipos.
-->

---

<!-- _class: lesson-code -->

## Devolver una función

```swift
func construyeSumador10() -> (Int) -> Int {
  func suma10(x: Int) -> Int {return x+10}
  return suma10
}
let g = construyeSumador10()
print(g(20))
// Imprime 30
```

La función local `suma10` se devuelve como valor. Su tipo es `(Int) -> Int`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 647. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Construir funciones con distintos incrementos

```swift
func construyeSumador(inc: Int) -> (Int) -> Int {
  func suma(x: Int) -> Int {return x+inc}
  return suma
}
let f2 = construyeSumador(inc: 10)
let f3 = construyeSumador(inc: 100)
print(f2(20))
// Imprime "30"
print(f3(20))
// Imprime "120"
```

Cada función devuelta captura el incremento de su invocación constructora.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 669. Notas de clase de la semana 8.
Resultados: 30 y 120. Comparar con construye-sumador en Scheme.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# Tipos en Swift

<p class="lead">Distinguir tipos con nombre, tipos compuestos y semántica de los valores.</p>

---

## Tipos con nombre y tipos compuestos

**Tipos con nombre:** clases, estructuras, enumeraciones y protocolos.

**Tipos compuestos:** tuplas y tipos función.

`Int`, `String`, `Array` y `Dictionary` son tipos definidos en la biblioteca estándar.

<!--
Fuente: Tipos con nombre y tipos compuestos. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Tuplas como tipos compuestos

```swift
let tupla: (Int, Int, String) = (2, 3, "Hola")
let otraTupla: (Int, Int, String) = (5, 8, "Adios")
func sumaTupla(tupla t1: (Int, Int), con t2: (Int, Int)) -> (Int, Int) {
  return (t1.0 + t2.0, t1.1 + t2.1)
}
print(sumaTupla(tupla: (tupla.0, tupla.1),
                con: (otraTupla.0, otraTupla.1)))
// Imprime (7, 11)
```

La función suma dos tuplas componente a componente.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 759. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Alias de tipos con `typealias`

```swift
typealias Resultado = (Int, Int)
enum Quiniela {
    case uno, equis, dos
}
```

`Resultado` es otro nombre para `(Int, Int)`. El alias no crea un tipo diferente.

<!--
Fuente: Typealias. Notas de clase de la semana 8.
El enum Quiniela se usa en la función siguiente.
-->

---

<!-- _class: lesson-code -->

## Descomponer una tupla con `switch`

```swift
func quiniela(resultado: Resultado) -> Quiniela {
  switch resultado {
    case let (goles1, goles2) where goles1 < goles2:
      return .dos
    case let (goles1, goles2) where goles1 > goles2:
      return .uno
    default:
      return .equis
  }
}
```

<!--
Fuente: Typealias: función quiniela. Notas de clase de la semana 8.
case let liga los componentes; where añade una condición.
-->

---

## Semántica de los tipos valor

<div class="columns equal">
<div>

```swift
var str1 = "Hola"
var str2 = str1
str1.append("Adios")
print(str1) // Imprime "HolaAdios"
print(str2) // Imprime "Hola"
```

</div>
<div>

```swift
var array1 = [1, 2, 3, 4]
var array2 = array1
array1[0] = 10
print(array1) // [10, 2, 3, 4]
print(array2) // [1, 2, 3, 4]
```

</div>
</div>

Cambiar la copia no modifica el valor de la otra variable. Los arrays y las cadenas tienen semántica de valor.

<!--
Fuente: Semántica de los tipos valor. Notas de clase de la semana 8.

-->

---

## Tipos valor y tipos referencia

- **Tipo valor:** asignar o pasar un valor mantiene una semántica de copia.
- **Tipo referencia:** distintas variables pueden referirse a la misma instancia.

Las optimizaciones de copia al escribir conservan la semántica de valor. Un parámetro con nombre inmutable puede contener una referencia a un objeto mutable.

<!--
Fuente: Tipos valor y tipos referencia. Notas de clase de la semana 8.
No afirmar que todos los parámetros de Swift producen copias independientes del objeto. Las clases se tratarán en la semana 10.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 8</div>

# Enumeraciones

<p class="lead">Expresar un conjunto de casos y, cuando hace falta, los datos asociados a cada caso.</p>

---

## Definir casos y utilizarlos

<div class="columns equal">
<div>

```swift
enum Direccion {
    case norte
    case sur
    case este
    case oeste
}
```

</div>
<div>

```swift
let hemosGirado = true
var direccionActual = Direccion.norte
if hemosGirado {
   direccionActual = .sur
}
```

</div>
</div>

Cuando el contexto conoce el tipo, podemos abreviar `Direccion.sur` como `.sur`.

<!--
Fuente: Definir casos y utilizarlos. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Seleccionar un caso con `switch`

```swift
let direccionAIr = Direccion.sur
switch direccionAIr {
case .norte:
   print("Nos vamos al norte")
case .sur:
   print("Cuidado con los pinguinos")
case .este:
    print("Donde nace el sol")
case .oeste:
    print("Donde el cielo es azul")
}
// Imprime "Cuidado con los pinguinos"
```

La selección debe cubrir todos los casos de la enumeración, directamente o mediante `default`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 923. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Valores brutos de una enumeración

```swift
enum Quiniela: Int {
    case uno=1, equis=0, dos=2
}
```

<!--
Fuente: Valores brutos de una enumeración. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Valores brutos de una enumeración (continuación)

```swift
enum Planeta: Int {
    case mercurio=1, venus, tierra, marte, jupiter, saturno, urano, neptuno
}
let posicionTierra = Planeta.tierra.rawValue
// posicionTierra es 3
```

`rawValue` obtiene el valor bruto. Los valores enteros omitidos continúan la secuencia.

<!--
Fuente: Valores brutos de una enumeración. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Valores brutos de tipo `String`

```swift
enum Direccion: String {
    case norte, sur, este, oeste
}
let direccionAtardecer = Direccion.oeste.rawValue
// direccionAtardecer es "oeste"
```

Si no se asignan explícitamente, los valores brutos son los nombres de los casos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 987. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Inicializar a partir del valor bruto

```swift
let posiblePlaneta = Planeta(rawValue: 7)
// posiblePlaneta es de tipo Planeta? y es igual a Planeta.urano
```

Puede no existir un caso para el valor dado. El resultado es opcional, que estudiaremos la semana siguiente.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1014. Notas de clase de la semana 8.

-->

---

## Enumeraciones con valores asociados

<div class="columns equal">
<div>

```swift
enum Multiple {
    case num(Int)
    case str(String)
}
```

</div>
<div>

```swift
let valor3 = Multiple.num(10)
let valor4 = Multiple.str("Hola")
```

</div>
</div>

Cada instancia proporciona el valor asociado de su caso. Un valor bruto, en cambio, es fijo para el caso.

<!--
Fuente: Enumeraciones con valores asociados. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Extraer un valor asociado

```swift
func imprime(multiple: Multiple) {
    switch multiple {
    case let .num(x):
        print("Multiple tiene un Int: \(x)")
    case let .str(s):
        print("Multiple tiene un String: \(s)")
    }
}
imprime(multiple: valor3)
// Imprime "Multiple tiene un Int: 10"
imprime(multiple: valor4)
// Imprime "Multiple tiene un String: Hola
```

`case let` liga el dato asociado a un nombre para usarlo dentro de esa rama.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1067. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Datos recursivos con `indirect enum`

```swift
indirect enum ExpresionAritmetica {
    case numero(Int)
    case suma(ExpresionAritmetica, ExpresionAritmetica)
    case multiplicacion(ExpresionAritmetica, ExpresionAritmetica)
}
```

<!--
Fuente: Datos recursivos con `indirect enum`. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Datos recursivos con `indirect enum` (continuación)

```swift
indirect enum Lista {
    case vacia
    case nodo(Int, Lista)
}
```

Los casos recursivos contienen valores del mismo tipo. `Lista` tiene un caso vacío y otro con cabeza y resto.

<!--
Fuente: Datos recursivos con `indirect enum`. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Construir una expresión aritmética

```swift
let cinco = ExpresionAritmetica.numero(5)
let cuatro = ExpresionAritmetica.numero(4)
let suma = ExpresionAritmetica.suma(cinco, cuatro)
let producto = ExpresionAritmetica.multiplicacion(suma, ExpresionAritmetica.numero(2))
```

La expresión representa `(5 + 4) * 2`.

<!--
Fuente: Enumeraciones recursivas. Notas de clase de la semana 8.
Los nombres de los casos distinguen números, suma y multiplicación.
-->

---

<!-- _class: lesson-code -->

## Evaluar una expresión recursiva

```swift
func evalua(expresion: ExpresionAritmetica) -> Int {
    switch expresion {
    case let .numero(valor):
        return valor
    case let .suma(izquierda, derecha):
        return evalua(expresion: izquierda) + evalua(expresion: derecha)
    case let .multiplicacion(izquierda, derecha):
        return evalua(expresion: izquierda) * evalua(expresion: derecha)
    }
}
print(evalua(expresion: producto))
// Imprime 18
```

Cada caso determina cómo evaluar la expresión. El caso `numero` termina la recursión.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1120. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Construir una lista recursiva

```swift
let lista: Lista = .nodo(10, .nodo(20, .nodo(30, .vacia)))
```

Cada nodo contiene un entero y otra lista. El último resto es `.vacia`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1162. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Sumar una lista recursiva

```swift
func suma(lista: Lista) -> Int {
    switch lista {
    case  .vacia:
        return 0
    case let .nodo(first, rest):
        return first + suma(lista: rest)
    }
}
let z: Lista = .nodo(20, .nodo(10, .vacia))
print(suma(lista: z))
// Imprime 30
```

El caso vacío devuelve `0`. El caso nodo suma su cabeza al resultado del resto.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1172. Notas de clase de la semana 8.

-->

---

<!-- _class: lesson-code -->

## Convertir un array en una lista

```swift
func construye(lista: [Int]) -> Lista {
    if (lista.isEmpty) {
        return Lista.vacia
    } else {
        let primero = lista[0]
        let resto = Array(lista.dropFirst())
        return Lista.nodo(primero, construye(lista: resto))
    } 
}
let lista2 = construye(lista: [1,2,3,4,5])
print(suma(lista: lista2))
// Imprime 15
```

El constructor conserva el primer elemento y convierte recursivamente el resto.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1191. Notas de clase de la semana 8.

-->
