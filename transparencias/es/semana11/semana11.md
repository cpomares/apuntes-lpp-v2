---
marp: true
theme: lpp-light
title: "LPP: Semana 11"
lang: es
size: 16:9
paginate: true
footer: "LPP · Tema 6: Programación orientada a objetos con Swift · Parte 2"
---

<!-- _class: cover institutional-cover -->
<!-- _paginate: false -->
<!-- _footer: "" -->
<div class="system-week">Semana 11</div>

# Protocolos y extensiones<br>en Swift

<div class="system-topics">Funciones operadoras y casting de tipos<br>Restricciones de tipos genéricos</div>
<div class="system-author">Cristina Pomares Puig</div>
<div class="institutional-logos">
<img class="university-logo" src="imagenes/logo-ua.svg" alt="Universitat d’Alacant · Universidad de Alicante">
<img class="department-logo" src="imagenes/logo-dccia.jpg" alt="Departamento de Ciencia de la Computación e Inteligencia Artificial">
</div>
<div class="mascot-figure cover-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>

<!-- Fuente: notas-clase/semana11/semana11.md. Diseño: semana 1, tema lpp-light. -->

---

## Veremos hoy

1. Funciones operadoras.
2. Protocolos y requisitos.
3. Protocolos como tipos y herencia de requisitos.
4. Comprobación y casting de tipos.
5. Genéricos con restricciones.
6. Extensiones de tipos existentes.

<!--
Marcas institucionales: https://imagenycomunicacion.ua.es/es/identidad-visual-corporativa-y-logotipos-ua.html
Logo DCCIA: https://web.ua.es/es/dccia/imagenes/gestadm/logotipos/logodccia.jpg
-->

<!--
Fuente: Veremos hoy. Notas de clase de la semana 11.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Funciones operadoras

<p class="lead">Definir el significado de un operador para nuestros tipos de datos.</p>

---

<!-- _class: lesson-code -->

## Sobrecarga de `+` para `Vector2D`

```swift
struct Vector2D {
    var x = 0.0, y = 0.0
    static func + (izquierdo: Vector2D, derecho: Vector2D) -> Vector2D {
        return Vector2D(x: izquierdo.x + derecho.x, y: izquierdo.y + derecho.y)
    }
}
```

La suma de dos vectores devuelve un vector nuevo. La función operadora se define aquí como miembro estático.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 41. Notas de clase de la semana 11.
La explicación antigua de las notas dice función global, pero el ejemplo la declara dentro de la estructura. Se describe la declaración real.
-->

---

<!-- _class: lesson-code -->

## Usar el operador infijo

```swift
let vector = Vector2D(x: 3.0, y: 1.0)
let otroVector = Vector2D(x: 2.0, y: 4.0)
let vectorSuma = vector + otroVector
// vectorSuma es una instancia de Vector2D con valores de (5.0, 5.0)
```

La notación del operador invoca la implementación para los tipos de sus operandos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 59. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Operador unario prefijo

```swift
   static prefix func - (vector: Vector2D) -> Vector2D {
       return Vector2D(x: -vector.x, y: -vector.y)
   }
```

Este método se añade dentro de `Vector2D`. `prefix` indica que se escribe antes de su operando.

<!--
Fuente: Operadores prefijos y postfijos. Notas de clase de la semana 11.
Se omite la elipsis del esqueleto de las notas; el fragmento es un miembro de Vector2D.
-->

---

<!-- _class: lesson-code -->

## Negación de un vector

```swift
let positivo = Vector2D(x: 3.0, y: 4.0)
let negativo = -positivo
// negativo es una instancia de Vector2D con valores de (-3.0, -4.0)
let tambienPositivo = -negativo
// tambienPositivo es una instancia de Vector2D con valores de (3.0, 4.0)
```

Negar dos veces produce los valores de las coordenadas originales.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 94. Notas de clase de la semana 11.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Protocolos

<p class="lead">Describir los requisitos que un tipo debe cumplir, sin fijar su implementación.</p>

---

## Adoptar y ajustarse a un protocolo

