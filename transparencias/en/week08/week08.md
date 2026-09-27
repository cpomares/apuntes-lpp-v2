---
marp: true
theme: lpp
size: 16:9
paginate: true
footer: "Cristina Pomares Puig · LPP"
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="eyebrow">Programming Languages and Paradigms</div>
<div class="week-marker">Week 8</div>

# Functional programming with Swift I

<p class="lead">Topic 5 · From immutable values to recursive enumerations</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Translate the functional ideas already studied in Scheme into Swift.
Say: "Swift is primarily imperative, but it includes immutability, first-class functions, closures, and recursive data types."
Bridge: "We will follow those ideas from values and functions to recursive enumerations."
-->

---

<div class="eyebrow">Today</div>

## Eight sections from the class notes

<div class="sequence week08-roadmap-eight">
  <div><b>1</b><span>Introduction</span></div>
  <div><b>2</b><span>Immutability</span></div>
  <div><b>3</b><span>Functions</span></div>
  <div><b>4</b><span>Recursion</span></div>
  <div><b>5</b><span>Function types</span></div>
  <div><b>6</b><span>Types</span></div>
  <div><b>7</b><span>Enumerations</span></div>
  <div><b>8</b><span>Associated and recursive values</span></div>
</div>

<!--
Idea: Reproduce the eight sections from the class notes.
Say: "The language changes, but the functional questions stay familiar: what changes, what is returned, and how recursive data is decomposed."
Bridge: "First, we locate Swift among the paradigms we already know."
-->

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Introduction

<p class="lead">Swift combines imperative programming with functional and object-oriented features.</p>

<!--
Idea: Use the classification from the notes without presenting Swift as a purely functional language.
Say: "Swift is multi-paradigm. In this topic we deliberately focus on the features that support functional programming."
Bridge: "Its static type system is visible from the first declaration."
-->

---

<div class="eyebrow">Strong static typing</div>

## Every value has a type

<div class="columns equal">
<div>

```swift
let n: Int = 10
let str: String = "Hola"
let array: [Int] = [1, 2, 3, 4, 5]
```

</div>
<div class="week08-definition-stack">
  <div><b>Checked</b><span>The compiler checks that operations use compatible types.</span></div>
  <div><b>Explicit</b><span>A colon introduces the declared type.</span></div>
  <div><b>Inferred</b><span>The compiler can often recover the same type from the value.</span></div>
</div>
</div>

<!--
Idea: Establish the type annotations used throughout both Swift weeks.
Say: "The annotation follows the name. Array of Int is written with square brackets."
Bridge: "When the initializer is unambiguous, Swift can omit the annotation."
-->

---

<div class="eyebrow">Type inference</div>

## The compiler can infer the declared types

<div class="week08-code-pair">
<div>
<b>Explicit types</b>

```swift
let n: Int = 10
let str: String = "Hola"
let array: [Int] = [1, 2, 3, 4, 5]
```
</div>
<div>
<b>Inferred types</b>

```swift
let n = 10
let str = "Hola"
let array = [1, 2, 3, 4, 5]
```
</div>
</div>

<div class="week08-conclusion"><code>n</code><span>still has type</span><code>Int</code></div>

<!--
Idea: Make clear that inference removes syntax, not types.
Say: "Swift remains strongly typed. The compiler infers Int, String, and Array of Int from the initializers."
Bridge: "The other distinction visible in a declaration is whether the value may change."
-->

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Immutability

<p class="lead">A value declared with <code>let</code> cannot be reassigned. Operations may instead construct and return a new value.</p>

<!--
Idea: Use the same section boundary as the class notes.
Say: "Swift distinguishes variables from constants. The next examples compare operations that return a new value with operations that mutate an existing variable."
Bridge: "The declaration keyword makes the first distinction visible."
-->

---

<div class="eyebrow">let and var</div>

## `let` prevents reassignment

<div class="columns equal">
<div>

```swift
var x = 10
x = 20        // valid
```

<div class="week08-value-label mutable"><b>var</b><span>mutable variable</span></div>
</div>
<div>

```swift
let y = 10
y = 20        // compile-time error
```

<div class="week08-value-label immutable"><b>let</b><span>immutable value</span></div>
</div>
</div>

<div class="week08-note-line"><b>The value may come from run time</b><code>let respuesta = respuestaUsuario.respuesta()</code></div>

<!--
Idea: Separate immutability from compile-time constants.
Say: "A let value need not be known while compiling. It becomes fixed once initialized."
Bridge: "This distinction also appears in the methods offered by collection types."
-->

---

<div class="eyebrow">New value or mutation</div>

## `sorted()` returns a new array

