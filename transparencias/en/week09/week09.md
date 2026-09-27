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
<div class="week-marker">Week 9</div>

# Functional programming with Swift II

<p class="lead">Topic 5 · Optionals, closures, higher-order functions, and generics</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Continue directly from the optional returned by raw-value enum initialization.
Say: "This week studies how Swift represents missing values, writes functions compactly, transforms collections, and abstracts over types."
Bridge: "The four blocks build on the typed functional tools from week 8."
-->

---

<div class="eyebrow">Today</div>

## Four extensions of functional Swift

<div class="sequence week04-roadmap">
  <div><b>1 · OPTIONALS</b><span>Represent and use a value that may be absent</span></div>
  <div><b>2 · CLOSURES</b><span>Write anonymous functions and capture their context</span></div>
  <div><b>3 · COLLECTIONS</b><span>Transform, select, and combine with higher-order methods</span></div>
  <div><b>4 · GENERICS</b><span>Write one definition for many concrete types</span></div>
</div>

<!--
Idea: Follow the four numbered sections in the class notes.
Say: "Optionals add safe absence. Closures provide function values. Collection methods consume those closures, and generics explain their reusable types."
Bridge: "We begin with the problem caused by an absent value."
-->

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Optionals

<p class="lead">An optional contains either a value of its declared type or <code>nil</code>.</p>

<!--
Idea: Give the two possibilities explicitly.
Say: "A normal String cannot contain nil. String question mark is a different type that represents either a String or absence."
Bridge: "A dictionary lookup is a natural source of an optional."
-->

---

<div class="eyebrow">Optional types</div>

## `?` makes absence part of the type

<div class="columns equal">
<div>

```swift
// Compile-time error
let cadena: String = nil
```

<div class="week09-optional-box impossible"><code>String</code><span>must contain a string</span></div>
</div>
<div>

```swift
var cadena: String? = "Hola"
cadena = nil
```

<div class="week09-optional-box possible"><code>String?</code><span>contains a string or nil</span></div>
</div>
</div>

<!--
Idea: Show that nil is rejected unless the type explicitly permits absence.
Say: "The question mark changes the type. It is not merely an annotation on one particular value."
Bridge: "Lookups use this type because a key may be missing."
-->

---

<div class="eyebrow">A lookup may fail</div>

## Dictionary subscripting returns an optional

```swift
let edades = [
    "Raquel": 30,
    "Pedro": 22
]

let edad1 = edades["Raquel"]
let edad2 = edades["Ana"]
```

<div class="week09-lookup-results">
  <div><code>edad1</code><span>type <code>Int?</code></span><b>30</b></div>
  <div><code>edad2</code><span>type <code>Int?</code></span><b>nil</b></div>
</div>

<!--
Idea: Explain why both results have the same optional type.
Say: "Even a successful lookup returns Int question mark because the operation cannot guarantee that every requested key exists."
Bridge: "An optional value cannot be used directly as the wrapped type."
-->

---

<div class="eyebrow">Wrapped values</div>

## An `Int?` is not an `Int`

<div class="week09-code-pair">
<div>
<b>Still wrapped</b>

```swift
var x: Int? = 10
let y = x + 10
// compile-time error
```
</div>
<div>
<b>Forced unwrapping</b>

```swift
var x: Int? = 10
let y = x! + 10
// y is 20
```
</div>
</div>

<div class="week09-unwrap-flow"><code>Int?</code><span>unwrap</span><code>Int</code><span>use in arithmetic</span></div>

<!--
Idea: Treat unwrapping as a type transition.
Say: "The compiler prevents arithmetic on a value that might be absent. Exclamation mark asserts that a value is present."
Bridge: "That assertion fails catastrophically when the optional contains nil."
-->

---

<div class="eyebrow">Forced unwrapping</div>

## `!` on `nil` causes a run-time error

```swift
var respuestaEncuesta: String?
print(respuestaEncuesta!)

// Fatal error: Unexpectedly found nil
// while unwrapping an Optional value
```

<div class="week09-warning"><b>The assertion behind <code>!</code></b><span>“I know this optional contains a value.” The program stops if that assertion is false.</span></div>