Un protocolo define requisitos de propiedades, métodos y otras operaciones.

Una clase, estructura o enumeración **adopta** el protocolo y **se ajusta** a él al satisfacer sus requisitos.

El código puede depender de esos requisitos sin depender de una implementación concreta.

<!--
Fuente: Adoptar y ajustarse a un protocolo. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Sintaxis de adopción

```swift
struct UnStruct: PrimerProtocolo, OtroProtocolo {
    // definición del struct
}
```

<!--
Fuente: Sintaxis de adopción. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Sintaxis de adopción (continuación)

```swift
class UnaClase: UnaSuperClase, PrimerProtocolo, OtroProtocolo {
    // definición de la clase
}
```

Una clase escribe primero su superclase y después los protocolos que adopta. Son esqueletos de sintaxis.

<!--
Fuente: Sintaxis de adopción. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Requisitos de propiedades

```swift
protocol UnProtocolo {
    var debeSerEscribible: Int { get set }
    var noTienePorQueSerEscribible: Int { get }
}
```

<!--
Fuente: Requisitos de propiedades. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Requisitos de propiedades (continuación)

```swift
protocol OtroProtocolo {
    static var unaPropiedadDeTipo: Int { get set }
}
```

`get set` exige lectura y escritura. `get` exige lectura, aunque la implementación también pueda permitir escritura.

<!--
Fuente: Requisitos de propiedades. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Un protocolo de nombre

```swift
protocol TieneNombre {
    var nombreCompleto: String { get }
}
```

<!--
Fuente: Un protocolo de nombre. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Un protocolo de nombre (continuación)

```swift
struct Persona: TieneNombre {
    var edad: Int
    var nombreCompleto: String
}
let john = Persona(edad: 35, nombreCompleto: "John Appleseed")
// john.nombreCompleto es "John Appleseed"
```

Una propiedad almacenada satisface el requisito de `nombreCompleto`.

<!--
Fuente: Un protocolo de nombre. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Otra implementación del mismo requisito

```swift
class NaveEstelar: TieneNombre {
    var prefijo: String?
    var nombre: String
    init(nombre: String, prefijo: String? = nil) {
        self.nombre = nombre
        self.prefijo = prefijo
    }
    var nombreCompleto: String {
        return (prefijo != nil ? prefijo! + " " : "") + nombre
    }
}
var ncc1701 = NaveEstelar(nombre: "Enterprise", prefijo: "USS")
// ncc1701.nombreCompleto es "USS Enterprise"
```

`NaveEstelar` proporciona `nombreCompleto` mediante una propiedad calculada.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 198. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Usar el protocolo como tipo

```swift
var algoConNombre: TieneNombre = ncc1701 // guardamos la nave estelar
algoConNombre = john // y ahora guardamos la persona
```

La variable puede contener una nave o una persona. A través del tipo protocolo accedemos a `nombreCompleto`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 219. Notas de clase de la semana 11.

-->

---

## Qué permite el tipo protocolo

```swift
print(algoConNombre.edad) 
// error: value of type 'TieneNombre' has no member 'edad'
```

Es un error intencionado. `edad` pertenece a `Persona`, pero no forma parte de los requisitos de `TieneNombre`.

<!--
Fuente: Qué permite el tipo protocolo. Notas de clase de la semana 11.
No confundir el tipo estático de la variable con el tipo concreto de la instancia.
-->

---

<!-- _class: lesson-code -->

## Requisitos de métodos

```swift
protocol GeneradorNumerosAleatorios {
    func random() -> Double
}
```

Cualquier implementación de `GeneradorNumerosAleatorios` debe proporcionar `random() -> Double`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 261. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Una implementación de prueba

```swift
class GeneradorNumerosAleatoriosFake: GeneradorNumerosAleatorios {
    private var numeros: [Double] = [0.2, 0.5, 0.8]
    private var indiceActual = 0
    func random() -> Double {
        let resultado = numeros[indiceActual]
        indiceActual = (indiceActual + 1) % numeros.count
        return resultado
    }
}
```

El generador devuelve cíclicamente `0.2`, `0.5` y `0.8`.

