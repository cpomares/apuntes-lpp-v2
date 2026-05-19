# Lab 12: Object-Oriented Programming in Swift (2)

## Before the Lab Session

The following exercises are based on the theory concepts covered last week.
Before the lab session, you should review all the concepts and **try with the
Swift compiler** all the examples from the following sections of topic 6
[_Object-Oriented Programming with
Swift_](../../theory/topic06-object-oriented-programming-swift/topic06-object-oriented-programming-swift.md#7-operator-functions)

- Operator functions
- Protocols
- Type casting
- Generics
- Extensions


## Exercises

### Exercise 1 ###

a) Complete the code of the `MiStruct` structure so that it compiles correctly.
Do it first on paper and then try it in the compiler.

```swift
protocol A {
    var a: String {get}
    func foo(a: String) -> String?
}
protocol B {
    mutating func bar()
}
struct MiStruct: A, B {
    // Completa el código
}
```

b) The following code has errors. Try to discover what they are without using the
compiler. Try different ways of fixing the code while changing as little as
possible of what is already defined (for example, you must not add new
properties to `MiStruct`). Check it with the compiler.

```swift
protocol A {
    var a: String {get set}
    func foo(a: Int, b: Int) -> Int?
}

protocol B {
    mutating func bar()
}

struct MiStruct: A, B {
    let a = 10
    func foo(valor1 a: Int, valor2 b: Int) -> Int {
        let res = a > 10 ? a: b
        return res
    }
}
```

c) Suppose we have the `Equipo` structure shown below, which represents a team in
a sports competition:

```swift
struct Equipo {
    let puntos: Int
    let nombre: String
}
```

Modify the definition so that two teams can be checked for equality and the
following code works correctly:

```swift
let equipo1 = Equipo(puntos: 10, nombre: "Hércules")
let equipo2 = Equipo(puntos: 8, nombre: "Villareal")
print(equipo1 == equipo2) // imprime false
```

Then modify the code again so that the structure also conforms to the
`Comparable` protocol, so two teams can be compared. Consult the protocol in the
[Swift documentation](https://developer.apple.com/documentation/swift/comparable).
A team is smaller than another when it has fewer points. If both have the same
points, the smaller one is the one with the alphabetically smaller name.

```swift
print(equipo1 > equipo2) // imprime true
```

Once the necessary operators have been defined, check that they work correctly by
creating several teams, inserting them into an array, and calling the `sorted`
method.

### Exercise 2 ###

a) Complete the following code so that it compiles correctly and prints the
indicated output:

```swift
struct Cuadrado {
    var lado: Double
}

// Completa el código justo a continuación,
// no puedes modificar el código anterior

var cuadrado = Cuadrado(lado: 4.0)
print(cuadrado.area) // Imprime: 16.0
cuadrado.lado = 10.0
print(cuadrado.area) // Imprime: 100.0

```

b) Fill in the following code so that it works correctly:

```swift
protocol Persona {
    var nombre: String {get}
    func encantada() -> Persona 
    func refrescada() -> Persona 
}

enum Pocion {
    case magica, refrescante, venenosa

    func esBebida(por persona: Persona) -> __________ {
        ______________ {
            case _________:
                return persona.encantada()
            case _________:
                return persona.refrescada()
            default:
                return nil
        }
    }
}
```

c) Complete the code of the `MiStruct` structure so that it compiles correctly:

```swift
protocol A {
    var valor: Int {get set}
    func foo(a: Int) -> Int
}
protocol B {
    mutating func bar()
}
struct MiStruct: A, B {
    // Completa el código

}
```

d) Complete the following code so that it compiles correctly and prints the
indicated output:

```swift
struct Circulo {
    var radio: Double
    // Completa el código

}

let c1 = Circulo(radio: 5.0)
let c2 = Circulo(radio: 10.0)
let c3 = c1 + c2
print("El radio de la suma es: \(c3.radio)")
// Imprime: El radio de la suma es: 15.0
```


### Exercise 3 ##


a) Complete the loop with the code that checks the type of variable `i` and
prints its `p` property and its `a1` or `a2` property, depending on its type.

```swift
protocol P {
   var p: Int { get }
}
class A1: P {
   var p = 0
   var a1 = 0
}
class A2: P {
   var p = 1
   var a2 = 0
}

var array: [P] = [A1(), A2()]
for i in array {

   // Código a completar
   //
}

// debe imprimir:
// debe imprimir:
// p: 0, a1: 0
// p: 1, a2: 0
```

b) Complete the code below so that it compiles correctly and the shown result
appears on screen.

```swift

protocol TieneVelocidad {
    func velocidadActual () -> Double
}

class Vehiculo {
    var velocidad = 0.0
    func velocidadActual() -> Double {
        return velocidad
    }
}

class Tren {
    static let velocidadEnMarcha = 300.0
    var pasajeros = 0
    var enMarcha = false
}

//
// Código a completar
//

var vehiculo1 = Vehiculo()
var tren1 = Tren()
tren1.enMarcha = true

let transportes: [TieneVelocidad] = [vehiculo1, tren1]

for i in transportes {
    print(i.velocidadActual())
}
// 0.0
// 300.0
```

### Exercise 4 ###

Define a `Timer` structure with which we can run the following code without
errors. The timer is initialized with a given number of seconds and defines an
instance method `paso()` that subtracts one second. Notice in the code that it is
possible to add timers. Finally, the type attribute `pasosTotales` stores the
number of steps taken across all instances.