<!--
Idea: Make forced unwrapping's contract explicit.
Say: "The compiler accepts the assertion, but the program still checks it at run time. We should prefer constructs that handle both possibilities."
Bridge: "Functions can expose possible failure in their return type."
-->

---

<div class="eyebrow">Optional return value</div>

<!-- _class: compact code-small -->

## An empty array has no maximum

```swift
func max(array: [Int]) -> Int? {
    if array.isEmpty {
        return nil
    } else if array.count == 1 {
        return array[0]
    } else {
        let primero = array[0]
        let resto = Array(array.dropFirst())
        return max(primero, max(array: resto)!)
    }
}

max(array: [])                    // nil
max(array: [10, 200, -100, 2])    // 200
```

<!--
Idea: Use the exact recursive example from the notes.
Say: "The return type records the empty-array case. The recursive branch force-unwraps because a nonempty array's rest is eventually handled by the one-element branch before it becomes empty."
Bridge: "Optional binding provides a safer general way to check and unwrap."
-->

---

<div class="eyebrow">Optional binding</div>

## `if let` checks and unwraps in one step

<div class="week09-code-pair">
<div>
<b>Manual check</b>

```swift
let opcional = leerRespuesta()

if opcional != nil {
    let respuesta = opcional!
    print("Respuesta: " + respuesta)
}
```
</div>
<div>
<b>Optional binding</b>

```swift
if let respuesta = leerRespuesta() {
    print("Respuesta: " + respuesta)
}
```
</div>
</div>

<div class="week09-binding-scope"><code>respuesta</code><span>has type <code>String</code> and exists only inside the <code>if</code> body</span></div>

<!--
Idea: Show the equivalence while emphasizing scope and nonoptional type.
Say: "The body runs only when a value exists. Inside it, respuesta is already a String, so no exclamation mark is needed."
Bridge: "Array.first lets recursion use the same pattern."
-->

---

<div class="eyebrow">Optional binding in recursion</div>

## `first` combines the test and the first element

```swift
func sumaValores(_ valores: [Int]) -> Int {
    if let primero = valores.first {
        let resto = Array(valores.dropFirst())
        return primero + sumaValores(resto)
    } else {
        return 0
    }
}

sumaValores([1, 2, 3, 4, 5, 6, 7, 8])    // 36
```

<div class="week09-case-map"><code>first has a value</code><span>add it and recur</span><code>first is nil</code><span>the array is empty, return 0</span></div>

<!--
Idea: Connect optional absence to the recursion base case.
Say: "For a nonempty array, first unwraps the element. For an empty array, first is nil and the else branch supplies the neutral element."
Bridge: "One if can bind several optionals together."
-->

---

<div class="eyebrow">Multiple optional bindings</div>

## The body runs only when every binding succeeds

```swift
let x1: Int? = pedirNumUsuario()
let x2: Int? = pedirNumUsuario()
let x3: Int? = pedirNumUsuario()

if let dato1 = x1,
   let dato2 = x2,
   let dato3 = x3 {
    print(dato1 + dato2 + dato3)
} else {
    print("Algún dato es nil")
}
```

<div class="week09-all-bind"><code>x1 != nil</code><b>and</b><code>x2 != nil</code><b>and</b><code>x3 != nil</code></div>

<!--
Idea: Explain the conjunction implied by comma-separated bindings.
Say: "No partial set of local values reaches the body. If any optional is nil, execution moves to else."
Bridge: "Some operations can inspect an optional without unwrapping it."
-->

---

<div class="eyebrow">Optional comparison</div>

## Equality can compare the wrapped value or `nil`

```swift
var x: Int? = 10

x == 10     // true
x != nil    // true
x == 0      // false

x = nil
x == nil    // true
x == 10     // false
```

<div class="week09-note-line"><b>No unwrapping required</b><span>The comparison itself accounts for the possibility of <code>nil</code>.</span></div>

<!--
Idea: Preserve the comparison rule from the notes.
Say: "Comparison does not extract an Int for later use. It only reports whether the optional matches the compared value."
Bridge: "When absence should map to a default, question-question expresses that directly."
-->

---

<div class="eyebrow">Nil coalescing</div>

## `??` supplies a default value

```swift
let a: Int? = nil
let b: Int? = 10

let x = a ?? -1
let y = b ?? -1

print(x, y)    // -1 10
```

<div class="week09-coalescing">
  <div><code>a ?? -1</code><span>a is nil</span><b>-1</b></div>
  <div><code>b ?? -1</code><span>b contains 10</span><b>10</b></div>
</div>

<!--
Idea: Show the two branches of the operator with the same default.
Say: "The expression returns the wrapped value when present. Only nil selects the default. The result is a nonoptional Int."
Bridge: "Optional chaining instead keeps the result optional."
-->

---

<div class="eyebrow">Optional chaining</div>

## `?.` calls the method only when a value exists

```swift
let nombre1: String? = "Pedro"
let nombre2: String? = nil

let str1 = nombre1?.lowercased()
let str2 = nombre2?.lowercased()

// str1: String? = "pedro"
// str2: String? = nil
```

<div class="week09-chain-flow"><code>String?</code><span><code>?.lowercased()</code></span><code>String?</code></div>

<!--
Idea: Explain why chaining preserves optionality.
Say: "The method runs only on a present String. Because the receiver may be nil, the complete expression may also produce nil."
Bridge: "An optional can also mark the end of a recursive structure."
-->

---

<div class="eyebrow">A recursive list with an optional rest</div>

<!-- _class: compact code-small -->

## `nil` replaces the separate empty case

```swift
indirect enum Lista {
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
suma(lista: z)    // 30
```

<!--
Idea: Compare this representation conceptually with week 8's vacia case.
Say: "The recursive link has type Lista question mark. nil is the end marker, so the enum itself needs only nodo."
Bridge: "Next, closures provide compact function values for methods such as sorted."
-->

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Closure expressions

<p class="lead">Swift can write an anonymous function directly where another function expects it.</p>

<!--
Idea: Introduce the first of the two closure topics in the notes.
Say: "First we simplify an inline comparison function. Then we study how returned closures capture variables."
Bridge: "The sorted by method supplies a concrete function parameter."
-->

---

<div class="eyebrow">The sorted(by:) method</div>

## A comparison function determines the order

```swift
func sorted(
    by areInIncreasingOrder: (Element, Element) -> Bool
) -> [Element]
```

<div class="week09-sort-contract">
  <code>first element</code><code>second element</code><span>comparison returns</span><code>Bool</code>
  <b>true</b><span>means the first element appears before the second</span>
</div>

<!--
Idea: Read the function parameter before showing any closure shorthand.
Say: "The method receives a function of two elements and returns a new sorted array. The original array remains unchanged."
Bridge: "A named comparison function works, but it is verbose for one expression."
-->

---

<div class="eyebrow">Named comparison function</div>

## Reverse alphabetical order with a helper function

```swift
func primeroMayor(s1: String, s2: String) -> Bool {
    return s1 > s2
}

let estudiantes = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let alreves = estudiantes.sorted(by: primeroMayor)

// ["Peter", "Kweku", "Kofi", "Akosua", "Abena"]
```

<div class="week09-call-path"><code>primeroMayor</code><span>has type</span><code>(String, String) -> Bool</code></div>

<!--
Idea: Establish the complete named version as the baseline.
Say: "The function returns true when the first string is alphabetically greater, placing it earlier in the descending result."
Bridge: "The same function can be written inline as a closure expression."
-->

---

<div class="eyebrow">Full closure syntax</div>

## Parameters and the return type appear inside the braces

```swift
let alreves = estudiantes.sorted(by: {
    (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```

<div class="week09-closure-anatomy">
  <div><code>(s1: String, s2: String)</code><span>parameters</span></div>
  <div><code>-> Bool</code><span>return type</span></div>
  <div><code>in</code><span>separates the signature from the body</span></div>
  <div><code>return s1 > s2</code><span>body</span></div>
</div>