<!--
Fuente: Requisitos de métodos: generador de prueba. Notas de clase de la semana 11.
No es un generador aleatorio real. Sirve para probar el código que depende del protocolo.
-->

---

## Métodos mutadores en protocolos

```swift
protocol Conmutable {
    mutating func conmutar()
}
```

El requisito `mutating` permite que estructuras y enumeraciones cambien su valor. Una clase lo implementa sin ese modificador.

<!--
Fuente: Métodos mutadores en protocolos. Notas de clase de la semana 11.
El ejemplo Interruptor satisface el requisito mediante una mutación de self.
-->

---

<!-- _class: lesson-code -->

## Implementar el requisito en una enumeración

```swift
enum Interruptor: Conmutable {
    case apagado, encendido
    mutating func conmutar() {
        switch self {
        case .apagado:
            self = .encendido
        case .encendido:
            self = .apagado
        }
    }
}
```

<!--
Fuente: Requisito mutating: Interruptor. Notas de clase de la semana 11.
Caso apagado pasa a encendido y viceversa.
-->

---

<!-- _class: lesson-code -->

## Un dado que depende de un protocolo

```swift
class Dado {
    let caras: Int
    let generador: GeneradorNumerosAleatorios
    init(caras: Int, generador: GeneradorNumerosAleatorios) {
        self.caras = caras
        self.generador = generador
    }
    func tirar() -> Int {
        return Int(generador.random() * Double(caras)) + 1
    }
}
```

`Dado` necesita un generador, sin exigir una clase concreta. Supondremos `caras > 0` y valores de `random()` en `[0, 1)`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 352. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Probar el dado con resultados conocidos

```swift
var d6 = Dado(caras: 6, generador: GeneradorNumerosAleatoriosFake())
for _ in 1...5 {
    print("Tirada: \(d6.tirar())")
}
// Tirada: 2
// Tirada: 4
// Tirada: 5
// Tirada: 2
// Tirada: 4
```

El generador de prueba permite predecir las tiradas: `2`, `4`, `5`, `2`, `4`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 381. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Cambiar la implementación del generador

```swift
class GeneradorLinealCongruente: GeneradorNumerosAleatorios {
    var ultimoRandom = 42.0
    let m = 139968.0
    let a = 3877.0
    let c = 29573.0
    func random() -> Double {
        let number = ultimoRandom * a + c
        ultimoRandom = number.truncatingRemainder(dividingBy: m)
        return ultimoRandom / m
    }
}
```

<!--
Fuente: Protocolos como tipos: generador lineal congruente. Notas de clase de la semana 11.
Se muestra la clase completa. Se omite el bloque de prueba de las notas, que duplica la variable generador y deja una llave abierta.
-->

---

<!-- _class: lesson-code -->

## Reutilizar `Dado` con otro generador

```swift
var dado = Dado(caras: 6, generador: GeneradorLinealCongruente())
for _ in 1...5 {
    print("Tirada: \(dado.tirar())")
}
// Tirada: 3
// Tirada: 5
// Tirada: 4
// Tirada: 5
// Tirada: 4
```

No cambiamos la implementación de `Dado`: sustituimos el valor que satisface el protocolo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 429. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Colecciones de tipos protocolo

```swift
var peterParker = Persona(edad: 24, nombreCompleto: "Peter Parker")
var ncc1701 = NaveEstelar(nombre: "Enterprise", prefijo: "USS")
let cosasConNombre: [TieneNombre] = [peterParker, ncc1701]
for cosa in cosasConNombre {
   print(cosa.nombreCompleto)
}
// Peter Parker
// USS Enterprise
```

Los elementos tienen tipos concretos diferentes. El recorrido usa las operaciones de `TieneNombre`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 450. Notas de clase de la semana 11.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Igualdad y herencia de protocolos

<p class="lead">Compartir requisitos y expresar las operaciones disponibles para un tipo.</p>

---

<!-- _class: lesson-code -->

## Igualdad en una clase con `Equatable`