```swift
var t1 = Timer(segundos: 10)
var t2 = Timer(segundos: 5)
for _ in 0...4 {
    t1.paso()
}
for _ in 0...2 {
    t2.paso()
}
var t3 = t1 + t2
t3.paso()
print("Segundos del temporizador 1: \(t1.segundos)")
print("Segundos del temporizador 2: \(t2.segundos)")
print("Segundos del temporizador 3: \(t3.segundos)")
print("Pasos totales: \(Timer.pasosTotales)")
// Imprime:
// Segundos del temporizador 1: 5
// Segundos del temporizador 2: 2
// Segundos del temporizador 3: 6
// Pasos totales: 9
```

### Exercise 5

Finally, we move to an exercise where we will see another way to work with
geometric figures.

#### 1. Complete the Initial Code ####

Start by including in the lab the code for the definitions of the geometric
structures: `Punto`, `Tamaño`, `Rectangulo`, and `Circulo`. You must complete the
code so that it does what is indicated in the comments.

```swift
struct Punto {
    var x = 0.0, y = 0.0
}

struct Tamaño {
    var ancho = 0.0, alto = 0.0
}

struct Circulo {
    var centro = Punto()
    var radio = 0.0
    
    var area: Double {
        // Propiedad calculada que devuelve el 
        // área del círculo y modifica el radio
        // cuando se actualiza
    }
}

struct Rectangulo {
    var origen = Punto()
    var tamaño = Tamaño()

    var centro: Punto {
        // Propiedad calculada que devuelve el 
        // centro del rectángulo y traslada su
        // origen cuando se modifica
    }

    var area: Double {
        // Propiedad calculada que devuelve el
        // área del rectángulo
    }
}
```

Try the structures by writing some code where you create a few instances and
update their properties.

#### 2. Define the Figure Protocol

Define the `Figura` protocol containing:

- Read-write property `centro` (`Punto`), which defines the center of the figure.
- Read-only properties `area` (`Double`) and `tamaño` (`Tamaño`), which return
  the size (height and width) of the figure.
- Method `descripcion()` that returns a `String` with the center and the area of
  the figure.

#### 3. Define Extensions

- Modify the `Rectangulo` and `Circulo` structures so that they conform to the
  `Figura` protocol, adding the necessary implementation code.

- Try the code written so far by creating an array of type `Figura` (the
  protocol) and adding circles and rectangles to it.

#### 4. `AlmacenFiguras` Structure

Finally, implement an `AlmacenFiguras` structure.

- It must have a single property `figuras` containing an array of figures. As in
  the previous lab, define in it the method `añade(figura:)` and the computed
  properties `numFiguras` (`Int`) and `areaTotal` (`Double`).

- Write the method `cuentaTipos() -> (Int, Int)`, which traverses the array of
figures and returns a tuple with two integers: number of rectangles and number of
circles. The function must print, for each figure in the array, the type of
figure, its description, and, if the figure is a rectangle, its size.

For example:

```
** Un rectángulo con tamaño Tamaño(ancho: 10.0, alto: 5.0) y descripción:
Centro: Punto(x: 8.0, y: 6.5) y área: 50.0
** Un círculo con descripción:
Centro: Punto(x: 5.0, y: 0.0) y área: 314.1592653589793
```

- Write an example of code where several figures are stored in a figure store
and its methods are called.


### Exercise 6 ###

In this exercise we will work with **protocol-oriented programming**. We consider
an element to be `Avisable` if it has:

- a read-only `nombre`;
- a `bateria`, which can be queried and modified;
- an `aviso()` method that returns a `String`.

In addition, all types that adopt the `Avisable` protocol will have a default
implementation of `aviso()` through a protocol extension.

a) Complete the code:

```swift
protocol Avisable {
    // Hueco 1:
    // Declara la propiedad nombre, de tipo String, solo lectura

    // Hueco 2:
    // Declara la propiedad bateria, de tipo Int, lectura y escritura

    // Hueco 3:
    // Declara el método aviso(), que devuelve un String
}
```

The default implementation of `aviso()` must return:

- `"Aviso: batería baja en <nombre>"` if the battery is less than 20.
- `"Batería suficiente en <nombre>"` otherwise.

```swift
extension Avisable {
    func aviso() -> String {
        // Hueco 4:
        // Escribe aquí la implementación por defecto del método aviso()
    }
}
```

b) Two types that adopt the `Avisable` protocol are now defined.

The `Sensor` type will use the default implementation of `aviso()`.

The `Robot` type, on the other hand, will have its own implementation of
`aviso()`:

- `"Robot <nombre> necesita recarga urgente"` if the battery is less than 20.
- `"Robot <nombre> operativo"` otherwise.

Complete the code:

```swift
struct Sensor: Avisable {
    let nombre: String
    var bateria: Int
    let ubicacion: String
}

struct Robot: Avisable {
    let nombre: String
    var bateria: Int
    let modelo: String

    // Hueco 5:
    // Implementa aquí el método aviso() específico para Robot
}
```

c) Complete the following code to create an array that can contain both robots
and sensors and call the `aviso()` method on all of them.

```swift
let robot1 = Robot(nombre: "R2", bateria: 15, modelo: "explorador")
let robot2 = Robot(nombre: "T7", bateria: 80, modelo: "transporte")
let sensor1 = Sensor(nombre: "S1", bateria: 10, ubicacion: "laboratorio")
let sensor2 = Sensor(nombre: "S2", bateria: 60, ubicacion: "almacén")

// Hueco 6:
// Declara un array llamado elementos que pueda contener valores
// de cualquier tipo que adopte Avisable.
// El array debe contener robot1, robot2, sensor1 y sensor2.


// Hueco 7:
// Recorre el array elementos e imprime el resultado de llamar
// al método aviso() de cada elemento.
```

d) Answer the following questions:

1. Why does `Sensor` not need to implement its own `aviso()` method?
2. Why can `Robot` define its own version of `aviso()`?
3. What is the advantage of declaring the array as `[Avisable]`?
4. What messages will be printed when the last code fragment is executed?

----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez

