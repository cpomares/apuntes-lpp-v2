# Lab 10: Functional Programming in Swift (2)

## Before the Lab Session

The following exercises are based on the theory concepts covered last week.
Before the lab session, you should review all the concepts and **try with the
Swift compiler** all the examples from the following sections of topic 5
[_Functional Programming with
Swift_](../../theory/topic05-functional-programming-swift/topic05-functional-programming-swift.md#9-optionals)

- Optionals
- Closures
- Higher-order functions
- Generics

## Exercises

### Exercise 1 ###

a) Define the function `maxOpt(_ x: Int?, _ y: Int?) -> Int?`, which returns the
maximum of two optional integers. If both are `nil`, it returns `nil`. If one is
`nil` and the other is not, it returns the integer that is not `nil`. If neither
parameter is `nil`, it returns the larger one.

Example:

```swift
let res1 = maxOpt(nil, nil) 
let res2 = maxOpt(10, nil)
let res3 = maxOpt(-10, 30)
print("res1 = \(String(describing: res1))")
print("res2 = \(String(describing: res2))")
print("res3 = \(String(describing: res3))")
// Imprime:
// res1 = nil
// res2 = Optional(10)
// res3 = Optional(30)

```

b1) Write a new version of exercise 2b) from lab 9 that allows negative numbers
and returns a pair `(Int?, Int?)` with `nil` in the left and/or right part if
there are no odd or even numbers. You must use the helper function defined in the
previous part.

Example:

```swift
let numeros = [-10, 202, 12, 100, 204, 2]
print("\n******\n1b1) Función parejaMayorParImpar2(numeros:)\n******")
print(parejaMayorParImpar2(numeros: numeros))
// Imprime:
// parejaMayorParImpar2(numeros: [-10, 202, 12, 100, 204, 2])
// (nil, Optional(204))
```

b2) Write the function `sumaMaxParesImpares(numeros: [Int]) -> Int`, which
**calls the previous function** and returns the sum of the maximum even number
and the maximum odd number. If an empty array is passed, it must return 0.

```swift
print("sumaMaxParesImpares(numeros: \(numeros))")
print(sumaMaxParesImpares(numeros: numeros))
// Imprime:
// sumaMaxParesImpares(numeros: [-10, 202, 12, 100, 204, 2])
// 204
```

b3) Write a new version of the function from exercise b1) that returns `nil` when
an empty array is passed as a parameter. How should the function declaration be
changed? Also write a new version of the function from exercise b2) that calls
the previous function.

### Exercise 2 ###

a) Indicate what the following expressions return:

a.1)
```swift
let nums = [1,2,3,4,5,6,7,8,9,10]
nums.filter{$0 % 3 == 0}.count
```

a.2)
```swift
let nums2 = [1,2,3,4,5,6,7,8,9,10]
nums2.map{$0+100}.filter{$0 % 5 == 0}.reduce(0,+)
```

a.3)
```swift
let cadenas = ["En", "un", "lugar", "de", "La", "Mancha"]
cadenas.sorted{$0.count < $1.count}.map{$0.count}
```


a.4)
```swift
let cadenas2 = ["En", "un", "lugar", "de", "La", "Mancha"]
cadenas2.reduce([]) {
    (res: [(String, Int)], c: String) -> [(String, Int)] in
        res + [(c, c.count)]}.sorted(by: {$0.1 < $1.1})
```


b) Explain what the following functions do and provide an example of how they
work:

b.1)
```swift
func f(nums: [Int], n: Int) -> Int {
    return nums.filter{$0 == n}.count
}
```


b.2)
```swift
func g(nums: [Int]) -> [Int] {
    return nums.reduce([], {
        (res: [Int], n: Int) -> [Int] in
            if !res.contains(n) {
                return res + [n]
            } else {
                return res
            }
    })
}
```


b.3)
```swift
func h(nums: [Int], n: Int) -> ([Int], [Int]) {
   return nums.reduce(([],[]), {
       (res: ([Int],[Int]), num: Int ) -> ([Int],[Int]) in
           if (num >= n) {
               return (res.0, res.1 + [num])
           } else {
               return ((res.0 + [num], res.1))
           }
   })
}
```

c) Implement the following functions with higher-order functions.

c.1) Function `suma(palabras:contienen:)`:

```swift
suma(palabras: [String], contienen: Character) -> Int
```

which receives an array of strings and returns the sum of the lengths of the
strings that contain the character passed as a parameter.


c.2) Function `sumaMenoresMayores(nums:pivote:)`:

```swift
sumaMenoresMayores(nums: [Int], pivote: Int) -> (Int, Int)
```

which receives an array of numbers and a pivot number, and returns a tuple with
the sum of the numbers smaller than the pivot and greater than or equal to the
pivot.


d) (Exercise on variables captured by closures) Reflect on the following code and
fill in the blank to obtain the expected result.

```swift
func bar(f: (Int) -> Int) {
  print(f(__________))
}

func foo() -> (Int) -> Int {
  var x = 3
  return {
    x += $0 + 2
    return x
  }
}

var x = 5
let g = foo()
bar(f: g)   // => 9
bar(f: g)   // => 15
```

### Exercise 3


Define an enum type with a generic tree, as we did in the last exercise of the
previous lab, whose contained data type is generic.

The following example shows how it should be possible to define a tree of
integers and a tree of strings with the same generic type:

```swift
let arbolInt: Arbol = .nodo(53, 
                            [.nodo(13, []), 
                             .nodo(32, []), 
                             .nodo(41, 
                                   [.nodo(36, []), 
                                    .nodo(39, [])
                                   ])
                            ])
let arbolString: Arbol = .nodo("Zamora", 
                               [.nodo("Buendía", 
                                      [.nodo("Albeza", []), 
                                       .nodo("Berenguer", []), 
                                       .nodo("Bolardo", [])
                                      ]), 
                                .nodo("Galván", [])
                               ])
```


Define the generic functions `toArray` and `toArrayFOS`, which return an array
with all the components of the tree using a _preorder_ traversal (first the root
and then the children). The first must be implemented with mutual recursion, and
the second using higher-order functions.

Example:

```swift
print(toArray(arbol: arbolInt))
// Imprime: [53, 13, 32, 41, 36, 39]
print(toArrayFOS(arbol: arbolString))
// Imprime: ["Zamora", "Buendía", "Albeza", "Berenguer", "Bolardo", "Galván"]
```


### Exercise 4

Implement in Swift the function `imprimirListadosNotas(alumnos:)`, which receives
an array of tuples, where each tuple contains information about the assessment of
an LPP student (studentName, examGrade1, examGrade2, examGrade3,
yearsOfEnrollment), and must print the following reports on screen:

- report 1: array sorted by student name (in increasing alphabetical order)
- report 2: array sorted by grade in exam 1 (in decreasing grade order)
- report 3: array sorted by grade in exam 2 (in increasing grade order)
- report 4: array sorted by enrollment year and grade in exam 3 (in decreasing
  year and grade order)
- report 5: array sorted by final grade (average of the three exams, weighted as:
  0.35, 0.3, 0.35) (in decreasing final-grade order)

The sorting must be done using the `sorted` function.

!!! Note "Note"
    To display the reports formatted with spaces, you can use the following
    function (you must also include the indicated import):

    ```swift

    import Foundation

    func imprimirListadoAlumnos(_ alumnos: [(String, Double, Double, Double, Int)]) {
        print("Alumno   Parcial1   Parcial2   Parcial3  Años")
        for alu in alumnos {
            alu.0.withCString {
                print(String(format:"%-10s %5.2f      %5.2f    %5.2f  %3d", $0, alu.1,alu.2,alu.3,alu.4))
            }
        }
    }
    ```


Example:

```swift
let listaAlumnos = [("Pepe", 8.45, 3.75, 6.05, 1), 
                    ("Maria", 9.1, 7.5, 8.18, 1), 
                    ("Jose", 8.0, 6.65, 7.96, 1),
                    ("Carmen", 6.25, 1.2, 5.41, 2), 
                    ("Felipe", 5.65, 0.25, 3.16, 3), 
                    ("Carla", 6.25, 1.25, 4.23, 2), 
                    ("Luis", 6.75, 0.25, 4.63, 2), 
                    ("Loli", 3.0, 1.25, 2.19, 3)]
imprimirListadosNotas(listaAlumnos)
```

Some of the reports that should be displayed are the following:

```txt
LISTADO ORIGINAL
Alumno   Parcial1   Parcial2   Parcial3  Años
Pepe        8.45       3.75     6.05    1
Maria       9.10       7.50     8.18    1
Jose        8.00       6.65     7.96    1
Carmen      6.25       1.20     5.41    2
Felipe      5.65       0.25     3.16    3
Carla       6.25       1.25     4.23    2
Luis        6.75       0.25     4.63    2
Loli        3.00       1.25     2.19    3

LISTADO ORDENADO por Parcial1 (decreciente)
Alumno   Parcial1   Parcial2   Parcial3  Años
Loli        3.00       1.25     2.19    3
Felipe      5.65       0.25     3.16    3
Carmen      6.25       1.20     5.41    2
Carla       6.25       1.25     4.23    2
Luis        6.75       0.25     4.63    2
Jose        8.00       6.65     7.96    1
Pepe        8.45       3.75     6.05    1
Maria       9.10       7.50     8.18    1
```


### Exercise 5

Given the array `listaAlumnos` from the previous exercise, use higher-order
functions to obtain the data requested in each case.

A) Number of students who passed the first exam and failed the second

```swift
print(listaAlumnos. ________________________________ )
// Resultado: 5
```

B) Students who passed the course (they have a final grade >= 5)

```swift
print(listaAlumnos._______________________________ )

// Resultado: ["Pepe", "Maria", "Jose"]
```

C) Average grade of all students as a tuple `(media_p1, media_p2, media_p3)`

```swift
var tupla = listaAlumnos._____________________________________ )
tupla = (tupla.0 / Double(listaAlumnos.count), tupla.1 / Double(listaAlumnos.count), tupla.2 / Double(listaAlumnos.count))
print(tupla)
// Resultado: (6.6812499999999995, 2.7624999999999997, 5.22625)
```

### Exercise 6 ###


Implement the function `construye` with the following type:

```swift
func construye(operador: Character) -> (Int, Int) -> Int
```

The function receives an operator that can be one of the following characters:
`+`, `-`, `*`, `/`, and must return a closure that receives two arguments and
performs the indicated operation on them.

Example:

```swift
var f = construye(operador: "+")
print(f(2,3))
// Imprime 5
f = construye(operador: "-")
print(f(2,3))
// Imprime -1
```

----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