<!--
Idea: Present the complete closure before any simplification.
Say: "The closure has the same parameter and result types as primeroMayor, but it has no function name."
Bridge: "The surrounding method call already tells Swift those types."
-->

---

<div class="eyebrow">Closure simplification 1</div>

## Context supplies the parameter and return types

```swift
let alreves = estudiantes.sorted(by: {
    s1, s2 in
    return s1 > s2
})
```

<div class="week09-inference-source">
  <code>estudiantes</code><span>contains</span><code>String</code>
  <code>sorted(by:)</code><span>therefore expects</span><code>(String, String) -> Bool</code>
</div>

<!--
Idea: Remove only the syntax justified by contextual inference.
Say: "Swift knows the receiver is an array of String, so the comparison must accept two strings and return Bool."
Bridge: "A single-expression closure can also omit return."
-->

---

<div class="eyebrow">Closure simplification 2</div>

## A single expression has an implicit return

```swift
let alreves = estudiantes.sorted(by: {
    s1, s2 in
    s1 > s2
})
```

<div class="week09-conclusion"><code>s1 > s2</code><span>is both the body and the returned Boolean value</span></div>

<!--
Idea: Make this simplification separate from type inference.
Say: "The closure body contains one expression, so its value becomes the result without writing return."
Bridge: "Swift can also supply shorthand names for the parameters."
-->

---

<div class="eyebrow">Closure simplification 3</div>

## `$0` and `$1` replace explicit parameter names

```swift
let alreves = estudiantes.sorted(by: {
    $0 > $1
})
```

<div class="week09-argument-map">
  <div><code>$0</code><span>first String</span></div>
  <div><code>$1</code><span>second String</span></div>
</div>

<div class="week09-note-line"><b>What disappeared?</b><span>The argument list and <code>in</code> are unnecessary when shorthand names identify the parameters.</span></div>

<!--
Idea: Explain every removed token rather than presenting magic syntax.
Say: "$0 and $1 refer to the first and second closure arguments. Because they identify the arguments directly, there is no separate parameter declaration."
Bridge: "The greater-than operator already is a function of this exact type."
-->

---

<div class="eyebrow">Closure simplification 4</div>

## The operator itself satisfies the required function type

```swift
let alreves = estudiantes.sorted(by: >)
```

<div class="week09-operator-type">
  <code>&gt;</code>
  <span>selected for strings by context</span>
  <code>(String, String) -> Bool</code>
</div>

<!--
Idea: Complete the exact simplification sequence in the notes.
Say: "Swift chooses the String implementation of greater-than because sorted needs a comparison for the elements of estudiantes."
Bridge: "A final closure argument can move outside the parentheses."
-->

---

<div class="eyebrow">Trailing closures</div>

## The final closure can follow the call

<div class="week09-code-pair">
<div>
<b>With parentheses</b>

```swift
let alreves = estudiantes.sorted() {
    $0 > $1
}
```
</div>
<div>
<b>Only argument</b>

```swift
let alreves = estudiantes.sorted {
    $0 > $1
}
```
</div>
</div>

<div class="week09-conclusion"><span>The parentheses may disappear when the closure is the method's only argument.</span></div>

<!--
Idea: Show both trailing-closure forms from the notes.
Say: "The closure still belongs to sorted. Moving it after the call improves readability when the body spans several lines."
Bridge: "Closures can also retain values from the scope where they are created."
-->

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Captured variables

<p class="lead">A closure keeps access to values from its defining scope, even after that scope has returned.</p>

<!--
Idea: Introduce lexical capture before the mutable-state example.
Say: "The closure carries its code together with access to the surrounding variables it uses."
Bridge: "The incrementer captures both an increment amount and an accumulated total."
-->

---

<div class="eyebrow">Mutable captured state</div>

<!-- _class: compact code-small -->

## The returned function remembers `cantidad` and `totalAcumulado`

```swift
func construyeIncrementador(
    incremento cantidad: Int
) -> () -> Int {
    var totalAcumulado = 0

    func incrementador() -> Int {
        totalAcumulado += cantidad
        return totalAcumulado
    }

    return incrementador
}
```

