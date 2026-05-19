# Lab 9: Swift Seminar and Functional Programming in Swift (1)

## Exercises

### Exercise 1 ###

Start by reading and trying the [Swift
seminar](../../seminars/seminar02-swift/seminar02-swift.md), up to and including
the _Functions and closures_ section.

1. To install the `swift` command on your computer, follow the instructions in
   the seminar.

2. As indicated in the seminar, you can also run Swift programs using an online
   environment, for example:
   [Swift MyCompiler](https://www.mycompiler.io/es/new/swift).
   But you should keep in mind that this option has some problems: an Internet
   connection is required, the editor is very limited, and the server may be down
   occasionally.

3. Create the file `lab09.swift` with a _Hello world_ instruction that prints
   that string. Run it in the environment you have installed and check that
   everything works correctly:

    ```
    $ swift practica09.swift
    Hola, mundo
    ```
4. Read the seminar, copying and modifying (whenever possible) the code from the
    examples in the `lab09.swift` file. Read the corresponding section carefully
    before trying each example. It is useful to **copy the code without
    copy-pasting**, so that you get used to the syntax of the new language.

    Include in the lab all the indicated experiments, up to `Experiment 9`. Before
    each experiment, add a comment indicating the experiment.


### Exercise 2 ###

a) Implement in Swift the recursive function `prefijos(prefijo:palabras:)`, which
receives a string and an array of words. It returns an array of `Bool` with the
Boolean values resulting from checking whether the string is a prefix of each
word in the list.

You can use the `hasPrefix()` method of `String` to check whether one string is a
prefix of another:

```swift
let miCadena = "Hola"
miCadena.hasPrefix("Ho") // Devuelve true
miCadena.hasPrefix("la") // Devuelve false
```

Example:

```swift
let array = ["anterior", "antígona", "antena"]
let prefijo = "ante"
print("\n******\n2a) Función prefijos(prefijo:palabras:)\n******")
print(prefijos(prefijo: prefijo, palabras: array))
// Imprime: [true, false, true]
```

b) Implement in Swift the recursive function `parejaMayorParImpar(numeros:)`,
which receives an array of positive integers and returns a pair with two
integers: the first is the largest odd number and the second is the largest even
number. If there is no even or odd number, 0 is returned.

```swift
let numeros = [10, 201, 12, 103, 204, 2]
print("\n******\n2b) Función parejaMayorParImpar(numeros:)\n******")
print(parejaMayorParImpar(numeros: numeros))
// Imprime: (201, 204)
```

### Exercise 3 ###

a) Implement in Swift the **recursive function**
`compruebaParejas(_:funcion:)` with the following type:

```
([Int], (Int) -> Int) -> [(Int, Int)]
```

The function receives two parameters: an `Array` of integers and a function that
receives an integer and returns an integer. The function will return an array of
tuples containing the tuples formed by those contiguous numbers in the first
array that satisfy that the number is the result of applying the function to the
number located in the previous position.

Example:

```swift
func cuadrado(x: Int) -> Int {
   return x * x
}
print(compruebaParejas([2, 4, 16, 5, 10, 100, 105], funcion: cuadrado))
// Imprime [(2,4), (4,16), (10,100)]
```

b) Implement in Swift the **recursive function**
`coinciden(parejas: [(Int,Int)], funcion: (Int)->Int)`, which returns an array of
Booleans indicating whether the result of applying the function to the first
number of each pair matches the second.


```swift
let array = [(2,4), (4,14), (4,16), (5,25), (10,100)]
print(coinciden(parejas: array, funcion: cuadrado))
// Imprime: [true, false, true, true, true]
```


### Exercise 4 ###

Suppose we are writing a program that has to process bank-account movements.
Define an enum `Movimiento ` with associated values that lets us represent:

- Deposit (associated value: `(Double)`)
- Bill charge (associated value: `(String, Double)`)
- ATM withdrawal (associated value: `(Double)`)

And define the function `aplica(movimientos:[Movimiento])`, which receives an
array of movements and returns a pair with the resulting money after accumulating
all the movements and an array of Strings with all the charges made.

Example:


```swift
let movimientos: [Movimiento] = [.deposito(830.0), .cargoRecibo("Gimnasio", 45.0), .deposito(400.0), .cajero(100.0), .cargoRecibo("Fnac", 38.70)]
print(aplica(movimientos: movimientos))
//Imprime (1046.3, ["Gimnasio", "Fnac"])
```


### Exercise 5 ###

Implement in Swift a recursive enum type that lets us build binary trees of
integers. The enum must have

- one case storing three values: an `Int` and two binary trees (the left child and
  the right child)
- another constant case: an empty binary tree

We will call the type `ArbolBinario` and the cases `nodo` and `vacio`.

Implement it so that the following example works correctly:

```swift
let arbol: ArbolBinario = .nodo(8, 
                                .nodo(2, .vacio, .vacio), 
                                .nodo(12, .vacio, .vacio))
```

Also implement the function `suma(arbolb:)`, which receives an instance of a
binary tree and returns the sum of all its nodes:

```swift
print(suma(arbolb: arbol))
// Imprime: 22
```


### Exercise 6 ###

Implement in Swift a recursive enum type that lets us build trees of integers
using the same approach as in Scheme: a node is formed by a datum (an `Int`) and
a collection of child trees. We will call the type `Arbol`.

Implement it so that the following example works correctly:

```swift

/*
Definimos el árbol

    10
   / | \
  3  5  8
  |
  1

*/

let arbol1 = Arbol.nodo(1, [])
let arbol3 = Arbol.nodo(3, [arbol1])
let arbol5 = Arbol.nodo(5, [])
let arbol8 = Arbol.nodo(8, [])
let arbol10 = Arbol.nodo(10, [arbol3, arbol5, arbol8])
```

Also implement the function `suma(arbol:cumplen:)`, which receives an instance
of a tree and a function `(Int) -> Bool` that checks a condition on the node. The
function must return the sum of all the nodes in the tree that satisfy the
condition.

Implement the function using the same strategy we already used in Scheme:
defining a helper function `suma(bosque:cumplen:)` and mutual recursion.

```swift
func esPar(x: Int) -> Bool {
    return x % 2 == 0
}

print("La suma del árbol es: \(suma(arbol: arbol10, cumplen: esPar))")
// Imprime: La suma del árbol genérico es: 18
```

----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
