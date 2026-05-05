# Topic 5: Functional Programming with Swift

## 1. Introduction

We recommend reading the Swift seminar, which introduces the language and
explains how to run programs written in it:

- [Swift Seminar](../../seminars/seminar02-swift/seminar02-swift.md)


### 1.2. Fundamental Concepts of Functional Programming ###

In this topic, we are going to review how Swift implements mainly functional
concepts such as:

- Immutable values
- Recursive data types
- Functions as first-class objects and closures
- Higher-order functions

Let's quickly review some basic functional programming concepts seen in the
first topics of the course.

Functional Programming:

> Functional Programming is a programming paradigm that treats computation as
> the evaluation of mathematical functions and avoids state changes and mutable
> data.

Mathematical or pure functions:

> Mathematical functions have the characteristic that, when invoked with the
> same argument, they always return the same result.

Functions as first-class objects:

> In functional programming, functions are first-class objects in the language,
> similar to integers or _strings_. We can pass functions as arguments to
> so-called _higher-order functions_ or return functions created at runtime
> (closures).

### 1.3. Basic Features of Swift ###

Swift is primarily an imperative language, but its design introduced modern
functional programming concepts drawn from languages such as Rust or Haskell.
Therefore, it can be considered a **multi-paradigm** language, in which we can
define functional code that can be executed together with imperative code.