```swift
class Punto3D: Equatable {
    let x, y, z: Double
    init(x: Double, y: Double, z: Double) {
        self.x = x 
        self.y = y 
        self.z = z 
    }
    static func == (izquierda: Punto3D, derecha: Punto3D) -> Bool {
        return izquierda.x == derecha.x &&
            izquierda.y == derecha.y &&
            izquierda.z == derecha.z
    }
}
```

<!--
Fuente: Protocolo Equatable. Notas de clase de la semana 11.
La clase implementa == comparando coordenadas. != dispone de implementación a partir de la igualdad. Se compactan únicamente espacios y el salto de línea de return.
-->

---

<!-- _class: lesson-code -->

## Igualdad sintetizada en una estructura

```swift
struct Punto3D: Equatable {
    let x, y, z: Double
}
let p1 = Punto3D(x: 0.0, y: 0.0, z: 0.0)
let p2 = Punto3D(x: 0.0, y: 0.0, z: 0.0)
print(p1 == p2)
// Imprime true
print(p1 != p2)
// Imprime false
```

Swift puede sintetizar `==` si todas las propiedades almacenadas cumplen `Equatable`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 533. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Un protocolo que hereda requisitos

```swift
protocol Libro {
    var titulo: String { get }
    var autor: String { get }
}
protocol LibroPrestable: Libro {
    var estaPrestado: Bool { get set }
    mutating func prestar()
    mutating func devolver()
}
```

`LibroPrestable` exige también todos los requisitos de `Libro`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 565. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Implementación de un préstamo

```swift
struct LibroDeBiblioteca: LibroPrestable {
    var titulo: String
    var autor: String
    var estaPrestado: Bool = false
    mutating func prestar() {
        if !estaPrestado {
            estaPrestado = true
        } else {
            print("El libro ya está prestado.")
        }
    }
```

<!--
Fuente: Herencia en protocolos: LibroDeBiblioteca. Notas de clase de la semana 11.
Fragmento inicial de LibroDeBiblioteca. La estructura implementa también devolver(), mostrado a continuación.
-->

---

<!-- _class: lesson-code -->

## Implementación de la devolución

```swift
    mutating func devolver() {
        if estaPrestado {
            estaPrestado = false
        } else {
            print("El libro no está prestado.")
        }
    }
```

`devolver()` es el otro método mutador de `LibroDeBiblioteca`.

<!--
Fuente: Herencia en protocolos: devolver. Notas de clase de la semana 11.
El método pertenece a la misma estructura del fragmento anterior.
-->

---

<!-- _class: lesson-code -->

## Orden con `Comparable`

```swift
struct CoordPantalla : Comparable {
    var x: Int 
    var y: Int 
    static func < (primero: CoordPantalla, segundo: CoordPantalla) -> Bool { 
        return primero.x < segundo.x || 
               (primero.x == segundo.x && primero.y < segundo.y) 
    } 
}
```

`Comparable` exige el contrato de igualdad y orden. Aquí se compara primero `x` y, en caso de empate, `y`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 624. Notas de clase de la semana 11.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Casting de tipos

<p class="lead">Comprobar un tipo concreto o acceder a sus operaciones cuando el tipo estático es más general.</p>

---

<!-- _class: lesson-code -->

## Clase base de la biblioteca

```swift
class MediaItem {
    var nombre: String
    init(nombre: String) {
        self.nombre = nombre
    }
}
```

Cada elemento tiene un nombre. Las subclases añaden los datos que corresponden a su tipo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 677. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Dos subclases de `MediaItem`

```swift
class Pelicula: MediaItem {
    var director: String
    init(nombre: String, director: String) {
        self.director = director
        super.init(nombre: nombre)
    }
}
```

<!--
Fuente: Dos subclases de `MediaItem`. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Dos subclases de `MediaItem` (continuación)

```swift
class Cancion: MediaItem {
    var artista: String
    init(nombre: String, artista: String) {
        self.artista = artista
        super.init(nombre: nombre)
    }
}
```

`Pelicula` añade director. `Cancion` añade artista.

<!--
Fuente: Dos subclases de `MediaItem`. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Colección con tipo estático común