<div class="week09-warning"><b>This is not a pure function</b><span>The captured <code>var</code> changes, so successive calls return different values.</span></div>

<!--
Idea: Preserve the explicit warning in the notes.
Say: "The example explains closure capture, but it uses mutable local state. The returned function therefore has a side effect on its captured variable."
Bridge: "Calls reveal that the captured state survives the outer function."
-->

---

<div class="eyebrow">State across calls</div>

## One closure continues its own accumulation

```swift
let incrementaDiez =
    construyeIncrementador(incremento: 10)

incrementaDiez()    // 10
incrementaDiez()    // 20
incrementaDiez()    // 30
```

<div class="week09-state-sequence">
  <code>0</code><span>+ 10</span><code>10</code><span>+ 10</span><code>20</code><span>+ 10</span><code>30</code>
</div>

<div class="week09-note-line"><b>After return</b><span><code>totalAcumulado</code> remains available because the closure captured it.</span></div>

<!--
Idea: Show persistence without a trace of implementation frames.
Say: "construyeIncrementador has finished, but the variable it created remains reachable through incrementaDiez."
Bridge: "A second call to the constructor creates a separate captured state."
-->

---

<div class="eyebrow">Independent closures</div>

<!-- _class: compact -->

## Each construction creates its own captured total

```swift
let incrementaDiez =
    construyeIncrementador(incremento: 10)

let incrementaSiete =
    construyeIncrementador(incremento: 7)

incrementaDiez()     // 10
incrementaDiez()     // 20
incrementaSiete()    // 7
incrementaDiez()     // 30
```

<div class="week09-two-states">
  <div><code>incrementaDiez</code><b>captured total: 30</b></div>
  <div><code>incrementaSiete</code><b>captured total: 7</b></div>
</div>

<!--
Idea: Distinguish two closure instances built from the same code.
Say: "The two closures share the definition but not the captured variable. Each constructor call creates a new totalAcumulado."
Bridge: "A closure expression can replace the nested function without changing the capture."
-->

---

<div class="eyebrow">Returning a closure expression</div>

## The anonymous closure captures the same variables

```swift
func construyeIncrementador(
    incremento cantidad: Int
) -> () -> Int {
    var totalAcumulado = 0

    return {
        totalAcumulado += cantidad
        return totalAcumulado
    }
}
```

<div class="week09-capture-list"><code>cantidad</code><span>immutable parameter</span><code>totalAcumulado</code><span>mutable local variable</span></div>

<!--
Idea: Show that named nested functions and closure expressions provide the same capture behavior.
Say: "The returned braces form an anonymous function of type empty-parameters to Int. Its free names identify the captured values."
Bridge: "Lexical scope decides which variable a captured name denotes."
-->

---

<div class="eyebrow">Lexical scope</div>

<!-- _class: compact code-small -->

## A closure uses the variable from its defining scope

```swift
func construyeFunc() -> () -> Int {
    var x = 0
    return { x += 1; return x }
}

let f = construyeFunc()
f()    // 1
f()    // 2

func usaFunc(_ f: () -> Int) -> Int {
    var x = 10
    return f()
}

usaFunc(f)    // 3
```

<div class="week09-warning"><b>Which <code>x</code>?</b><span><code>f</code> changes the captured <code>x</code>, not the local <code>x = 10</code> at the call site.</span></div>

<!--
Idea: Explain lexical scoping using the exact example from the topic.
Say: "The closure's environment was fixed where it was defined. A same-named variable in usaFunc does not replace the captured binding."
Bridge: "Assigning a closure does not copy that environment."
-->

---

<div class="eyebrow">Reference semantics</div>

## Two constants can refer to the same closure

```swift
let incrementaDiez =
    construyeIncrementador(incremento: 10)

incrementaDiez()              // 10
incrementaDiez()              // 20

let tambienIncrementaDiez = incrementaDiez
tambienIncrementaDiez()       // 30
incrementaDiez()              // 40
```

<div class="week09-shared-closure"><code>incrementaDiez</code><span>same closure and captured state</span><code>tambienIncrementaDiez</code></div>

<!--
Idea: State the reference-type consequence from the notes.
Say: "The assignment copies a reference to the closure, not a new independent total. Both names continue one captured counter."
Bridge: "Collection methods use closures without requiring mutable state."
-->

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Higher-order functions

<p class="lead"><code>map</code>, <code>filter</code>, and <code>reduce</code> accept closures that define the computation.</p>

<!--
Idea: Connect these Swift methods with the Scheme functions already studied.
Say: "Each method controls the traversal. The closure describes the operation applied during that traversal."
Bridge: "map transforms every element."
-->

---

<div class="eyebrow">map</div>

## A transformation produces one result per element

```swift
func map<T>(
    _ transform: (Element) -> T
) -> [T]
```

<div class="week09-hof-flow">
  <code>[Element]</code><span>apply <code>transform</code> to each value</span><code>[T]</code>
</div>

```swift
let numeros = [Int](0...5)
numeros.map { $0 * $0 }
// [0, 1, 4, 9, 16, 25]
```

<!--
Idea: Read map's generic signature before the example.
Say: "The result contains the same number of elements, but T may differ from Element. Here both happen to be Int."
Bridge: "The closure may also destructure or inspect a compound element."
-->

---

<div class="eyebrow">map over tuples</div>

## Each pair becomes one integer

```swift
func suma(parejas: [(Int, Int)]) -> [Int] {
    return parejas.map {
        (pareja: (Int, Int)) -> Int in
        return pareja.0 + pareja.1
    }
}

suma(parejas: [(1, 1), (2, 2), (3, 3), (4, 4)])
// [2, 4, 6, 8]
```

<div class="week09-map-pairs"><code>(1, 1)</code><code>(2, 2)</code><code>(3, 3)</code><code>(4, 4)</code><span>map</span><code>2</code><code>4</code><code>6</code><code>8</code></div>

<!--
Idea: Show a map that changes element shape from tuple to scalar.
Say: "The input element type is a pair of Int. The closure returns one Int, so the final array stores integers."
Bridge: "A mapping closure can capture a parameter from its surrounding function."
-->

---

<div class="eyebrow">map with a captured value</div>

## The closure uses `inc` for every element

```swift
func incrementa(
    valores: [Int],
    con inc: Int
) -> [Int] {
    return valores.map { $0 + inc }
}

incrementa(valores: [10, 20, 30], con: 5)
// [15, 25, 35]
```

<div class="week09-capture-list"><code>$0</code><span>current array element</span><code>inc</code><span>captured function parameter</span></div>

<!--
Idea: Use immutable capture to contrast with the mutable counter example.
Say: "The closure receives each element explicitly and captures inc implicitly. Since neither value is mutated, this transformation is pure."
Bridge: "filter keeps or discards each element instead of transforming it."
-->

---

<div class="eyebrow">filter</div>

## A predicate selects the retained elements

```swift
func filter(
    _ isIncluded: (Element) -> Bool
) -> [Element]
```

```swift
let numeros = [Int](0...10)
numeros.filter { $0 % 2 == 0 }
// [0, 2, 4, 6, 8, 10]
```

<div class="week09-filter-rule"><code>true</code><span>keep the element</span><code>false</code><span>omit the element</span></div>

<!--
Idea: Emphasize that filter preserves the element type.
Say: "The closure returns a Boolean, not a replacement value. Elements for which it returns true appear unchanged in the result."
Bridge: "reduce combines the whole collection into one accumulated result."
-->

---

<div class="eyebrow">reduce</div>

## A folding function updates one accumulated result

```swift
func reduce<Result>(
    _ initialResult: Result,
    _ nextPartialResult: (Result, Element) -> Result
) -> Result
```

<div class="week09-reduce-anatomy">
  <div><code>Result</code><span>previous accumulated result</span></div>
  <div><code>Element</code><span>next collection element</span></div>
  <div><code>Result</code><span>new accumulated result</span></div>
</div>

<!--
Idea: Relate Swift reduce to Scheme foldl as the notes do.
Say: "The accumulator starts at initialResult. The closure combines it with each element from left to right."
Bridge: "Summation is the simplest folding operation."
-->

---

<div class="eyebrow">reduce examples</div>

## The initial value fixes the starting accumulator

<div class="week09-code-pair">
<div>
<b>Sum integers</b>

```swift
let numeros = [Int](0...10)
numeros.reduce(0, +)
// 55
```
</div>
<div>
<b>Sum string lengths</b>

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]
cadenas.reduce(0) {
    $0 + $1.count
}
// 18
```
</div>
</div>

<div class="week09-note-line"><b>Argument order</b><span><code>$0</code> is the accumulated result. <code>$1</code> is the current element.</span></div>

<!--
Idea: Contrast a Result equal to Element with a Result of another type.
Say: "The second reduction consumes strings but accumulates an Int, showing why reduce has separate Result and Element types."
Bridge: "String concatenation makes the left-to-right order visible."
-->

---

<div class="eyebrow">Reduction order</div>

## `reduce` combines elements from left to right

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]

cadenas.reduce("*") {
    $0 + "-" + $1
}

// "*-Patatas-Arroz-Huevos"
```

<div class="week09-reduce-steps">
  <code>"*"</code><span>with "Patatas"</span><code>"*-Patatas"</code><span>with "Arroz"</span><code>"*-Patatas-Arroz"</code><span>with "Huevos"</span>
</div>

<!--
Idea: Use the exact order-revealing example from the topic.
Say: "At every step, the complete previous result is the first closure argument. The next array string is the second."
Bridge: "Methods that return collections can be chained."
-->

---

<div class="eyebrow">Combining higher-order functions</div>

## The output of one method becomes the next receiver

<div class="week09-pipeline">
  <div><code>[1, 2, ..., 10]</code><b>filter even</b><code>[2, 4, 6, 8, 10]</code><b>map square</b><code>[4, 16, 36, 64, 100]</code></div>
</div>

```swift
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.filter { $0 % 2 == 0 }.map { $0 * $0 }
// [4, 16, 36, 64, 100]
```

<!--
Idea: Show the intermediate collection explicitly.
Say: "filter runs first because it is the receiver closest to numeros. map then squares only the retained even values."
Bridge: "A final reduce can collapse the selected collection to one value."
-->

---

<div class="eyebrow">Filtering before reducing</div>

## Selection and accumulation remain separate operations

```swift
let numeros = [103, 2, 330, 42, 532, 6, 125]

numeros
    .filter { $0 >= 100 }
    .reduce(0, +)

// 1090
```

<div class="week09-pipeline two-step">
  <div><code>[103, 330, 532, 125]</code><b>reduce with + from 0</b><code>1090</code></div>
</div>

<!--
Idea: Preserve the second combination example from the notes.
Say: "filter expresses which elements count. reduce expresses how the retained values combine."
Bridge: "The generic signatures of these methods lead to the final topic."
-->

---

<!-- _class: section -->

<div class="eyebrow">05</div>

# Generics

<p class="lead">A generic definition uses type parameters where the algorithm does not depend on one concrete type.</p>

<!--
Idea: Introduce generics through duplicated swap functions, following the notes.
Say: "The body of swap only changes positions. It does not inspect or modify the two values, so their concrete types should not constrain the algorithm."
Bridge: "The non-generic versions expose the duplication."
-->

---

<div class="eyebrow">Duplicated definitions</div>

## The swap algorithm stays the same while types change

<div class="week09-code-pair">
<div>
<b>Int and String</b>

```swift
func intercambia(
    _ tupla: (Int, String)
) -> (String, Int) {
    return (tupla.1, tupla.0)
}
```
</div>
<div>
<b>Int and Int</b>

```swift
func intercambia(
    _ tupla: (Int, Int)
) -> (Int, Int) {
    return (tupla.1, tupla.0)
}
```
</div>
</div>

<div class="week09-conclusion"><span>Only the concrete type annotations differ.</span></div>

<!--
Idea: Show the motivation without introducing generics first.
Say: "Both bodies select component one and then component zero. Rewriting the function for every type pair repeats the same algorithm."
Bridge: "Type parameters replace those concrete types."
-->

---

<div class="eyebrow">Generic function</div>

## `A` and `B` stand for the two component types

```swift
func intercambia<A, B>(
    _ tupla: (A, B)
) -> (B, A) {
    return (tupla.1, tupla.0)
}
```

<div class="week09-generic-map">
  <div><code>(A, B)</code><span>input</span></div>
  <div><code>(B, A)</code><span>output</span></div>
</div>

<div class="week09-note-line"><b>Placeholders</b><span>The angle brackets declare type parameters. The function body works without knowing their concrete types.</span></div>

<!--
Idea: Explain the relationship between positions and type parameters.
Say: "The first returned component has type B because it came from position one. The second has type A because it came from position zero."
Bridge: "Each call determines concrete substitutions for A and B."
-->

---

<div class="eyebrow">Generic type inference</div>

## Calls instantiate the same definition with different types

<div class="week09-generic-examples">
  <div><code>intercambia((10, "Hola"))</code><span><code>A = Int</code> · <code>B = String</code></span><b>("Hola", 10)</b></div>
  <div><code>intercambia((10, 20))</code><span><code>A = Int</code> · <code>B = Int</code></span><b>(20, 10)</b></div>
  <div><code>intercambia((true, 10.5))</code><span><code>A = Bool</code> · <code>B = Double</code></span><b>(10.5, true)</b></div>
</div>

<!--
Idea: Make inference concrete for all three examples in the topic.
Say: "The compiler derives A and B independently at each call. The generic source definition does not change."
Bridge: "Enums can also take a generic type parameter."
-->

---

<div class="eyebrow">Generic recursive list</div>

## One enum represents lists of any element type

```swift
indirect enum Lista<T> {
    case vacia
    case nodo(T, Lista<T>)
}
```

<div class="week09-list-types">
  <div><code>Lista&lt;Int&gt;</code><span><code>.nodo(20, ...)</code></span></div>
  <div><code>Lista&lt;String&gt;</code><span><code>.nodo("A", ...)</code></span></div>
</div>

<div class="week09-warning"><b>One list, one element type</b><span>The same <code>T</code> appears in every node of a particular list.</span></div>

<!--
Idea: Generalize week 8's Int-only recursive enum.
Say: "T replaces Int in the node payload and reappears in the recursive rest. A concrete list therefore uses one consistent element type throughout."
Bridge: "Selectors use the same type parameter and return optionals for the empty case."
-->

---

<div class="eyebrow">Generic selectors</div>

## Empty lists make `first` and `rest` optional

<div class="columns equal">
<div>

```swift
func first<T>(_ lista: Lista<T>) -> T? {
    switch lista {
    case let .nodo(primero, _):
        return primero
    case .vacia:
        return nil
    }
}
```

</div>
<div>

```swift
func rest<T>(
    _ lista: Lista<T>
) -> Lista<T>? {
    switch lista {
    case let .nodo(_, resto):
        return resto
    case .vacia:
        return nil
    }
}
```

</div>
</div>

<!--
Idea: Join generics, recursive enums, pattern matching, and optionals.
Say: "For a node, first returns T and rest returns Lista of T. For vacia, neither value exists, so both result types are optional."
Bridge: "The same functions work for integer and string lists."
-->

---

<div class="eyebrow">One implementation, several list types</div>

## The generic operations preserve each element type

```swift
let lista: Lista =
    .nodo(20, .nodo(30, .nodo(40, .vacia)))

let lista2: Lista =
    .nodo("A", .nodo("B", .nodo("C", .vacia)))

first(rest(lista)!)!      // 30
first(rest(lista2)!)!     // "B"
```

<div class="week09-result-row">
  <div><code>Lista&lt;Int&gt;</code><b>30</b></div>
  <div><code>Lista&lt;String&gt;</code><b>"B"</b></div>
</div>

<!--
Idea: Close the example exactly where the notes close it.
Say: "Type inference specializes Lista and the generic selectors at each declaration. Forced unwraps are safe for these known nonempty examples, although optional binding would be safer for unknown input."
Bridge: "Stop here. These generic list operations prepare the object-oriented Swift material that follows."
-->