<div class="columns equal">
<div>

```swift
let miArray = [10, -1, 3, 80]
let arrayOrdenado = miArray.sorted()

print(miArray)
// [10, -1, 3, 80]

print(arrayOrdenado)
// [-1, 3, 10, 80]
```

</div>
<div class="week08-before-after">
  <div><b>Original</b><code>[10, -1, 3, 80]</code></div>
  <div><b>Returned value</b><code>[-1, 3, 10, 80]</code></div>
  <strong>The original array does not change.</strong>
</div>
</div>

<!--
Idea: Use the exact functional sorting example from the notes.
Say: "The method constructs and returns an ordered array. The value bound to miArray remains unchanged."
Bridge: "The imperative counterpart changes the receiver itself."
-->

---

<div class="eyebrow">New value or mutation</div>

## `sort()` mutates the original array

<div class="columns equal">
<div>

```swift
var miArray = [10, -1, 3, 80]
miArray.sort()

print(miArray)
// [-1, 3, 10, 80]
```

</div>
<div class="week08-mutation-rule">
  <code>sorted()</code><span>requires no mutation and returns an array</span>
  <code>sort()</code><span>changes a variable declared with <code>var</code></span>
</div>
</div>

<div class="week08-warning"><b>Functional style</b><span>Prefer operations that construct new values and avoid side effects.</span></div>

<!--
Idea: Contrast the two library methods directly.
Say: "The method names differ by one letter, but their effects differ completely. sort needs mutable state."
Bridge: "Appending an element offers the same contrast."
-->

---

<div class="eyebrow">Adding an array element</div>

## `+` constructs while `append` mutates

<div class="week08-code-pair">
<div>
<b>New array</b>

```swift
let miArray = [10, -1, 3, 80]
let array2 = miArray + [100]

// array2: [10, -1, 3, 80, 100]
```
</div>
<div>
<b>Mutation</b>

```swift
var miArray = [10, -1, 3, 80]
miArray.append(100)

// miArray: [10, -1, 3, 80, 100]
```
</div>
</div>

<div class="week08-conclusion"><code>let</code><span>also blocks mutating methods such as</span><code>append</code></div>

<!--
Idea: Repeat the notes' second mutation comparison.
Say: "Both fragments produce the same elements. Only the second changes an existing array."
Bridge: "Now we can define functions that preserve this value-oriented style."
-->

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Functions

<p class="lead">Swift function declarations make parameter types, argument labels, and return types explicit.</p>

<!--
Idea: Introduce the syntax before moving to recursion and first-class functions.
Say: "Swift adds a type and an external label to each parameter. Those labels form part of the function's public name."
Bridge: "A small greeting function contains all the basic pieces."
-->

---

<div class="eyebrow">Function declaration</div>

## Parameters precede the return type

```swift
func saluda(nombre: String) -> String {
    let saludo = "Hola, " + nombre + "!"
    return saludo
}

print(saluda(nombre: "Ana"))
// Hola, Ana!
```

<div class="week08-anatomy">
  <div><code>func saluda</code><span>function name</span></div>
  <div><code>nombre: String</code><span>parameter and type</span></div>
  <div><code>-> String</code><span>return type</span></div>
  <div><code>return saludo</code><span>returned value</span></div>
</div>

<!--
Idea: Read the declaration from left to right.
Say: "The call includes nombre because Swift uses the parameter name as the argument label by default."
Bridge: "The external label and the internal name can also be different."
-->

---

<div class="eyebrow">Argument labels</div>

## External labels describe the call

```swift
func saluda(nombre: String, de ciudad: String) -> String {
    return "Hola \(nombre)! Vienes desde \(ciudad)."
}

saluda(nombre: "Bill", de: "Cupertino")
```

<div class="week08-label-map">
  <div><b>Call site</b><code>de:</code><span>argument label</span></div>
  <div><b>Function body</b><code>ciudad</code><span>parameter name</span></div>
</div>

<!--
Idea: Distinguish the two names attached to one parameter.
Say: "The caller reads de, while the body reads ciudad. The label explains the role of the argument in the sentence formed by the call."
Bridge: "An underscore removes an external label."
-->

---

<div class="eyebrow">Omitting labels</div>

## `_` allows positional arguments

<div class="columns equal">
<div>

```swift
func max(_ x: Int, _ y: Int) -> Int {
    if x > y {
        return x
    } else {
        return y
    }
}

max(10, 3)
```

</div>
<div>

```swift
func divide(_ x: Double,
            entre y: Double) -> Double {
    return x / y
}

divide(30, entre: 4)
```

</div>
</div>

<!--
Idea: Show a fully positional function and a mixed-label function.
Say: "The underscore suppresses the label. divide keeps a label only where it makes the call easier to read."
Bridge: "These labels contribute to the complete name of a function."
-->

---

<div class="eyebrow">Complete function names</div>

## Labels distinguish functions with the same base name

<div class="columns equal">
<div>

```swift
func mitad(par: Int) -> Int {
    return par / 2
}

mitad(par: 8)      // 4
```

</div>
<div>

```swift
func mitad(impar: Int) -> Int {
    return (impar + 1) / 2
}

mitad(impar: 9)    // 5
```

</div>
</div>

<div class="week08-signatures"><code>mitad(par:)</code><code>mitad(impar:)</code></div>

<!--
Idea: Use the exact overload example from the notes.
Say: "The complete name includes the argument labels, so these are two distinct functions."
Bridge: "Parameters and return values can also be absent or compound."
-->

---

<div class="eyebrow">Parameters and return values</div>

## Functions may omit parameters or a result

<div class="week08-code-pair">
<div>
<b>No parameters</b>

```swift
func diHolaMundo() -> String {
    return "hola, mundo"
}
```
</div>
<div>
<b>No returned value</b>

```swift
func diAdios(nombre: String) {
    print("Adiós, \(nombre)!")
}
```
</div>
</div>

<div class="week08-warning"><b>Functional observation</b><span>A function that only prints performs a side effect instead of returning a value.</span></div>

<!--
Idea: Preserve the functional caveat in the notes.
Say: "A procedure with no result can be useful, but printing is an observable effect. Pure functions return a value instead."
Bridge: "A function can also return several related values as one tuple."
-->

---

<div class="eyebrow">Multiple results</div>

## A tuple groups the two roots of an equation

```swift
func ecuacion(a: Double, b: Double, c: Double)
    -> (pos: Double, neg: Double) {
    let discriminante = b * b - 4 * a * c
    let raizPositiva = (-b + discriminante.squareRoot()) / (2 * a)
    let raizNegativa = (-b - discriminante.squareRoot()) / (2 * a)
    return (raizPositiva, raizNegativa)
}

let resultado = ecuacion(a: 1, b: -5, c: 6)
resultado.pos     // 3.0
resultado.neg     // 2.0
```

<!--
Idea: Show labelled tuple components as the function result.
Say: "The returned value is one tuple. Its labels make resultado.pos and resultado.neg more descriptive than numeric positions."
Bridge: "The same syntax supports recursive functions."
-->

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Recursion

<p class="lead">A Swift function can call itself. The definition still needs a base case and a smaller recursive problem.</p>

<!--
Idea: Keep functions and recursion as separate sections, following the class notes.
Say: "The syntax is Swift, but the recursive design method is the same one used in Scheme."
Bridge: "The first example also makes the pending operations visible."
-->

---

<div class="eyebrow">Recursive function</div>

## The result waits for the recursive call

<div class="columns equal">
<div>

```swift
func suma(hasta x: Int) -> Int {
    if x == 0 {
        return 0
    } else {
        return x + suma(hasta: x - 1)
    }
}

suma(hasta: 5)    // 15
```

</div>
<div class="week08-recursion-rule">
  <div><b>Base case</b><code>x == 0</code><span>return 0</span></div>
  <div><b>Recursive case</b><code>x > 0</code><span>add x to the smaller problem</span></div>
  <strong>The pending addition remains on the call stack.</strong>
</div>
</div>

<!--
Idea: Connect Swift recursion with the process model from week 5.
Say: "This definition is recursive, not tail-recursive. Each invocation must wait to add x after the recursive result arrives, so calls remain pending and consume stack space."
Bridge: "Arrays need an explicit way to obtain the first element and the remaining elements."
-->

---

<div class="eyebrow">Array decomposition</div>

## Index zero and `dropFirst()` imitate `first` and `rest`

```swift
let a = [10, 20, 30, 40, 50, 60]

let primero = a[0]
let resto = Array(a.dropFirst())
```

<div class="week08-array-strip">
  <div class="head"><b>primero</b><code>10</code></div>
  <div class="tail"><b>resto</b><code>[20, 30, 40, 50, 60]</code></div>
</div>

<div class="week08-note-line"><b>Why the constructor?</b><span><code>dropFirst()</code> returns an <code>ArraySlice</code>. <code>Array(...)</code> creates an array.</span></div>

<!--
Idea: Translate the Scheme decomposition without claiming arrays are linked lists.
Say: "dropFirst returns a slice view, not an Array. The constructor performs the conversion expected by our recursive function."
Bridge: "With this decomposition, the Scheme-style sum transfers directly."
-->

---

<div class="eyebrow">Recursion over arrays</div>

## Empty array or first plus the recursive result

```swift
func sumaValores(_ valores: [Int]) -> Int {
    if valores.isEmpty {
        return 0
    } else {
        let primero = valores[0]
        let resto = Array(valores.dropFirst())
        return primero + sumaValores(resto)
    }
}

sumaValores([1, 2, 3, 4, 5, 6, 7, 8])    // 36
```

<div class="week08-recursive-flow"><code>[] → 0</code><code>[x] + rest → x + sumaValores(rest)</code></div>

<!--
Idea: Preserve the recursive shape from the notes.
Say: "The base case contributes the neutral element zero. The recursive case reduces the array by one element."
Bridge: "A recursive call may return a compound result, not only one number."
-->

---

<!-- _class: compact -->

<div class="eyebrow">A tuple from recursion</div>

## One recursive call finds both limits of the rest

```swift
func minMax(array: [Int]) -> (min: Int, max: Int) {
    if array.count == 1 {
        return (array[0], array[0])
    } else {
        let primero = array[0]
        let resto = Array(array.dropFirst())
        let limitesResto = minMax(array: resto)

        return (min(primero, limitesResto.min),
                max(primero, limitesResto.max))
    }
}
```

<div class="week08-conclusion"><code>[8, -6, 2, 100, 3, 71]</code><span>returns</span><code>(min: -6, max: 100)</code></div>

<!--
Idea: Emphasize the single recursive call and tuple result.
Say: "The recursive result already contains both values for the tail. The current first element is compared with each component."
Bridge: "All intermediate names use let, so this stepwise code still avoids mutation."
-->

---

<!-- _class: section -->

<div class="eyebrow">05</div>

# Function types

<p class="lead">Functions are first-class values: Swift can store them, pass them, and return them.</p>

<!--
Idea: State the three first-class operations used in the notes.
Say: "The type system records the parameter types and result type of every function value."
Bridge: "Two arithmetic functions can share one type."
-->

---

<div class="eyebrow">Function values</div>

## Parameter types and return type define the function type

<div class="columns equal">
<div>

```swift
func sumaDosInts(a: Int, b: Int) -> Int {
    return a + b
}

func multiplicaDosInts(a: Int, b: Int) -> Int {
    return a * b
}
```

</div>
<div class="week08-function-type">
  <code>(Int, Int) -> Int</code>
  <span>two Int parameters</span>
  <span>one Int result</span>
</div>
</div>

<!--
Idea: Read the function type separately from the function names and labels.
Say: "Both declarations have the same function type even though their bodies perform different operations."
Bridge: "That shared type lets one variable refer to either function."
-->

---

<div class="eyebrow">Assigning function values</div>

## One variable can hold different functions of the same type

```swift
var f = sumaDosInts
f(2, 3)                    // 5

f = multiplicaDosInts
f(2, 3)                    // 6
```

<div class="week08-function-slot">
  <span>variable</span><code>f</code><b>type</b><code>(Int, Int) -> Int</code>
</div>

<div class="week08-warning"><b>No argument labels</b><span>A function value is invoked as <code>f(2, 3)</code>, using only its function type.</span></div>

<!--
Idea: Explain why labels disappear through a function-valued variable.
Say: "f can refer to any value of that function type. The type does not retain the original labels a and b."
Bridge: "Function types also appear as parameter types."
-->

---

<div class="eyebrow">A function parameter</div>

## The caller supplies the operation

```swift
func printResultado(
    funcion: (Int, Int) -> Int,
    _ a: Int,
    _ b: Int
) {
    print("Resultado: \(funcion(a, b))")
}

printResultado(funcion: sumaDosInts, 3, 5)
// Resultado: 8
```

<div class="week08-call-path"><code>sumaDosInts</code><span>passed as a value</span><code>funcion(3, 5)</code><span>invoked inside</span></div>

<!--
Idea: Show that the function is passed, not called at the call site.
Say: "There are no parentheses after sumaDosInts in the argument. printResultado receives the function and decides when to invoke it."
Bridge: "The same idea abstracts the operation performed at each point of a sum."
-->

---

<div class="eyebrow">Higher-order recursive sum</div>

## `sumatorio` applies a function before adding

<div class="week08-equation">
  <code>f(a) + f(a + 1) + ··· + f(b)</code>
</div>

```swift
func sumatorio(desde a: Int,
               hasta b: Int,
               func f: (Int) -> Int) -> Int {
    if a > b {
        return 0
    } else {
        return f(a) + sumatorio(desde: a + 1, hasta: b, func: f)
    }
}
```