```swift
let biblioteca: [MediaItem] = [
    Pelicula(nombre: "El Señor de los Anillos", director: "Peter Jackson"),
    Cancion(nombre: "Child in Time", artista: "Deep Purple"),
    Pelicula(nombre: "El Puente de los Espías", director: "Steven Spielberg"),
    Cancion(nombre: "I Wish You Were Here", artista: "Pink Floyd"),
    Cancion(nombre: "Yellow", artista: "Coldplay")
]
```

La colección tiene tipo `[MediaItem]`. Los objetos conservan su tipo concreto en tiempo de ejecución.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 711. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Comprobar el tipo con `is`

```swift
var contadorPeliculas = 0
var contadorCanciones = 0
for item in biblioteca {
    if item is Pelicula {
        contadorPeliculas += 1
    } else if item is Cancion {
        contadorCanciones += 1
    }
}
```

La biblioteca contiene **dos películas y tres canciones**.

<!--
Fuente: Comprobación del tipo. Notas de clase de la semana 11.
Se corrigen las etiquetas invertidas del print de las notas. is no cambia el tipo estático del nombre item.
-->

---

<!-- _class: lesson-code -->

## Downcasting con `as?`

```swift
for item in biblioteca {
    if let pelicula = item as? Pelicula {
        print("Película: \(pelicula.nombre), dir. \(pelicula.director)")
    } else if let cancion = item as? Cancion {
        print("Cancion: \(cancion.nombre), de \(cancion.artista)")
    }
}
```

`as?` devuelve un opcional. El ligado permite acceder al director o al artista cuando la conversión tiene éxito.

<!--
Fuente: Downcasting. Notas de clase de la semana 11.
Evitar describir el cast como creación o transformación del objeto.
-->

---

<!-- _class: lesson-code -->

## Seleccionar tipos mediante `switch`

```swift
for item in biblioteca {
    switch item {
    case let pelicula as Pelicula:
        print("Película: \(pelicula.nombre), dir. \(pelicula.director)")
    case let cancion as Cancion:
        print("Cancion: \(cancion.nombre), de \(cancion.artista)")
    default:
        break
    }
}
```

`case let ... as Tipo` comprueba el tipo y proporciona un nombre con el que usar sus operaciones.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 824. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## El tipo `Any`

```swift
var array = [Any]()
array.append(0)
array.append(0.0)
array.append(42)
array.append(3.14159)
array.append("hola")
array.append((3.0, 5.0))
array.append(Pelicula(nombre: "Ghostbusters", director: "Ivan Reitman"))
array.append({ (name: String) -> String in "Hola, \(name)" })
```

Puede contener valores de cualquier tipo, incluidas tuplas y funciones. Para usarlos necesitamos conocer sus operaciones.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 846. Notas de clase de la semana 11.

-->

---

## Patrones sobre valores de tipo `Any`

En un `switch` podemos combinar:

- Un valor concreto y su tipo: `case 0 as Int`.
- Un ligado al tipo: `case let texto as String`.
- Una comprobación: `case is Double`.
- Una condición adicional con `where`.

El caso `default` recoge los valores no contemplados.

<!--
Fuente: Patrones sobre valores de tipo `Any`. Notas de clase de la semana 11.
El ejemplo completo de las notas combina números, cadenas, tuplas, películas y funciones.
-->

---

## Comprobar el ajuste a un protocolo

```swift
protocol TieneArea {
    var area: Double { get }
}
```

Un tipo puede proporcionar el requisito `area` como propiedad calculada o como propiedad almacenada.

<!-- Fuente: Comprobación de ajustarse a un protocolo. Notas de clase de la semana 11. -->

---

<!-- _class: lesson-code -->

## Dos clases que proporcionan un área

```swift
class Circulo: TieneArea {
    let pi = 3.1415927
    var radio: Double
    var area: Double { return pi * radio * radio }
    init(radio: Double) { self.radio = radio }
}
class Pais: TieneArea {
    var area: Double
    init(area: Double) { self.area = area }
}
```

La representación de la propiedad puede cambiar entre tipos; el requisito accesible es el mismo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 921. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Objetos con y sin área

```swift
class Animal {
    var patas: Int
    init(patas: Int) { self.patas = patas }
}
```

```swift
let objetos: [Any] = [
    Circulo(radio: 2.0),
    Pais(area: 243_610),
    Animal(patas: 4)
]
```

<!-- Fuente: Comprobación de ajustarse a un protocolo. Notas de clase de la semana 11. Animal no se ajusta a TieneArea. -->

---

<!-- _class: lesson-code -->

## Casting al tipo protocolo

```swift
for objecto in objetos {
    if let objetoConArea = objecto as? TieneArea {
        print("El área es \(objetoConArea.area)")
    } else {
        print("Algo que no tiene un área")
    }
}
// El área es 12.5663708
// El área es 243610.0
// Algo que no tiene un área
```

`objetoConArea` dispone de la propiedad requerida sin depender de la clase concreta.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 967. Notas de clase de la semana 11.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Restricciones de tipos genéricos

<p class="lead">Indicar qué operaciones deben admitir los tipos usados por un algoritmo.</p>

---

## De una pila de enteros a una pila genérica

<div class="columns equal">
<div>

```swift
struct IntStack {
    var items = [Int]()
    mutating func push(_ item: Int) {
        items.append(item)
    }
    mutating func pop() -> Int {
        return items.removeLast()
    }
}
```

</div>
<div>

```swift
struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}
```

</div>
</div>

`Element` sustituye al tipo fijo de los elementos. `pop()` exige que la pila no esté vacía.

<!--
Fuente: De una pila de enteros a una pila genérica. Notas de clase de la semana 11.

-->

---

## Usar una pila de cadenas

<div class="columns equal">
<div>

```swift
var stackOfStrings = Stack<String>()
stackOfStrings.push("uno")
stackOfStrings.push("dos")
stackOfStrings.push("tres")
stackOfStrings.push("cuatro")
// la pila contiene ahora 4 cadenas
```

</div>
<div>

```swift
let fromTheTop = stackOfStrings.pop()
```

</div>
</div>

La estructura mantiene el mismo tipo de elemento en las inserciones y en las extracciones.

<!--
Fuente: Usar una pila de cadenas. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Buscar el índice de una cadena

```swift
func findIndex(ofString valueToFind: String, in array: [String]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

La comparación `==` está disponible para cadenas. La búsqueda puede no encontrar el valor: devuelve un opcional.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1068. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Una generalización insuficiente

```swift
func findIndex<T>(of valueToFind: T, in array: [T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

Es un error intencionado: un parámetro de tipo `T` sin restricciones no garantiza que exista `==`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1093. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Restringir `T` a `Equatable`

```swift
func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

La restricción expresa exactamente la operación que necesita el algoritmo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1114. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Buscar con otro tipo de dato

```swift
let doubleIndex = findIndex(of: 9.3, in: [3.14159, 0.1, 0.25, 9.3])
// devuelve Int? 3
```

Los índices del array comienzan en `0`. El valor `9.3` se encuentra en la posición `3`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1128. Notas de clase de la semana 11.
Se corrige el comentario de las notas, que daba índice 2.
-->

---

<!-- _class: lesson-code -->

## Restricciones en dos parámetros de tipo

```swift
func reproducirSonido<T: Animal, U: EmisorDeSonido>(animal: T, emisorDeSonido: U) {
    let sonido = emisorDeSonido.emitirSonido()
    print("\(animal.nombre) emite el sonido: \(sonido)")
}
```

`T` debe heredar de `Animal`; `U` debe ajustarse a `EmisorDeSonido`. Son requisitos independientes.

<!--
Fuente: Restricciones en varios tipos genéricos. Notas de clase de la semana 11.
Es la variante de Animal que tiene nombre, distinta de la usada antes para el ejemplo de áreas.
-->

---

<!-- _class: lesson-code -->

## Aplicar las dos restricciones

```swift
class Perro: Animal {}
class Silbato: EmisorDeSonido {
    func emitirSonido() -> String {
        return "silbido"
    }
}
```

```swift
let perro = Perro(nombre: "Fido")
let silbato = Silbato()
reproducirSonido(animal: perro, emisorDeSonido: silbato)
```

<!--
Fuente: Restricciones: Perro y Silbato. Notas de clase de la semana 11.
El ejemplo presupone Animal(nombre:) y EmisorDeSonido de las notas.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 11</div>

# Extensiones

<p class="lead">Añadir funcionalidad a un tipo existente sin modificar su definición original.</p>

---

## Qué puede añadir una extensión

- Propiedades calculadas.
- Métodos de instancia o del tipo.
- Inicializadores adicionales dentro de las reglas del tipo.
- Ajuste a protocolos.

Una extensión no añade propiedades almacenadas de instancia ni sobreescribe funcionalidades existentes.

<!--
Fuente: Qué puede añadir una extensión. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Extender `Persona` con una propiedad

```swift
extension Persona {
   var mayorEdad: Bool {
      return edad >= 18
   }
}
```

<!--
Fuente: Extender `Persona` con una propiedad. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Extender `Persona` con una propiedad (continuación)

```swift
var p = Persona(edad: 15, nombreCompleto: "Lucía")
p.mayorEdad // false
```

La nueva propiedad calcula el resultado a partir de `edad`.

<!--
Fuente: Extender `Persona` con una propiedad. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Datos del rectángulo

```swift
struct Tamaño {
    var ancho = 0.0, alto = 0.0
}
struct Punto {
    var x = 0.0, y = 0.0
}
struct Rectangulo {
    var origen = Punto()
    var tamaño = Tamaño()
}
```

La estructura conserva los inicializadores sintetizados por sus valores por defecto.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1254. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Añadir un inicializador en una extensión

```swift
extension Rectangulo {
    init(centro: Punto, tamaño: Tamaño) {
        let origenX = centro.x - (tamaño.ancho / 2)
        let origenY = centro.y - (tamaño.alto / 2)
        self.init(origen: Punto(x: origenX, y: origenY), tamaño: tamaño)
    }
 }
```

La delegación a `self.init` reutiliza el inicializador por propiedades. Es una ampliación externa a la definición original.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1282. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Añadir un método de instancia

```swift
extension Persona {
    func descripcion() -> String {
        return "Me llamo \(nombreCompleto) y tengo \(edad) años"
    }
}
let reedRichards = Persona(edad: 40, nombreCompleto: "Reed Richards")
print(reedRichards.descripcion())
```

El método puede acceder a los miembros de `Persona` para producir una descripción.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1311. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Extender un tipo de la biblioteca estándar

```swift
extension Int {
    func repeticiones(_ tarea: () -> Void) {
        for _ in 0..<self {
            tarea()
        }
    }
}
```

`repeticiones` recibe una tarea de tipo `() -> Void`. El ejemplo presupone un entero no negativo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1325. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Usar el método con una clausura al final

```swift
3.repeticiones {
   print("Adios!")
}
// Adios!
// Adios!
// Adios!
```

La tarea se ejecuta tres veces. Esta sintaxis es una clausura al final, no recursión por la cola.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1353. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Índices de una cadena

```swift
let cadena = "Hola"
let posicion = 2
let index = cadena.index(cadena.startIndex, offsetBy: posicion)
cadena[index] // Devuelve "l"
```

Las posiciones de `String` usan `String.Index`, no un índice entero directo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1369. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Añadir un acceso mediante posición

```swift
extension String {
    func at(_ pos: Int) -> Character {
        let index = self.index(self.startIndex, offsetBy: pos)
        return self[index]
    }
}
```

La posición debe estar dentro de los límites de la cadena. El método devuelve un `Character`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1379. Notas de clase de la semana 11.

-->

---

<!-- _class: lesson-code -->

## Definir un subíndice

```swift
extension String {
    subscript (pos: Int) -> Character {
        let index = self.index(self.startIndex, offsetBy: pos)
        return self[index]
    }
}
"Hola"[3] // devuelve "a"
```

La extensión habilita la notación de corchetes. También exige una posición válida.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 1392. Notas de clase de la semana 11.

-->