As its creator [Chris Lattner](http://nondot.org/sabre/) says:

> The Swift language is the product of tireless effort from a team of language
> experts, documentation gurus, compiler optimization ninjas, and an incredibly
> important internal dogfooding group. Of course, it also greatly benefited from
> experiences hard-won by many other languages, drawing ideas from Objective-C,
> Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list.

#### 1.3.1. Strongly Typed Language ####

Unlike Scheme, Swift is a **strongly typed** language in which the types of
variables, parameters, and functions must be defined.

For example, in the following statements we define variables of
different types:

```swift
let n: Int = 10
let str: String = "Hola"
let array: [Int] = [1,2,3,4,5]
```

The Swift compiler can identify the types of variables when an assignment is
made. This technique is called **type inference** and allows variables to be
declared without writing their type. For example, the previous variables can
also be declared like this:

```swift
let n = 10
let str = "Hola"
let array = [1,2,3,4,5]
```

Although we have not explicitly declared the type of the variables, the
compiler has assigned them the corresponding type. For example, we cannot
assign them a value of a different type:

```swift
var x = 5
x = 4 // correcto
x = 6.0 // error
// error: cannot assign value of type 'Double' to type 'Int'
// x = 5.0
//     ^~~
//    Int( )
```

The compiler reports the error and even suggests a possible solution. In this
case, it suggests calling the `Int()` constructor and passing it a `Double` as a
parameter.

#### 1.3.2. Multi-Paradigm Language ####

Swift allows us to combine functional features with imperative and
object-oriented programming features. We will see in this topic that Swift has
many functional features that we can use in any Swift program we develop. For
example, when we declare a variable we can declare it as
mutable, using the `var` declaration, or as immutable, using the
declaration `let`. If we want to use a functional approach, we will always
prefer to declare variables with `let`. 

```swift
var x = 10
x = 20 // x es mutable
let y = 10
y = 20 // error: y es inmutable
```

One advantage of immutability is that it allows the Swift compiler to optimize
the code very efficiently. In fact, the compiler itself tells us that it is
preferable to define a variable with `let` if we are not going to modify it:

```swift
func saluda(nombre: String) -> String {
    var saludo = "Hola " + nombre + "!"
    return saludo
}
//warning: variable 'saludo' was never mutated; consider changing to 'let' constant
//    var saludo = "Hola " + nombre
//    ~~~ ^
//    let
```


## 2. Immutability

One of Swift's important functional features is its emphasis on immutability
to reinforce language safety. 

We have seen that the keyword `let` allows us to define constants, and that
Swift recommends using it when the value we define will not be modified.

The value assigned to a constant `let` may not be known in time
compilation, but can be obtained at run time
as a value returned by a function:

```swift
let respuesta: String = respuestaUsuario.respuesta()
```

Declaring a variable with `let` locks its contents and does not allow it to be
modified. One of the advantages of the functional paradigm and immutability is
that it guarantees that the code we write has no side effects and can be
executed safely in multi-processor or multi-threaded environments.

### 2.1. Creation of new structures and mutation

In the [standard library
Swift](https://developer.apple.com/documentation/swift/swift_standard_library)
There are a large number of structures (such as `Int`, `Double`,
`Bool`, `String`, `Array`, `Dictionary`, etc.) which have two types of
methods: methods that mutate the structure and methods that return a
new structure. When we are writing code in a functional style we must always use these last methods, which
They build new structures.

For example, in the struct `Array` the method `sort` is defined and the
method `sorted`. The first sorts the array by mutation and the second
returns an ordered copy, without modifying the original array. In the
following code does not modify the original array, but rather
build a new sorted array:


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

This code is recommended when we are writing in a functional programming style.

However, the following code is imperative and uses the mutation of the original array:

```swift
// Código no recomendable en programación funcional
// porque utiliza el método sort que muta el array original
var miArray = [10, -1, 3, 80]
miArray.sort()
print(miArray)
// Imprime:
// [-1, 3, 10, 80]
```

Another example is in the way of adding elements to an array. we can
do it with a functional approach, using the `+` operator that builds
a new array:

```swift
// Código recomendable en programación funcional
let miArray = [10, -1, 3, 80]
let array2 = miArray + [100]
print(array2)
// Imprime:
// [10, -1, 3, 80, 100]
```

And we can do it using an imperative approach, with the method
`append`:

```swift
// Código no recomendable en programación funcional
var miArray = [10, -1, 3, 80]
miArray.append(100)
print(miArray)
// Imprime:
// [10, -1, 3, 80, 100]
```

!!! Important "Important"
    In functional programming we must always use the methods
    **that do not modify the structures**. This way we will avoid the effects
    sides and our code will work correctly in environments
    multi-thread.

When we define a variable of type `let` the value that is
assign to that variable becomes immutable. If it is a
structure or a class with mutable methods the compiler will give a
error. For example:

```swift
let miArray = [10, -1, 3, 80]
miArray.append(100)
// error: cannot use mutating member on immutable value: 'miArray' is a 'let' constant
```

Another example: the `append(_:)` method of a `String` is a mutating method.
If we define a string with `let`, we will not be able to modify it and the
following code will produce an error:

```swift
var cadenaMutable = "Hola"
let cadenaInmutable = "Adios"
cadenaMutable.append(cadenaInmutable) // cadenaMutable es "HolaAdios"
cadenaInmutable.append("Adios")
// error: cannot use mutating member on immutable value: 'cadenaInmutable' is a 'let' constant
```


## 3. Functions


### 3.1. Defining a Function in Swift

To define a function in Swift you must use the keyword `func`, define the name
of the function, its parameters, and the type of the returned value. The value
returned by the function must be returned using the keyword `return`.

`saluda(nombre:)` function code:

```swift
func saluda(nombre: String) -> String {
    let saludo = "Hola, " + nombre + "!"
    return saludo
}
```

A feature of Swift is that to invoke the function it is
necessary to precede the argument with the label defined by the name
of the parameter.

For example, it would be a mistake to call the above function from
following way:

```swift
// Error: hay que especificar la etiqueta `nombre:`
print(saluda("Ana"))
```

The correct way to call the function is as follows:

```swift
print(saluda(nombre:"Ana"))
print(saluda(nombre:"Pedro"))
// Imprime "Hola, Ana!"
// Imprime "Hola, Pedro!"
```

This Swift feature makes code more readable and
easy to understand as we can clearly see what the purpose is
of each argument when calling the function. 

For example, we can also have another similar function that returns
a greeting receiving the name and age of a person:

```swift
func crearSaludo(nombre: String, edad: Int) -> String {
    return "Hola, \(nombre)! Tienes \(edad) años."
}

let saludo = crearSaludo(nombre: "Carlos", edad: 25)
print(saludo)
```

By calling the function `crearSaludo` it is clear that we are passing
the name and age of the person we want to greet.


### 3.2. Argument Labels and Parameter Names

It is possible to make the argument label (external name) different
with which to call the function) of the parameter name
(internal name used in the function body):

```swift
func saluda(nombre: String, de ciudad: String) -> String {
    return "Hola \(nombre)! Me alegro de que hayas podido visitarnos desde \(ciudad)."
}
print(saluda(nombre: "Bill", de: "Cupertino"))
// Imprime "Hola Bill! Me alegro de que hayas podido visitarnos desde Cupertino."
```

In this case the external name of the parameter, the one we use when invoking
the function is `de` and the internal name is the one used in the body of
the function is `ciudad`.

Another example, the following function `concatena(palabra:con:)`: 

```swift
func concatena(palabra str1: String, con str2: String) -> String {
    return str1+str2
}

print(concatena(palabra:"Hola", con:"adios"))
```

If you do not want an argument label for a parameter, you can
write an underscore (`_`) instead of an explicit argument label for that
parameter. This allows us to call the function without using a parameter name. For example, the function `max(_:_:)` and the
function `divide(_:entre:)`:

```swift
func max(_ x: Int, _ y: Int) -> Int {
   if x > y {
      return x
   } else {
      return y
   }
}

print(max(10,3))

func divide(_ x: Double, entre y: Double) -> Double {
   return x / y
}

print(divide(30, entre:4))
```

The function signature (also called the function profile) is made up of the
function name, the argument labels and their types, and the type returned by the
function.

For example, in the previous case, the signature of the `max` function would be:

- Name: `max`
- Parameter list: `(_ x: Int, _ y: Int)`
- Return type: `Int`

And the signature of the `divide` function would be:

- Name: `divide`
- Parameter list: `(_ x: Double, entre y: Double)`
- Return type: `Double`

This signature allows the compiler and programmer to identify and
differentiate functions with the same name but with different lists
of parameters or return types.

In the documentation of functions in Swift it is usually used to
name them their full name: the name of the function itself plus the
name of the parameters. For example, the above functions are
named as `max(_:_:)` and `divide(_:entre:)`.

As we have said, the parameter names are part of the name
complete function. It is possible to define different functions with
just different parameter names, like the following functions
`mitad(par:)` and `mitad(impar:)`:

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

### 3.3. Parameters and Return Values

It is possible to define functions without parameters:

```swift
func diHolaMundo() -> String {
    return "hola, mundo"
}
print(diHolaMundo())
// Imprime "hola, mundo"
```

We can define functions without a return value. For example, the
next function `diAdios(nombre:)`. You don't have to write an arrow with it
returned type. Be careful, it would not be functional programming properly.

```swift
func diAdios(nombre: String) {
    print("Adiós, \(nombre)!")
}
diAdios(nombre:"Dave")
// Imprime "Adiós, Dave!"
```

It is possible to return multiple values, constructing a tuple. By
For example, the following function `ecuacion(a:b:c:)` calculates both
solutions of a second degree equation:

```swift
func ecuacion(a: Double, b: Double, c: Double) -> (pos: Double, neg: Double) {
    let discriminante = b*b-4*a*c
    let raizPositiva = (-b + discriminante.squareRoot()) / 2*a
    let raizNegativa = (-b - discriminante.squareRoot()) / 2*a
    return (raizPositiva, raizNegativa)
}
```
Let's remember (see the Swift seminar) that we can access the
tuple values by position:

```swift
let resultado = ecuacion(a: 1, b: -5, c: 6)
print("Las raíces de la ecuación son \(resultado.0) y \(resultado.1)")
//Imprime "Las raíces de la ecuación son 3.0 y 2.0"
```

In this case in the definition of the type returned by the function we are
tagging those values with the tags `pos` and `neg`. Of this
way we can access the components of the tuple using those
defined tags:

```swift
let resultado = ecuacion(a: 1, b: -5, c: 6)
print("Las raíces de la ecuación son \(resultado.pos) y \(resultado.neg)")
//Imprime "Las raíces de la ecuación son 3.0 y 2.0"
```

## 4. Recursion

Let's look at some examples of recursive functions in Swift.

First a function `suma(hasta:)` that returns the sum from 0 to
the number that we pass as a parameter.

```swift
func suma(hasta x: Int) -> Int {
  if x == 0 {
    return 0
  } else {
    return x + suma(hasta: x - 1)
  }
}

print(suma(hasta: 5))
// Imprime "15"
```

It is also possible to define recursions that traverse arrays in a
similar to how we worked at Scheme. Arrays in Swift do not
They work exactly like Scheme lists (they are not lists of
pairs), but we can get the first element and the rest of the
following way.

```swift
let a = [10, 20, 30, 40, 50, 60]
let primero = a[0]
let resto = Array(a.dropFirst())
```

The number 10 is stored in `primero`. The number 10 is stored in `resto`
from 20 to 60. The `dropFirst` method returns a `ArraySlice`, which is
a view of a range of elements of the array, in this case the one that goes
from position 1 to 5 (the starting position of an array is the
0). You need the `Array` constructor to convert that
`ArraySlice` on a `Array`.

Using the previous instructions we can define the recursive function that adds the
values of an Array in the following way similar to how we did it
in Scheme:

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

A final example is the following function `minMax(array:)` which
returns the smallest and largest number in an array of integers:

```swift
func minMax(array: [Int]) -> (min: Int, max: Int) {
    if (array.count == 1) {
        return (array[0], array[0])
    } else {
        let primero = array[0]
        let resto = Array(array.dropFirst())

        // Llamada recursiva que devuelve el mínimo y el máximo del
        // resto del array
        let minMaxResto = minMax(array: resto)

        let minimo = min(primero, minMaxResto.min)
        let maximo = max(primero, minMaxResto.max)
        return (minimo, maximo)
    }
}

let limites = minMax(array: [8, -6, 2, 100, 3, 71])
print("El mínimo es \(limites.min) y el máximo es \(limites.max)")
// Imprime "El mímimo es -6 y el máximo es 100"
```

In this example we depart a little from the solution seen in Scheme
because we allow execution steps that initialize variables. but
We do not leave the functional paradigm, because they are all variables
immutables defined with `let`.


## 5. Function Types

In Swift functions are first-class objects and we can
assign them to variables, pass them as a parameter or return them as
result of another function. 

The following example shows all possible uses of a function
as a first-class object in Swift. Later we will see with more
detail each of the cases.

```swift
// Definimos una función simple que suma dos números
func suma(a: Int, b: Int) -> Int {
    return a + b
}

// Asignamos la función suma a una variable
let miSuma = suma

// Llamamos a la función suma usando la variable
let resultado = miSuma(3, 4)
print("La suma de 3 y 4 es: \(resultado)") 
// Salida: La suma de 3 y 4 es: 7

// Definimos una función que toma otra función como parámetro y la aplica a dos números
func aplicarOperacion(_ operacion: (Int, Int) -> Int, a: Int, b: Int) -> Int {
    return operacion(a, b)
}

let resultadoAplicarOperacion = aplicarOperacion(suma, a: 5, b: 6)
print("La suma de 5 y 6 es: \(resultadoAplicarOperacion)") 
// Salida: La suma de 5 y 6 es: 11

// Definimos una función que devuelve otra función como resultado
func obtenerOperacion() -> ((Int, Int) -> Int) {
    return suma
}

let funcionObtenida = obtenerOperacion()
let resultadoFuncionObtenida = funcionObtenida(7, 8)
print("La suma de 7 y 8 es: \(resultadoFuncionObtenida)") 
// Salida: La suma de 7 y 8 es: 15
```

As we see in the previous example, the operation of the objects
function is similar to the one we have already seen in Scheme. But with a
important difference: Swift being a strongly typed language,
we must specify the type of the parameters or type results
function.

The specific type of the function is defined by the type of its
parameters and the type of the returned value.

```swift
func sumaDosInts(a: Int, b: Int) -> Int {
    return a + b
}
func multiplicaDosInts(a: Int, b: Int) -> Int {
    return a * b
}
```

The type of these functions is `(Int, Int) -> Int`, which can be read as:

"A function type that has two parameters, both of type `Int` and that
returns a value of type `Int`".

As we have seen in the first example, we can assign these functions
to a variable of type function:

```swift
var f = sumaDosInts
print(f(2,3))
// Imprime "5"
f = multiplicaDosInts
print(f(2,3))
// Imprime "6"
```

The variable `f` is a variable of type `(Int, Int) -> Int`, that is,
a variable that contains functions with two `Int` arguments that return an
`Int`.

!!! Note "Note"
    You may have noticed that when invoking `f` no labels are placed on the
    arguments. In fact, if we put them the Swift compiler will
    complain:
    
    ```swift
    print(f(a:2, b:3))
    //error: extraneous argument labels 'a:b:' in call
    ```

    This is because `f` is a variable and can be assigned any function that has
    the type `(Int, Int) -> Int`, regardless of the argument labels.

### 5.1. Functions that receive other functions

As we saw in the initial example, we can use a function type
in parameters of other functions:

```swift
func printResultado(funcion: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Resultado: \(funcion(a, b))")
}
printResultado(funcion: sumaDosInts, 3, 5)
// Prints "Resultado: 8"
```
The `printResultado(funcion:_:_:)` function takes as its first parameter another
function that receives two `Int` values and returns an `Int`, and two `Int`
values as its second and third parameters. In the body, it calls the function
that is
passed as a parameter with the arguments `a` and `b`.

Let's look at another example, which we already saw in Scheme. Suppose we want
calculate the sum from `a` to `b` in which we apply a
`f` function to each number we add:

```text
sumatorio(a, b, f) = f(a) + f(a+1) + f(a+2) + ... + f(b)
```

We remember that it is resolved with the following recursion:

```text
sumatorio(a, b, f) = f(a) + sumatorio(a+1, b, f)
sumatorio(a, b, f) = 0 si a > b
```

Let's see how it is implemented in Swift: 

```swift
func sumatorio(desde a: Int, hasta b: Int, func f: (Int) -> Int) -> Int {
   if a > b { 
      return 0 
   } else {
      return f(a) + sumatorio(desde: a + 1, hasta: b, func: f)
   }
}

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


### 5.2. Functions in structures

Like any other type Functions can also be included in
  Composite data structures, such as arrays:
  
```swift
let funciones = [identidad, doble, cuadrado]
print(funciones[0](10)) // 10
print(funciones[1](10)) // 20 
print(funciones[2](10)) // 100
```

The type of the variable `funciones` would be `[(Int) -> Int]`. 

Since Swift is strongly typed, we could not make an array with
different types of functions. For example the following code would give a
error:

```swift
func suma(_ x: Int, _ y: Int) -> Int {
   return x + y
}
// La siguiente línea genera un error
let misFunciones = [doble, cuadrado, suma]
// error: heterogenous collection literal could only be inferred to
// '[Any]'; add explicit type annotation if this is intentional

```

### 5.3 Functions that Return Other Functions

Finally, let's look at an example of functions that return other
functions. 

It is a simple example, a function that returns another that
sum 10:

```swift
func construyeSumador10() -> (Int) -> Int {
  func suma10(x: Int) -> Int {return x+10}
  return suma10
}

let g = construyeSumador10()
print(g(20))
// Imprime 30
```

The function returned by `construyeSumador10()` is a function with type
`(Int) -> Int` (receives an integer parameter and returns an integer). In
The call to `construyeSumador10()` creates that function and assigns it to the
variable `g`.

These returned functions are called **closures**. Later we will talk more about
them. We will also see later that it is
possible to use **closure expressions** that construct closures
anonymous. 

We can modify the previous example, making the function
`construyeSumador` receive the number to add as a parameter:

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

We invoke `construyeSumador(inc:)` twice and save the
closures built in the variables `f2` and `f3`. In `f2` a
function that adds `10` to its argument and in `f3` another that adds `100`.

## 6. Types

Among the advantages of using types is the detection of errors in
compile-time programs or environment help
development to autocomplete code. Among the drawbacks are
finds the need to be stricter when defining the
parameters and the values returned by functions, which prevents
Scheme flexibility.

Types are used to define the possible values of:

- variables
- function parameters
- values returned by functions

As we have seen when we have commented that Swift is strongly
typing Type definitions are preceded by a colon in the
variables and parameters, or an arrow (`->`) in the definition of the
types of values returned by a function:

```swift
let valorDouble : Double = 3.0
let unaCadena: String = "Hola"

func calculaEstadisticas(valores: Array<Int>) -> (min: Int, max: Int, media: Int) {
   ...
}
```

In Swift there are two kinds of types: named types and compound types. 

### 6.1. Named types

A named type is a type to which we can give a certain name
when defined. For example, when defining a name of a class or
an enumeration we are also defining a name of a type.
 
In Swift it is possible to define the following named types:

- class names
- structure names
- enum names
- protocol names 

For example, instances of a user-defined class called
`MiClase` have the type `MiClase`.In addition to user-defined types, the standard library
Swift has a large number of predefined types. Unlike
other languages, these types are not part of the language itself but rather
are mostly defined as structures implemented in this
standard library. For example, arrays, dictionaries or even
More basic types like `String` or `Int` are built on that
library. The implementation of these elements is available in
opened on the GitHub site
Swift](https://github.com/apple/swift/tree/master/stdlib/public/core). 

### 6.2. Composite types

Composite types are types without names. In Swift two are defined:
tuples and function types. A composite type can have named types
and other compound types. For example the tuple `(Int, (Int, Int))`
contains two elements: the first is the type with name `Int` and the
second the composite type that defines the tuple `(Int, Int)`. The types
function we have seen previously.

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

#### 6.2.1. Typealias ####

In Swift the keyword `typealias` is defined to give it a name
assigned to any other type. Both types are equal to all
effects (it is only syntactic sugar).

For example, in the following code we define a `typealias` called
`Resultado` which corresponds to a tuple with two corresponding `Int`
to the result of a soccer match. Once defined, we can use it
like a guy The function `quiniela(partido:)` returns a `String`
corresponding to the result of the pool of a match:


```swift
typealias Resultado = (Int, Int)

func quiniela(partido: Resultado) -> String {
  switch partido {
    case let (goles1, goles2) where goles1 < goles2:
      return "Dos"
    case let (goles1, goles2) where goles1 > goles2:
      return "Uno"
    default:
      return "Equis"
  }
}

print(quiniela(partido: (1,3)))
// Imprime "Dos"
print(quiniela(partido: (2,2)))
// Imprime "Equis"
```

The example uses a statement `switch` that receives the result
of the party. This result is a tuple of two integers. In the case
let` se instancia los valores de esa tupla en las variables `goles1` and
`goles2` and then a condition is defined to enter the case. In
the first case, that `goles1` is less than `goles2` and in the second
that `goles1` is greater than `goles2`.

### 6.3. Value types and reference types

In Swift there are two types of constructions that form the basis of the
object-oriented programming: structures (_structs_) and
classes. In the next topic we will talk about it.

In the [standard library
Swift](https://developer.apple.com/documentation/swift/swift_standard_library)
most of the defined types (such as `Int`, `Double`, `Bool`,
`String`, `Array`, `Dictionary`, etc.) are structures, not classes.

One of the most important differences between structures and classes is
their behavior in an assignment: structures have a
**copy semantics** (they are value types) and classes have **copy semantics
reference** (they are reference types).

A _value type_ is a type that has copy semantics in the
assignments and when passed as a parameter in function calls.

Value types are very useful because they avoid side effects in
programs and simplify the behavior of the compiler in the
memory management. Since there are no references, it is simplified
greatly the memory management of these structures. It is not
necessary to keep track of which references point to a certain
value, but the memory can be freed as soon as the
current scope.

Compared to a value type, a reference type is one in which the
Values are assigned to variables with reference semantics. When
several assignments are made from the same instance to different
variables all of them hold a reference to the same instance. Yes
instance is modified, all variables will reflect the new
value. When we look at the classes in the next topic we will see some examples.Let's now look at some examples of copy by value in structures.

For example, if we assign one string to another, a copy is made:

```swift
var str1 = "Hola"
var str2 = str1
str1.append("Adios")
print(str1) // Imprime "HolaAdios"
print(str2) // Imprime "Hola"
```

Arrays are also structures and, therefore, they also have
copy semantics:

```swift
var array1 = [1, 2, 3, 4]
var array2 = array1
array1[0] = 10
print(array1) // [10, 2, 3, 4]
print(array2) // [1, 2, 3, 4]
```

Unlike other languages such as Java, the parameters of a
function are always immutable and are passed by copy, to reinforce the
functional nature of the functions. For example, it is incorrect
write the following:

```
func ponCero(array: [Int], pos: Int) {
    array[pos] = 0
// error: cannot assign through subscript: 'array' is a 'let' constant
}
```

You might think that it is very expensive to copy an entire array. By
For example, if we assign or pass as a parameter an array of 1000
elements. But it is not like that. The Swift compiler optimizes these
sentences and only makes the copy when there is a
modification of one of the variables that share the array. It's what
It's called _copy on write_.


## 7. Enumerations ##

Enums define a type with a restricted value of possible
values:

```swift
enum Direccion {
    case norte
    case sur
    case este
    case oeste
}
```

Any variable of type `Direccion` can only have one of the
four defined values. The value is obtained by writing the name of
the enumeration, a point and the defined value. If the type of
enumeration can be inferred, it is not necessary to write it.

```swift
let hemosGirado = true
var direccionActual = Direccion.norte
if hemosGirado {
   direccionActual = .sur
}
```

In switch statements:

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

Another example:

```swift
enum Planeta {
    case mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno
}
```

And finally, it is more correct to define the result of a pool with a
listed instead of with a `String`:

```swift
enum Quiniela {
    case uno, equis, dos
}
```

### 7.1. Raw values of enumerations ###

It is possible to assign a specific value of
an underlying type, for example integers:

```swift
enum Quiniela: Int {
    case uno=1, equis=0, dos=2
}
```

The raw value can be obtained from the type itself or from a
variable of type, using `rawValue`:

```swift
// Obtenemos el valor bruto a partir del tipo
let valorEquis: Int = Quiniela.equis.rawValue

// Obtenemos el valor bruto a partir de una variable
let res = Quiniela.equis
let valorEquis = res.rawValue
```

You can also assign the values implicitly, giving a
value to the first constant. The following have the consecutive value:

```swift
enum Planeta: Int {
    case mercurio=1, venus, tierra, marte, jupiter, saturno, urano, neptuno
}
let posicionTierra = Planeta.tierra.rawValue
// posicionTierra es 3
```


We can choose any underlying type. For example the type `Character`:

```swift
enum CaracterControlASCII: Character {
    case tab = "\t"
    case lineFeed = "\n"
    case carriageReturn = "\r"
}
```

The new line character (_lineFeed_) can be obtained as follows:

```
let nuevaLinea = CaracterControlASCII.LineFeed.rawValue
```

And finally, you can define the underlying type `String` and the
raw values of the constants will be their names converted to
chains:

```swift
enum Direccion: String {
    case norte, sur, este, oeste
}
let direccionAtardecer = Direccion.oeste.rawValue
// direccionAtardecer es "oeste"
```

In this case, you can also initialize the raw value with a
explicit assignment and not using the name itself:

```swift
enum Direccion: String {
    case norte = "north"
    case sur = "south"
    case este = "east"
    case oeste = "west"
}
let direccionAtardecer = Direccion.oeste.rawValue
// direccionAtardecer es "west"
```

When raw values are defined it is possible to initialize the enumeration
in a way similar to a structure or a class passing the value
gross. Returns the corresponding enumerated value or `nil` (a
optional):

```swift
let posiblePlaneta = Planeta(rawValue: 7)
// posiblePlaneta es de tipo Planeta? y es igual a Planeta.urano
```

## 8. Instantiable Enumerations ##

A unique feature of enums in Swift is that
allow defining variable values associated with each case of the
enumeration, creating something very similar to an instance of the
enumeration.

### 8.1. Values associated with enumeration instances ###

An instantiable enumeration allows values to be associated with the instance of the
listed. To create an instance of the enumeration we must provide
the associated value.

Like a normal enumeration, the enumeration can specify
different cases. Each case can determine an associated type of value.

In other programming languages they are called _tagged unions_ or
_variants_.

For example, we can define an enumeration that allows saving a
`Int` or a `String`:

```swift
enum Multiple {
    case num(Int)
    case str(String)
}
```

In this way, we can create values of type `Multiple` that contain
a `Int` (instantiating the case `num`) or a `String` (instantiating the
case `str`):

```swift
let valor3 = Multiple.num(10)
let valor4 = Multiple.str("Hola")
```

To obtain the associated value we must use an expression `case let`
in a statement `switch` with a variable to which the
value. For example, the following function receives instances of type
`Multiple` and prints the value associated with the enumeration that is passed as
parameter.

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

!!! Note "Note"
    Do not confuse a value associated with a case and a raw value:
    the raw value of an enumeration case is the same for all
    the instances, while the associated value is different and is
    provided when the concrete value of the enum is defined.


The case type can also be a composite type, such as a
tuple. We use an enum to define possible values of a code
bars, in which we include two possible types of barcode: the
linear barcode (referred to as UPC) and QR code:

```swift
enum CodigoBarras {
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}
```

It reads as follows: “We define an enumerated type called
`CodigoBarras`, which can take as a value a `upc` (bar code
linear) with an associated value of type `(Int, Int, Int, Int)` (a
tuple of 4 integers that represent the 4 numbers in the
linear barcodes) or a value `qrCode` with associated value of
type `String`". 

Let's see an example of use, in which we create a barcode of
UPC type product, then we modify it to another QR code type
and finally we print it:

```swift
var codigoBarrasProducto = CodigoBarras.upc(8, 85909, 51226, 3)
codigoBarrasProducto = .qrCode("ABCDEFGHIJKLMNOP")

switch codigoBarrasProducto {
case let .upc(sistemaNumeracion, fabricante, producto, control):
   print("UPC: \(sistemaNumeracion), \(fabricante), \(producto), \(control).")
case let .qrCode(codigoProducto):
   print("Código QR: \(codigoProducto).")
}
// Imprime  "Código QR : ABCDEFGHIJKLMNOP."
```

### 8.2. Recursive enumerations ###

It is possible to combine the characteristics of enumerations with value
with recursion to create recursive enumerations. must precede
the keyword `enum` with `indirect`:

```swift
indirect enum ExpresionAritmetica {
    case numero(Int)
    case suma(ExpresionAritmetica, ExpresionAritmetica)
    case multiplicacion(ExpresionAritmetica, ExpresionAritmetica)
}

let cinco = ExpresionAritmetica.numero(5)
let cuatro = ExpresionAritmetica.numero(4)
let suma = ExpresionAritmetica.suma(cinco, cuatro)
let producto = ExpresionAritmetica.multiplicacion(suma, ExpresionAritmetica.numero(2))
```

It is very convenient to handle recursive enumerations recursively:

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

Another example of recursive enums, to define a data type
`Lista` similar to the one we saw in Scheme. The list can be a list
empty or can contain two elements: a value `Int` and another list:

```swift
indirect enum Lista {
    case vacia
    case nodo(Int, Lista)
}
```

To create a list of type `nodo` we must give an integer value (the
value of the head of the list) and another list (the rest of the
list). We can also create an empty list.

For example, we can create the list `(10, 20, 30)` as follows
way:

```swift
let lista1 = Lista.nodo(30, Lista.vacia)
let lista2 = Lista.nodo(20, lista1)
let lista3 = Lista.nodo(10, lista2)
```

We could create this same list in a more abbreviated way:

```swift
let lista: Lista = .nodo(10, .nodo(20, .nodo(30, .vacia)))
```

Once the enumerated type is defined, we can define functions that
work with him. The following function, for example, is a function
recursive that receives a list and returns the sum of its
elements. It works in a very similar way to the definition that
we did in Scheme:

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

We can also define a recursive function `construye(lista:[Int])`
which returns a list from an array of integers:

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

## 9. Optionals

One of the main features that Swift tries to promote is
safety and robustness. It must be difficult for the developer
write buggy code that breaks the application. For example, static type
checking and automatic memory management are two language features that go in
this direction.

Another of the language's most important elements for promoting safety is
optionals. We are going to study their use and usefulness.

In many languages there is the concept of an _empty value_. For example, Java
uses _null_ and Python uses _None_.

!!! Note "Note"
    Tony Hoare introduced the concept of _Null_ in ALGOL in 1965. In a 2009
    talk, he discusses this idea and considers it a costly mistake: [Null References: The Billion Dollar
    Mistake](https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare). 

The concept of _null_ is dangerous, as Java developers know very well. In Java,
if we try to use a variable that contains _null_, the typical _null pointer
exception_ occurs and the application breaks. We have all fallen into this
mistake, more often than would be desirable.

Swift also has a null value. It is represented with the identifier `nil`. 

The safety feature that Swift introduces with respect to Java
and other languages is that it is not possible to assign `nil` to a variable
of a normal type.

For example, the following line would give a compilation error:

```swift
let cadena: String = nil
// error: 'nil' cannot initialize specified type 'String'
```

If we want to use `nil`, we must declare the variable using what is called an
**optional type**:

```swift
var cadena: String? = "Hola"
cadena = nil
```

The type `String?` indicates that we can have either a `nil` value or a value
of the original type. First, we define variable `cadena` with type `String?`
(optional `String`) and assign it a specific value (of type `String`). Then we
assign `nil`.

The use of optionals is necessary in situations where we can obtain an unknown
value. For example, in a function where we ask the user for a value and the
user may not enter anything, or in data structures where we perform searches
that may not return any value, as in a dictionary:

```swift
var edades = [
    "Raquel": 30,
    "Pedro": 22,
]
let edad1 = edades["Raquel"]
let edad2 = edades["Ana"] // devuelve nil
```

In the previous code we define a dictionary `edades` with keys of type
`String` and values of type `Int`. Then we look in the dictionary for
the key `"Raquel"` and the value `30` is returned, which is saved in the
variable `edad1`. When searching for the key `"Ana"`, a `nil` is returned because it is not
defined. 

Therefore, the variable `edad2` will be of type `Int?` (`Int` optional) and
will contain a `nil`.

An optional value cannot be used directly. First we must
check if the value is different from `nil` and only then we can
use it. 

To enforce this, Swift _hides_ or _wraps_ the real value of the optional and
requires calling the `!` operator to _unwrap_ it and use it. This operator is
called **forced unwrapping**.

For example, the following code produces a compile error
because we try to use an optional without unwrapping it:

```swift
var x: Int? = 10
let y = x + 10 
// error: value of optional type 'Int?' must be unwrapped to a value of type 'Int'
```

To use the value assigned to `x` we must unwrap it with the
operator `!`:

```swift
var x: Int? = 10
let y = x! + 10 
print(y)
// Imprime "20"
```

Applying the `!` operator to a `nil` value causes a runtime error and the
application breaks:

```swift
var respuestaEncuesta: String?
print(respuestaEncuesta!)
// Fatal error: Unexpectedly found nil while unwrapping an Optional value
```

We can define optional variables, parameters
or function return values of any type by adding the question mark at the end.

For example, the following function `max` is a function that returns a
`Int?`, an optional integer in case an array is passed
empty. When returning an optional, we must unwrap the returned value
when we want to use it like `Int` (for example, in the recursive call).

```swift
func max(array:[Int]) -> Int? {
    if (array.isEmpty) {
        return nil
    } else if (array.count == 1) {
        return array[0]
    } else {
        let primero = array[0]
        let resto = Array(array.dropFirst())
        return max(primero, max(array:resto)!)
    }
}

let maximo = max(array:[10,200,-100,2])
print(maximo!)
// Imprime "200"
```

An optional variable without assigning any value is initialized
automatically to `nil`:

```swift
var respuestaEncuesta: String?
// respuestaEncuesta es inicializado automáticamente a nil
```

### 9.1. Optional Binding

To check whether an optional value is `nil`, we can use an `if`. We must do so
if we do not know the value we receive. For example,
suppose that the function `leerRespuesta()` reads a response from the user and
returns a `String?`. To use this function we should
check if the returned value is different from `nil`:

```swift
let respuestaEncuesta = leerRespuesta()
if respuestaEncuesta != nil {
    let respuesta = respuestaEncuesta!
    print("Respuesta: " + respuesta)
}
```

Since the previous pattern is very common, Swift makes it possible to check
whether an optional has a value and assign that value to another variable at the
same time with a construct called _optional binding_:

```swift
let respuestaEncuesta = leerRespuesta()
if let respuesta = respuestaEncuesta {
    print ("Respuesta: " + respuesta)
}
```

We can read the previous code in the following way: "If the
optional `respuestaEncuesta` contains a value, define the constant `respuesta`
with the value contained in the optional".

An even better way to write the above code would be the following,
in which we only use one variable:

```swift
// Mejor este código que el anterior
if let respuesta = leerRespuesta() {
    print ("Respuesta: " + respuesta)
}
```

!!! Note "Note"
    To avoid having to search for a new variable name, Swift allows 
    use the same variable name in the `if let` statement:

    ```swift
    var x: Int? = 0
    if let x = x {
        print(x)
    }
    ```
    The variable `x` created by `if let` is of non-optional type and only has a value 
    in the scope of `if`.

Another example: the `first` method of an array returns an optional that
contains `nil` if the array is empty, or the first element of the array if it
exists. The following code uses optional binding to implement another version of
the function that sums the values of an array:

```swift
func sumaValores(_ valores: [Int]) -> Int {
    if let primero = valores.first {
        let resto = Array(valores.dropFirst())
        return primero + sumaValores(resto)
    } else {
        return 0
    }
}

print(sumaValores([1,2,3,4,5,6,7,8])) 
// Imprime "36"
```

If we have several optionals, it is possible to check that all of them are
different from `nil` by using several `let` bindings in the same `if`:

```swift
var x1: Int? = pedirNumUsuario()
var x2: Int? = pedirNumUsuario()
var x3: Int? = pedirNumUsuario()
if let dato1 = x1, let dato2 = x2, let dato3 = x3 {
   let suma = dato1+dato2+dato3
   print("Ningún nil y la suma de todos los datos es: \(suma)")
} else {
   print("Algún dato del usuario es nil")
}
```

### 9.2 Comparing Optionals ###

There is no need to unwrap an optional to compare it with another value using
the `==` or `!=` operators.

For example, the following code is correct:

```swift
var x: Int? = 10
x == 10 // devuelve true
x != nil // devuelve true
x == 0 // devuelve false
```

If the optional contains `nil`, it will only return `true` when compared with
`nil`:

```swift
x = nil
x == nil // devuelve true
x == 10 // devuelve false
```

### 9.3. _nil-coalescing_ operator ###

The _nil-coalescing_ operator (`??`) allows us to define a default value in an
assignment if an optional is `nil`.

```swift
let a: Int? = nil
let b: Int? = 10
let x = a ?? -1
let y = b ?? -1
print("Resultado: \(x), \(y)")
// Imprime Resultado: -1, 10
```

In the previous example, the value `-1` will be saved in the variable `x` and
in the variable `y` the value `10`.

### 9.4. Optional Chaining ###

Optional chaining allows us to call a method on a variable that contains an
optional. If the variable is not `nil`, the method is executed and its value is
returned as an optional. If the variable is `nil`, `nil` is returned.


```swift
let nombre1: String? = "Pedro"
let nombre2: String? = nil

// Error: let str1 = nombre1.lowercased()
// No podemos llamar al método lowercased() del String
// porque nombre es opcional y puede tener nil

let str1 = nombre1?.lowercased()
let str2 = nombre2?.lowercased()
// str1: String? = "pedro"
// str2: String? = nil
```


### 9.5. Definition of `Lista` with optionals

Let's see as a last example a second version of the enum `Lista`, in which
we use a single `case`, but giving the possibility that the rest
of the list is `nil` making it optional.

We define the enumeration and also the function `suma(lista:)`:

```swift
indirect enum Lista{
	case nodo(Int, Lista?)
}

func suma(lista: Lista?) -> Int {
    switch lista {
        case nil:
            return 0
        case let .nodo(first, rest):
            return first + suma(lista: rest)
    }
}

let z: Lista = .nodo(20, .nodo(10, nil))
print(suma(lista: z))
/// Devuelve 30
```


## 10. Closures

We have already seen that in Swift functions are first-class objects in the
language, and that it is possible to define functions and pass them as
parameters to other functions. 

It is also possible to build closures, functions defined in the
scope of other functions and returned as results.

We will first see how to compactly define functions that are passed
as parameters to other functions, using _closure expressions_. Later we will
see how closures defined inside other functions capture variables defined in
the scope of the main function.


### 10.1. Closure Expressions

Swift allows us to define compact expressions with which to build these
functions that are passed as parameters to other functions. They are called
_closure expressions_. These expressions provide syntax optimizations for
writing closures in a concise and clear way. Let's see the different
optimizations using the `sorted(by:)` method as an example.

### 10.2. The `sorted(by:)` method

As we have seen previously, the Swift standard library
defines a method `sorted()` that returns the sorted elements of a
[Array](https://developer.apple.com/reference/swift/array). The original array
is not modified. The comparison between the elements is carried out
using the `<` comparator.

Let's look at an example with an array of strings:

```swift
let estudiantes = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let ordenados = estudiantes.sorted()
print(ordenados)
// Imprime "["Abena", "Akosua", "Kofi", "Kweku", "Peter"]"
```

This function is similar to those in many languages. The only
functional aspect is that the original array is not modified, but the
sorting builds a new array (there is a mutable alternative
called `sort()`). 

The interesting thing related to closures is in the function
`sorted(by:)`. In this function a closure is used as a parameter
to modify the comparison between elements and result in a
different ordering. It is one of the different higher-order functions defined on collections (later we will see
others).

The signature of the function `sorted(by:)` is:

```
func sorted(by areInIncreasingOrder: (Element, Element) -> Bool)
```

The parameter is a two-parameter function (whose parameters have the type of
the array elements) that returns a Boolean indicating whether the first
parameter comes before the second in the sorted array. The sorting closure
returns `true` if the first value should appear before the second value, and
`false` otherwise.

For example, we could sort an array of strings in reverse alphabetical order. 

```swift
func primeroMayor(s1: String, s2: String) -> Bool {
    return s1 > s2
}
let estudiantes = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let alreves = estudiantes.sorted(by: primeroMayor)
print(alreves)
// Imprime ["Peter", "Kweku", "Kofi", "Akosua", "Abena"]
```

If the first string (`s1`) is greater than the second string (`s2`), the
function `primeroMayor(s1:s2:)` will return `true`, indicating that `s1`
should appear before `s2` in the sorted array. The greater-than or less-than ordering refers to alphabetical order when dealing
with characters.

The previous version is a rather complicated way of writing what is basically
a single-expression function (`a > b`). In this example, it would be preferable
to write the sorting closure _inline_, using the syntax of closure expressions.

### 10.3. Closure Expression Syntax

The syntax of closure expressions has the following general form:

```text
{ ( <parametros>) -> <tipo devuelto> in
   <sentencias>
}
```

If we apply this syntax to the previous example:

```swift
let alreves = estudiantes.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```

It should be noted that the declaration of the parameters and the type
returned by this _inline_ closure is identical to the declaration of the
function `primeroMayor(s1:s2:)`. In both cases, it is written as `(s1:
String, s2: String) -> Bool`. However, in the closure expression
the parameters and the returned type are written inside the braces, not outside them.

The beginning of the closure body is introduced by the keyword `in`. This
keyword indicates that the definition of the parameters and the type returned
by the closure is over, and that the closure body is going to begin.

Since the body of the closure is short, we can even write it in
a single line:

```swift
let alreves = estudiantes.sorted(by: { (s1: String, s2: String) -> Bool in return s1 > s2 } )
```

### 10.4. Type Inference from Context

Since the sort closure is passed as an argument to a method,
Swift can infer the types of its parameters and the type of the value it
returns. The `sorted(by:)` method is called on an array of strings,
so its argument must be a function of type `(String,
String) -> Bool`. This means that the types `(String, String)` and
`Bool` do not need to be written as part of the definition of the
closure expression. Because all types can be
inferred, the arrow of the returned type and the parentheses around
parameter names can also be omitted:

```swift
let alreves = estudiantes.sorted(by: { s1, s2 in return s1 > s2 } )
```

### 10.5. Implicit returns in closures with a single expression

In closures with a single expression we can also omit the keyword `return`:

```swift
let alreves = estudiantes.sorted(by: { s1, s2 in s1 > s2 } )
```

### 10.6. Abbreviations in argument names

Swift automatically provides abbreviations for names.
arguments of _inline_ closures that can be used to refer
to the values of the closure arguments using the names
`$0`, `$1`, `$2`, etc.

If you use these shorthand arguments, you can skip the definition
from the list of arguments:

```swift
let alreves = estudiantes.sorted(by: { $0 > $1 } )
```

### 10.7. Operator functions

There is even an even shorter way to write the expression
previous closure.  Swift defines a specific implementation of
greater-than operator strings (`>`) as a function that has two
parameters of type `String` and returns a `Bool`. This is exactly
what the `sorted(by:)` method needs. We can, therefore, pass
just this greater-than operator, and Swift will infer that we want
use the specific strings:

```swift
let alreves = estudiantes.sorted(by: >)
```

### 10.8. Trailing Closures

If we need to pass a closure expression as an argument to a function and the
expression is long, it can be useful to write it instead as a trailing closure (_trailing
closure_). A trailing closure is a closure expression that is written outside (and after)
the parentheses of the function to which it is passed as a parameter:

```swift
let alreves = estudiantes.sorted() { $0 > $1 }
```

When a closure expression is provided as the sole argument of a function or
method and is passed as a trailing closure, it is not necessary to write the
parentheses after the function name:

```swift
let alreves = estudiantes.sorted { $0 > $1 }
```


### 10.9. Captured variables

!!! Danger "Beware"
    The examples we are going to see below do not use functional programming,
    because the variable captured by the closure is a **mutable** variable
    (defined with `var`, not with `let`). Therefore, the resulting functions are
    not pure functions; they return a different value each time they are
    invoked. They are functions with mutable local state.

A closure can capture constants and variables from the context in which it is
defined. The closure can refer to and modify those values inside its body, even
if the original scope in which those constants and variables were defined no
longer exists.

In Swift, the simplest form of a closure that captures variables is
a nested function (_nested function_) written in the body of another
function. A nested function can capture any of the
arguments of its outer function, and it can also capture any constant or
variable defined inside the outer function. Let's look at an example similar to the one we saw in Scheme. The function
`construyeIncrementador` contains a nested function called
`incrementador`. This function captures two variables from its context:
`totalAcumulado` and `cantidad`. After capturing these variables,
`incrementador` is returned by `construyeIncrementador` as a
closure that increments `totalAcumulado` by `cantidad` each time
call.

```swift
func construyeIncrementador(incremento cantidad: Int) -> () -> Int {
    var totalAcumulado = 0
    func incrementador() -> Int {
        totalAcumulado += cantidad
        return totalAcumulado
    }
    return incrementador
}
```

The return type of `construyeIncrementador` is `() -> Int`. This
means that it returns a function that has no parameters and that
returns a `Int` every time it is called.

The function `construyeIncrementador(incremento:)` has a single
parameter `Int` with external name `incremento` and local name
`cantidad`. The argument passed to this parameter specifies how much
will be incremented `totalAcumulado` every time the function is called
`incrementador` returned. The function `construyeIncrementador` defines
a nested function called `incrementador`, which performs the increment
real. This function simply adds `cantidad` to `totalAcumulado`, and
returns the result.

If we consider it in isolation, the nested function `incrementador()`
might seem strange:

```swift
func incrementador() -> Int {
    totalAcumulado += cantidad
    return totalAcumulado
}
```

The function has no parameters, and yet refers to
`totalAcumulado` and `cantidad` on his body. You can do it because you have
captured a reference to these variables from the surrounding function
and uses them on his own body. By capturing these references the
variables `totalAcumulado` and `cantidad` do not disappear when finished
the call to `construyeIncrementador`. These variables will also be
available the next time the `incrementador` function is called.

Here's an example of `construyeIncrementador` in action:

```swift
let incrementaDiez = construyeIncrementador(incremento: 10)
```

This example defines a constant called `incrementaDiez` to
reference the function `incrementador` that returns
`construyeIncrementador`. This function adds 10 to the variable
`totalAcumulado` every time you are called. If we call the function
More than once we can see his behavior in action:

```swift
incrementaDiez()
// devuelve 10
incrementaDiez()
// devuelve 20
incrementaDiez()
// devuelve 30
```

If we create a second incrementer, it will have its own references to
a new variable `totalAcumulado`, different from the previous one:

```swift
let incrementaSiete = construyeIncrementador(incremento: 7)
incrementaSiete()
// devuelve 7
```

If we call the original `incrementador` function (`incrementaDiez`)
we see that it continues to increase its own variable `totalAcumulado` and
which is not affected by the variable captured by `incrementaSiete`:

```swift
incrementaDiez()
// devuelve 40
```


### 10.10. Closures with Closure Expressions ###

In the previous example we have used an internal definition of a
function to define the closure that is returned. We have done it for
clarity, but it is not necessary. It is possible to write more compact code using closure expressions.

For example, the function `construyeSumador()` seen in the section
"Functions that return other functions":

```swift
func construyeSumador10() -> (Int) -> Int {
  func suma10(x: Int) -> Int {return x+10}
  return suma10
}
```

A version of this same function using a closure expression is
the following:

```swift
func construyeSumador10() -> (Int) -> Int {
    return {$0 + 10}
}

let f = construyeSumador10()
print(f(20))
// Imprime "30"
```

And the same with the function `construyeIncrementador(incremento:)` seen in
the previous section:

```swift
func construyeIncrementador(incremento cantidad: Int) -> () -> Int {
    var totalAcumulado = 0
    func incrementador() -> Int {
        totalAcumulado += cantidad
        return totalAcumulado
    }
    return incrementador
}
```

The version with a closure expression:

```swift
func construyeIncrementador(incremento cantidad: Int) -> () -> Int {
    var totalAcumulado = 0
    return {totalAcumulado += cantidad
            return totalAcumulado}
}

let incrementaDiez = construyeIncrementador(incremento: 10)
print(incrementaDiez())
// Imprime "10"
print(incrementaDiez())
// Imprime "20"
```


### 10.11. Variables captured by closures and invocation scope variables ###

Closures use captured variables, not variables declared in the scope where the
closure is invoked. Let's explain it with an example.

```swift linenums="1" hl_lines="2 14 20"
func construyeFunc() -> () -> Int {
   var x = 0
   return {
      x = x + 1
      return x
   }
}

let f = construyeFunc()
print(f()) // -> 1
print(f()) // -> 2

func usaFunc(_ f: () -> Int) -> Int {
     var x = 10
     return f()
}

print(usaFunc(f)) // -> 3

var x = 100
print(usaFunc {return x + 10}) // -> 110
```

The three variable declarations are highlighted in the code above.
`x`. It is very important to check the area in which these are carried out.
statements. The first declaration is made inside the function
`construyeFunc()`, the second one inside the function `usaFunc()` and the
third in the global scope. In each case, the variable will be initialized
when that line of code is executed.The function `usaFunc` defined on line 13 receives a function `f`
no parameters that returns an integer. At the local level of `usaFunc`
the local variable `x` is defined to have the value `10` before
invoke the received `f` function.

What if the received function is a closure that has captured a
variable that is also called `x`? In the case of the invocation of
`usaFunc` that is on line 18, the function `f` that is passed as
parameter is the closure obtained in line 9. This closure has
captured the variable `x` defined on line 2. And at that moment
that variable has the value 2. The closure code is the one defined
on lines 3 to 6:

```swift
{
x = x + 1
return x
}
```

Which variable `x` does that code refer to? The captured variable, which has
the value 2? Or the variable in the execution scope (line 14), which has the
value 10?

If we execute the code we will see that the expression returns 3. That is,
closures always use the captured variables.

We can also check this in the invocation on line 21. There, the closure that
is passed is a closure expression that captures the variable `x` defined on the
previous line. That is why, when the statement runs, it prints the value `110`
and not the value `20`.


### 10.12. Closures are reference types

In the example above, `incrementaSiete` and `incrementaDiez` are
constants, but the closures to which these constants refer
can increase the variable `totalAcumulado` that they have
captured. This is because functions and closures are reference types.

Whenever we assign a function or a closure to a constant or a
variable, we are actually establishing that the constant or variable
It is a reference to function or closure. In the previous example,
is the choice of closure to which `incrementaDiez` refers
which is constant, not the contents of the closure.

This also means that if we assign a closure to two constants
or different variables, both constants or variables will refer to the
same closure:

```swift
let tambienIncrementaDiez = incrementaDiez
tambienIncrementaDiez()
// devuelve 50
```


## 11. Higher-order functions

One of the functional features that we have used the most when working with
lists in Scheme are higher-order functions such as
`map`, `filter` or `foldl`. Swift has defined equivalent functions
for working with collections. They are called `map`,
`filter` and `reduce`. All of them accept closure expressions as arguments.

### 11.1. Map

The `map` method is defined in the protocol
[`CollectionType`](https://developer.apple.com/library/ios/documentation/Swift/Reference/Swift_CollectionType_Protocol/index.html#//apple_ref/swift/intfm/CollectionType/s:FEsPs14CollectionType3mapurFzFzWx9Generator7Element_qd__GSaqd___)
and is adopted by multiple structures such as `Array`, `Dictionary`,
`Set`.

The signature of the `map` method is as follows:

```swift
func map<T>(_ transform: (Element) -> T) -> [T]
```

This is a generic method (we will see it later) that receives
as parameter a unary function (transformation function) 
of the type of the elements of the collection and that returns another element
(it may be of the same or different type as the elements of the
collection). Returns an array containing the result of applying
the transformation function to each element of the original array.

For example:

```swift
let numeros = [Int](0...5)
numeros.map {$0 * $0}
// devuelve [0, 1, 4, 9, 16, 25]
```

Another example, where we use `map` to implement the function
`sumaParejas(parejas: [(Int, Int)]) -> [Int]` that returns receives the
array `parejas` of two-integer tuples and returns an array with the
result of adding the two elements of each pair:

```swift
func suma(parejas: [(Int, Int)]) -> [Int] {
   return parejas.map({(pareja: (Int, Int)) -> Int in
                        return pareja.0 + pareja.1})
}
suma(parejas:[(1, 1), (2, 2), (3, 3), (4, 4)])
// devuelve [2, 4, 6, 8]
```
We can use in the body of the closure expression of `map` a
captured variable. For example in the following function
`incrementaValores(_:con:)` which adds `con` to all the numbers in a
array that is passed as a parameter:

```swift
func incrementa(valores: [Int], con: Int) -> [Int] {
   return valores.map({(x: Int) -> Int in
                        return x + con})
}
incrementa(valores:[10, 20, 30], con: 5)
// devuelve [15, 25, 35]
```
The abbreviated version of the closure expression is:

```swift
func incrementa(valores: [Int], con inc: Int) -> [Int] {
   return valores.map {$0 + inc}
}
incrementa(valores: [10, 20, 30], con: 5)
// devuelve [15, 25, 35]
```


### 11.2. Filter


The `filter` function is also the same as the one defined in Scheme. Its
signature is:

```swift
func filter(_ isIncluded: (Element) -> Bool) -> [Element]
```

It receives a one-argument closure that returns
a boolean. The function returns an array with the elements of the
collection for which the closure returns _true_. 

Example:

```swift
let numeros = [Int](0...10)
numeros.filter {$0 % 2 == 0}
// devuelve [0, 2, 4, 6, 8, 10]
```


### 11.3. Reduce 

Similar to Scheme's _foldl_. His signature is the following:


```swift
func reduce<Result>(_ initialResult: Result, 
                    _ nextPartialResult: (Result, Element) -> Result) -> Result
```

It is a generic function that returns a value of a generic type (the
type of the result that is constructed in the function). Receive as
parameter an initial value and a _folding function_ that is applied to the
previous result and to the collection element, returning a
result. The final result is the result of applying the function
folded to all elements in the collection, starting with the value
initial.

For example, we can use `reduce` to add all the numbers in an array:


```swift
let numeros = [Int](0...10)
numeros.reduce(0, +)
```

The function combines the elements of the collection using the function
combination passed as a parameter. The function passed as
parameter receives two parameters: the first is the result of the
combination and the second is taken from the collection. 

For example, the following code uses `reduce` to add the length
of all the strings in an array:

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]
cadenas.reduce(0, {(i: Int, c: String) -> Int in
                      c.count + i })
// devuelve 18
```

It is possible to simplify the previous notation:

```swift
cadenas.reduce(0, {$1.count + $0})
```

You can also use trailing-closure notation:

```swift
cadenas.reduce(0) {$1.count + $0}
```

The combination is done from left to right:

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]
print(cadenas.reduce("*", {$0 + "-" + $1}))
// Imprime "*-Patatas-Arroz-Huevos"
```

The first argument of the fold function (`$0`) is the result
above (starts with `"*"`) and the second argument (`$1`) is taken from
array of strings.


### 11.4. Combination of higher-order functions

When the result of applying a higher-order function to a
collection is another collection it is possible to apply another function
higher-order than this result.

For example, the following statement returns all even numbers
of the initial array squared:


```swift
let numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.filter{$0 % 2 == 0}.map{$0*$0}
// Devuelve el array [4,16,36,64,100]
```

And the following returns the sum of numbers greater than 100:

```swift
let numeros = [103, 2, 330, 42, 532, 6, 125]
numeros.filter{$0 >= 100}.reduce(0,+)
// Devuelve 1090
```


## 12. Generics


Let's start with a simple example. Let us assume the following function
`intercambia(_:)` which receives a tuple `(Int, String)` and returns a
tuple `(String, Int)` with the exchanged values.

```swift
func intercambia(_ tupla: (Int, String)) -> (String, Int) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}

let tupla = (10, "Hola")
intercambia(tupla)
// devuelve ("Hola", 10)
```

The function is interesting, but it only receives tuples whose first
component is a `Int` and its second component is a
`String`. Suppose we want to do the same function for
exchange elements of a tuple `(Int, Int)`. we would have to use
the same code, but changing the types:

```swift
func intercambia(_ tupla: (Int, Int)) -> (Int, Int) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}

let tupla = (10, 20)
intercambia(tupla)
// devuelve (20, 10)
```

The code is the same, the only thing different is the types. Could we
**generalize** the above functions to make the code
Can it work with any type? The answer is yes, using
**generic function**:

```swift
func intercambia<A,B>(_ tupla: (A, B)) -> (B, A) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}
```
The body of the function is identical to the previous function. The
The difference is that in the generic version *placeholder types* are used (the
symbols `A` and `B`) instead of concrete types. They are generic types,
which are defined using an identifier between symbols of `<` and
`>`. The actual types to be used in the function are determined in
each invocation to the function, depending on the type of the parameter that
is used in the call:

```swift
let tupla = (10, "Hola")
intercambia(tupla)
// devuelve ("Hola", 10)
let tupla2 = (10, 20)
intercambia(tupla2)
// devuelve (20, 10)
let tupla3 = (true, 10.5)
intercambia(tupla3)
// devuelve (10.5, true)
```

In the first example, the types `A` and `B` are inferred as `Int` and
`String`. In the second example as `Int` and `Int`. And in the third
such as `Bool` and `Double`.

Generic types can be used in the definition of all
Swift elements: functions, enums, structures, classes, protocols
or extensions. We finish with an example in which we include many
concepts seen in this topic. This is the implementation in Swift
Scheme-style lists, with the functions `first`, `resty `empty`
using a recursive enum with a generic type that allows generalization
the type of list items.

```swift
indirect enum Lista<T> {
     case vacia
     case nodo(T, Lista<T>)
}

func first<T>(_ lista: Lista<T>) -> T? {
   switch lista {
      case let .nodo(primero, _):
         return primero
      case .vacia:
         return nil
   }
}

func rest<T>(_ lista: Lista<T>) -> Lista<T>? {
   switch lista {
      case let .nodo(_, resto):
         return resto
      case .vacia:
         return nil
   }
}

func vacia<T>(_ lista: Lista<T>) -> Bool {
   switch lista {
      case .vacia:
         return true
      default:
         return false
   }
}

let lista : Lista = .nodo(20, .nodo(30, .nodo(40, .vacia)))
let lista2 : Lista = .nodo("A", .nodo("B", .nodo("C", .vacia)))

print(first(rest(lista)!)!) // Imprime 30
print(first(rest(lista2)!)!) // Imprime "B"

```

## 13. Bibliography

- Swift Language Guide
    - [The Basics](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID309)
    - [Collection Types](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/CollectionTypes.html#//apple_ref/doc/uid/TP40014097-CH8-ID105)
    - [Functions](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Functions.html#//apple_ref/doc/uid/TP40014097-CH10-ID158)
    - [Closures](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID94)
    - [Enumerations](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Enumerations.html#//apple_ref/doc/uid/TP40014097-CH12-ID145)
    - [Generics](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Generics.html#//apple_ref/doc/uid/TP40014097-CH26-ID179)
- [Swift Standard Library](https://developer.apple.com/library/ios/documentation/General/Reference/SwiftStandardLibraryReference/)


----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