<!--
Idea: Present the abstraction before the concrete operations.
Say: "The recursion controls the interval. The function parameter controls what value each integer contributes."
Bridge: "Changing only the function argument changes the resulting series."
-->

---

<div class="eyebrow">One traversal, three computations</div>

## The function argument selects each contribution

```swift
func identidad(_ x: Int) -> Int { x }
func doble(_ x: Int) -> Int { x + x }
func cuadrado(_ x: Int) -> Int { x * x }

sumatorio(desde: 0, hasta: 10, func: identidad)   // 55
sumatorio(desde: 0, hasta: 10, func: doble)       // 110
sumatorio(desde: 0, hasta: 10, func: cuadrado)    // 385
```

<div class="week08-result-row">
  <div><code>identidad</code><b>55</b></div>
  <div><code>doble</code><b>110</b></div>
  <div><code>cuadrado</code><b>385</b></div>
</div>

<!--
Idea: Keep the interval constant and vary only the passed function.
Say: "The recursive structure is reused. identidad sums the integers, doble sums twice each integer, and cuadrado sums their squares."
Bridge: "Function values can also be elements of a collection."
-->

---

<div class="eyebrow">Functions in arrays</div>

## Every element must have the same function type

```swift
let funciones = [identidad, doble, cuadrado]

funciones[0](10)    // 10
funciones[1](10)    // 20
funciones[2](10)    // 100
```

<div class="week08-function-array">
  <b>Array type</b><code>[(Int) -> Int]</code>
  <span><code>suma(_:_:)</code> cannot join this array because its type is <code>(Int, Int) -> Int</code>.</span>
</div>

<!--
Idea: Connect homogeneous arrays with strong typing.
Say: "Every stored function accepts one Int and returns one Int. A two-argument function has a different type."
Bridge: "Finally, a function can construct and return another function."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Returning a function</div>

## A returned function can capture its surrounding value

```swift
func construyeSumador(inc: Int) -> (Int) -> Int {
    func suma(x: Int) -> Int {
        return x + inc
    }
    return suma
}

let f2 = construyeSumador(inc: 10)
let f3 = construyeSumador(inc: 100)

f2(20)    // 30
f3(20)    // 120
```

<div class="week08-closure-capture"><code>f2</code><span>captures 10</span><code>f3</code><span>captures 100</span></div>

<!--
Idea: Introduce closures with an immutable captured parameter.
Say: "Each call creates a function whose body can still use inc after construyeSumador has returned. We will study capture in detail next week."
Bridge: "Before recursive enums, we need a vocabulary for Swift types."
-->

---

<!-- _class: section -->

<div class="eyebrow">06</div>

# Types

<p class="lead">Named types identify declarations. Composite types describe tuples and functions directly.</p>

<!--
Idea: Follow the two-category distinction in the notes.
Say: "This classification is about how a type is written, not whether its values are mutable."
Bridge: "Named types include both library types and our own declarations."
-->

---

<div class="eyebrow">Named and composite types</div>

## Swift uses two forms of type description

<div class="week08-type-columns">
  <div>
    <b>Named types</b>
    <code>Int</code><code>String</code><code>Array&lt;Int&gt;</code>
    <span>Classes, structures, enumerations, and protocols introduce names.</span>
  </div>
  <div>
    <b>Composite types</b>
    <code>(Int, String)</code><code>(Int) -> Bool</code>
    <span>Tuples and function types describe their components directly.</span>
  </div>
</div>

<!--
Idea: Give the exact two composite categories stated in the topic.
Say: "Int and String are named types from the standard library. A tuple and a function type need no declaration of their own name."
Bridge: "A typealias can attach a convenient name to any existing type."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Type aliases</div>

## `typealias` names an existing type

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
```

<div class="week08-conclusion"><code>Resultado</code><span>and</span><code>(Int, Int)</code><span>denote the same type</span></div>

<!--
Idea: Make clear that typealias is syntactic convenience, not a new distinct type.
Say: "The alias documents that this pair represents a match result. switch decomposes the tuple and its where clauses compare the goals."
Bridge: "A separate classification determines whether assignment copies a value or shares an object."
-->

---

<div class="eyebrow">Assignment semantics</div>

## Value types copy while reference types share

<div class="week08-semantics">
  <div class="value">
    <b>Value type</b>
    <span>Assignment gives the destination its own value.</span>
    <code>struct</code><code>enum</code>
  </div>
  <div class="reference">
    <b>Reference type</b>
    <span>Assignment makes both variables refer to one instance.</span>
    <code>class</code>
  </div>
</div>

<div class="week08-note-line"><b>Standard library</b><span><code>Int</code>, <code>String</code>, <code>Array</code>, and <code>Dictionary</code> are structures.</span></div>

<!--
Idea: State the distinction from the topic before examples.
Say: "Structures and enumerations have value semantics. Classes have reference semantics, which we will examine in the object-oriented topic."
Bridge: "Strings show the observable result of value semantics."
-->

---

<div class="eyebrow">Value semantics</div>

## Changing one string leaves its copy unchanged

```swift
var str1 = "Hola"
var str2 = str1

str1.append("Adios")

print(str1)    // HolaAdios
print(str2)    // Hola
```

<div class="week08-copy-diagram">
  <div><code>str1</code><span>after mutation</span><b>"HolaAdios"</b></div>
  <div><code>str2</code><span>independent value</span><b>"Hola"</b></div>
</div>

<!--
Idea: Demonstrate behavior rather than describe implementation details.
Say: "Assigning str1 to str2 gives str2 its own value. Later mutation of str1 does not affect str2."
Bridge: "Arrays provide the same value semantics."
-->

---

<div class="eyebrow">Value semantics</div>

## Arrays also behave as independent values

```swift
var array1 = [1, 2, 3, 4]
var array2 = array1

array1[0] = 10

print(array1)    // [10, 2, 3, 4]
print(array2)    // [1, 2, 3, 4]
```

<div class="week08-warning"><b>Copy on write</b><span>Swift can share storage until one value is modified, while preserving value semantics.</span></div>

<!--
Idea: Explain the semantic guarantee separately from the optimization.
Say: "The programmer observes two independent arrays. Copy on write avoids an eager physical copy when neither value changes."
Bridge: "Function parameters reinforce the same immutable view."
-->

---

<div class="eyebrow">Function parameters</div>

## Parameters are immutable inside the function

```swift
func ponCero(array: [Int], pos: Int) {
    array[pos] = 0
    // error: cannot assign through subscript
    // 'array' is a 'let' constant
}
```

<div class="week08-parameter-rule">
  <code>array</code><span>receives a value</span>
  <code>array[pos] = 0</code><span>tries to mutate the local parameter</span>
  <b>compile-time error</b>
</div>

<!--
Idea: Keep the exact compiler-level restriction from the topic.
Say: "A parameter behaves as an immutable local binding. A function that needs to produce a changed array should return a new array."
Bridge: "Enumerations now let us define precise sets of possible values."
-->

---

<!-- _class: section -->

<div class="eyebrow">07</div>

# Enumerations

<p class="lead">An enumeration defines a type whose values belong to a fixed set of cases.</p>

<!--
Idea: Introduce simple cases before raw and associated values.
Say: "An enum gives meaningful names to the alternatives and lets switch check every case."
Bridge: "A direction is the simplest example."
-->

---

<div class="eyebrow">Enumeration cases</div>

## A variable can hold only a declared case

```swift
enum Direccion {
    case norte
    case sur
    case este
    case oeste
}

var direccionActual = Direccion.norte
direccionActual = .sur
```

<div class="week08-enum-cases"><code>.norte</code><code>.sur</code><code>.este</code><code>.oeste</code></div>

<!--
Idea: Show the shorthand made possible by type inference.
Say: "The full name is needed for the first value. Once Swift knows the type, dot syntax is enough."
Bridge: "switch can branch on every possible case."
-->

---

<div class="eyebrow">Exhaustive switch</div>

## Each case selects one branch

```swift
let direccion = Direccion.sur

switch direccion {
case .norte:
    print("Nos vamos al norte")
case .sur:
    print("Cuidado con los pingüinos")
case .este:
    print("Donde nace el sol")
case .oeste:
    print("Donde el cielo es azul")
}
```

<div class="week08-conclusion"><code>.sur</code><span>selects</span><code>Cuidado con los pingüinos</code></div>

<!--
Idea: Demonstrate pattern matching over a finite type.
Say: "Because Direccion defines four alternatives, the switch accounts for all four without a default branch."
Bridge: "A case may also have one fixed raw value."
-->

---

<div class="eyebrow">Raw values</div>

## Every case can have a fixed underlying value

<div class="columns equal">
<div>

```swift
enum Quiniela: Int {
    case uno = 1
    case equis = 0
    case dos = 2
}

Quiniela.equis.rawValue    // 0
```

</div>
<div>

```swift
enum Planeta: Int {
    case mercurio = 1, venus, tierra,
         marte, jupiter, saturno,
         urano, neptuno
}

Planeta.tierra.rawValue    // 3
```

</div>
</div>

<!--
Idea: Distinguish explicit and automatically incremented integer raw values.
Say: "A raw value belongs to the case definition. Every instance of that case has the same raw value."
Bridge: "Converting a raw value back into a case may fail."
-->

---

<div class="eyebrow">Initialization from a raw value</div>

## A lookup by raw value returns an optional

```swift
let posiblePlaneta = Planeta(rawValue: 7)
```

<div class="week08-raw-lookup">
  <code>7</code><span>matches a case</span><code>Planeta.urano</code>
  <code>20</code><span>matches no case</span><code>nil</code>
</div>

<div class="week08-note-line"><b>Inferred type</b><code>Planeta?</code><span>The question mark means that the result may be absent. Optionals are the first topic of week 9.</span></div>

<!--
Idea: Preview optionals only to explain why raw-value initialization cannot promise a case.
Say: "The initializer cannot know whether an arbitrary integer identifies a planet. It therefore returns either a Planeta or nil."
Bridge: "Associated values solve a different problem: storing instance-specific data inside a case."
-->

---

<!-- _class: section -->

<div class="eyebrow">08</div>

# Associated values and recursive enumerations

<p class="lead">An enum case can carry data, including another value of the same enum.</p>

<!--
Idea: Move from a finite label set to algebraic data with payloads.
Say: "Each case determines the type and shape of the data stored in that particular value."
Bridge: "Multiple stores either an integer or a string."
-->

---

<div class="eyebrow">Associated values</div>

## Different cases can carry different types

```swift
enum Multiple {
    case num(Int)
    case str(String)
}

let valor3 = Multiple.num(10)
let valor4 = Multiple.str("Hola")
```

<div class="week08-associated-values">
  <div><code>.num</code><b>case</b><span>associated <code>Int</code>: 10</span></div>
  <div><code>.str</code><b>case</b><span>associated <code>String</code>: "Hola"</span></div>
</div>

<!--
Idea: Treat the case as a constructor that requires its payload.
Say: "Multiple.num alone is incomplete. Constructing a value requires the associated Int. The str case requires a String."
Bridge: "A switch extracts that payload with case let."
-->

---

<div class="eyebrow">Extracting associated values</div>

## `case let` binds the data carried by the case

```swift
func imprime(multiple: Multiple) {
    switch multiple {
    case let .num(x):
        print("Multiple tiene un Int: \(x)")
    case let .str(s):
        print("Multiple tiene un String: \(s)")
    }
}

imprime(multiple: valor3)    // ... Int: 10
imprime(multiple: valor4)    // ... String: Hola
```

<!--
Idea: Show pattern matching as both case selection and payload extraction.
Say: "The variable x exists only in the num branch and s only in the str branch."
Bridge: "Associated values and raw values must not be confused."
-->

---

<div class="eyebrow">Raw value or associated value</div>

## The two mechanisms answer different questions

<div class="week08-comparison-table">
  <div class="header"><b>Mechanism</b><b>Defined</b><b>Meaning</b></div>
  <div><strong>Raw value</strong><span>once with the enum case</span><span>the same fixed representation for that case</span></div>
  <div><strong>Associated value</strong><span>when an instance is created</span><span>data that can differ between instances</span></div>
</div>

<!--
Idea: Reproduce the warning in the notes as a compact comparison.
Say: "Quiniela.equis always has raw value zero. Multiple.num can carry 10 in one value and 25 in another."
Bridge: "An associated value may itself be a tuple."
-->

---

<div class="eyebrow">Compound associated values</div>

## A case can carry several related fields

```swift
enum CodigoBarras {
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}

var codigo = CodigoBarras.upc(8, 85909, 51226, 3)
codigo = .qrCode("ABCDEFGHIJKLMNOP")
```

<div class="week08-barcode-types">
  <code>.upc</code><span>carries four integers</span>
  <code>.qrCode</code><span>carries one string</span>
</div>

<!--
Idea: Show that each case defines its own payload shape.
Say: "The enum variable keeps one case at a time, and its associated data has the type required by that case."
Bridge: "If the payload type refers back to the enum, the data becomes recursive."
-->

---

<div class="eyebrow">Recursive enumeration</div>

## `indirect` permits a case to contain the same enum

```swift
indirect enum ExpresionAritmetica {
    case numero(Int)
    case suma(ExpresionAritmetica,
              ExpresionAritmetica)
    case multiplicacion(ExpresionAritmetica,
                        ExpresionAritmetica)
}
```

<div class="week08-recursive-enum">
  <div><code>.numero(5)</code><span>leaf</span></div>
  <div><code>.suma(left, right)</code><span>two subexpressions</span></div>
  <div><code>.multiplicacion(left, right)</code><span>two subexpressions</span></div>
</div>

<!--
Idea: Relate the cases to the tree structure studied in week 7.
Say: "numero ends the recursion. suma and multiplicacion store two complete arithmetic expressions."
Bridge: "We can construct the expression (5 + 4) times 2 from inside out."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Constructing an expression</div>

## Cases build the recursive value from its subexpressions

```swift
let cinco = ExpresionAritmetica.numero(5)
let cuatro = ExpresionAritmetica.numero(4)
let suma = ExpresionAritmetica.suma(cinco, cuatro)
let producto = ExpresionAritmetica.multiplicacion(
    suma,
    ExpresionAritmetica.numero(2)
)
```

<div class="week08-expression-tree">
  <code>multiplicacion</code>
  <div><span><code>suma</code><small><code>numero(5)</code><code>numero(4)</code></small></span><span><code>numero(2)</code></span></div>
</div>

<!--
Idea: Make the recursive construction visible without adding a new example.
Say: "The product contains the already constructed sum as its left subexpression and numero(2) as its right subexpression."
Bridge: "Evaluation follows exactly the same recursive shape."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Evaluating the expression</div>

## Each case determines the recursive computation

```swift
func evalua(expresion: ExpresionAritmetica) -> Int {
    switch expresion {
    case let .numero(valor):
        return valor
    case let .suma(izquierda, derecha):
        return evalua(expresion: izquierda)
             + evalua(expresion: derecha)
    case let .multiplicacion(izquierda, derecha):
        return evalua(expresion: izquierda)
             * evalua(expresion: derecha)
    }
}

evalua(expresion: producto)    // 18
```

<!--
Idea: Align each data constructor with one function branch.
Say: "numero returns its stored value. The two recursive cases evaluate both subexpressions and combine their results with the matching operator."
Bridge: "A Scheme-style list can use the same enum pattern."
-->

---

<div class="eyebrow">A recursive list type</div>

## A list is empty or one node followed by another list

```swift
indirect enum Lista {
    case vacia
    case nodo(Int, Lista)
}
```

<div class="week08-list-definition">
  <div><code>.vacia</code><span>base case</span><b>no element</b></div>
  <div><code>.nodo(Int, Lista)</code><span>recursive case</span><b>first value and rest</b></div>
</div>

<!--
Idea: Match the recursive data definition to the Scheme pair model.
Say: "The second field of nodo is a complete Lista, so it represents the rest. vacia ends the chain."
Bridge: "Constructing a list means nesting nodo cases."
-->

---

<div class="eyebrow">Constructing a recursive list</div>

## The innermost node is built first

```swift
let lista1 = Lista.nodo(30, Lista.vacia)
let lista2 = Lista.nodo(20, lista1)
let lista3 = Lista.nodo(10, lista2)
```

<div class="week08-list-chain">
  <code>nodo(10,</code><code>nodo(20,</code><code>nodo(30,</code><code>vacia)))</code>
</div>

```swift
let lista: Lista = .nodo(10, .nodo(20, .nodo(30, .vacia)))
```

<!--
Idea: Show the expanded construction and its compact equivalent.
Say: "lista1 represents the suffix containing 30. Each following node adds one value to the front."
Bridge: "A recursive function uses switch to distinguish the same two cases."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Recursion over the enum</div>

## `suma` follows the two cases of `Lista`

```swift
func suma(lista: Lista) -> Int {
    switch lista {
    case .vacia:
        return 0
    case let .nodo(first, rest):
        return first + suma(lista: rest)
    }
}

let z: Lista = .nodo(20, .nodo(10, .vacia))
suma(lista: z)    // 30
```

<div class="week08-case-map"><code>.vacia</code><span>returns 0</span><code>.nodo</code><span>adds first and recurs on rest</span></div>

<!--
Idea: Reinforce that recursive data drives recursive control flow.
Say: "The switch has one branch per constructor. The recursive call receives exactly the recursive component stored by nodo."
Bridge: "We can also construct this enum recursively from a Swift array."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">Converting an array into `Lista`</div>

## The array decomposition builds one enum node at a time

```swift
func construye(lista: [Int]) -> Lista {
    if lista.isEmpty {
        return Lista.vacia
    } else {
        let primero = lista[0]
        let resto = Array(lista.dropFirst())
        return Lista.nodo(primero,
                          construye(lista: resto))
    }
}

let lista2 = construye(lista: [1, 2, 3, 4, 5])
suma(lista: lista2)    // 15
```

<!--
Idea: Close the week by joining arrays, recursion, and recursive enums.
Say: "An empty array becomes vacia. Otherwise, the first element becomes a node whose rest is constructed recursively."
Bridge: "Week 9 adds safe absence, compact closures, collection transformations, and generic types."
-->
