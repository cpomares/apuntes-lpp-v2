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
<div class="week-marker">Week 11</div>

# Object-oriented programming with Swift II

<p class="lead">Topic 6 · Operators, protocols, type casting, generics, and extensions</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Continue directly from the class and structure mechanisms in week 10.
Say: "This week studies how Swift gives types common interfaces, discovers run-time types, abstracts over element types, and adds functionality after a type is defined."
Bridge: "Operator functions provide the first example of type-specific behavior."
-->

---

<div class="eyebrow">Today</div>

## Five extensions of Swift types

<div class="sequence week11-roadmap">
  <div><b>1 · OPERATORS</b><span>Define existing operators for our own types</span></div>
  <div><b>2 · PROTOCOLS</b><span>Express requirements shared by unrelated types</span></div>
  <div><b>3 · TYPE CASTING</b><span>Inspect and recover a concrete run-time type</span></div>
  <div><b>4 · GENERICS</b><span>Parameterize a definition by a type</span></div>
  <div><b>5 · EXTENSIONS</b><span>Add computed properties, initializers, methods, and subscripts</span></div>
</div>

<!--
Idea: Preserve the five sections and their order from the class notes.
Say: "Protocols connect several later ideas. They act as types, constrain generics, and can receive shared behavior through extensions."
Bridge: "We begin with operator overloading."
-->

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Operator functions

<p class="lead">A class or structure can define how an existing Swift operator works for its values.</p>

<!--
Idea: Define overloading without implying that arbitrary operator symbols are introduced here.
Say: "The operator keeps its familiar syntax, while a static function supplies behavior for a particular type."
Bridge: "Vector addition is the central example."
-->

---

<div class="eyebrow">Binary operator</div>

## A static function defines `+` for two vectors

```swift
struct Vector2D {
    var x = 0.0
    var y = 0.0

    static func + (
        left: Vector2D,
        right: Vector2D
    ) -> Vector2D {
        return Vector2D(
            x: left.x + right.x,
            y: left.y + right.y
        )
    }
}
```

<div class="week11-operator-signature"><code>Vector2D</code><b>+</b><code>Vector2D</code><span>returns</span><code>Vector2D</code></div>

<!--
Idea: Show that the operator's parameter and result types define its meaning.
Say: "The function is static because it belongs to the type. Its two parameters correspond to the left and right operands."
Bridge: "The call then uses normal infix syntax."
-->

---

<div class="eyebrow">Infix use</div>

## The operator call constructs a new vector

```swift
let a = Vector2D(x: 3, y: 1)
let b = Vector2D(x: 2, y: 4)

let sum = a + b
// Vector2D(x: 5, y: 5)
```

<div class="week11-vector-add">
  <div><code>a</code><b>(3, 1)</b></div>
  <strong>+</strong>
  <div><code>b</code><b>(2, 4)</b></div>
  <strong>=</strong>
  <div><code>sum</code><b>(5, 5)</b></div>
</div>

<div class="week11-note-line"><b>No mutation</b><span>The function returns a third value. The two operands remain unchanged.</span></div>

<!--
Idea: Connect operator overloading to the value semantics of structures.
Say: "Addition reads the two vectors and returns a new Vector2D. It does not modify either operand."
Bridge: "Unary operators use one operand and declare their position."
-->

---

<div class="eyebrow">Prefix operator</div>

## `prefix` places a unary operator before its operand

```swift
extension Vector2D {
    static prefix func - (vector: Vector2D) -> Vector2D {
        return Vector2D(x: -vector.x, y: -vector.y)
    }
}

let positive = Vector2D(x: 3, y: 4)
let negative = -positive
// Vector2D(x: -3, y: -4)

let positiveAgain = -negative
// Vector2D(x: 3, y: 4)
```

<div class="week11-note-line"><b>Unary shape</b><span>One operand enters and one value returns. <code>prefix</code> distinguishes <code>-value</code> from a postfix operator.</span></div>

<!--
Idea: Make prefix syntax and double negation explicit.
Say: "The operator negates both components. Applying the same operation twice restores the original vector."
Bridge: "Operators describe one type. Protocols describe a capability that many types can share."
-->

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Protocols

<p class="lead">A protocol states requirements. A conforming type supplies implementations that satisfy them.</p>

<!--
Idea: Separate declaration of a capability from implementation.
Say: "A protocol does not decide how a type stores its state. It specifies the interface that clients may rely on."
Bridge: "The conformance declaration appears after a colon."
-->

---

<div class="eyebrow">Protocol syntax</div>

## A type lists the protocols it conforms to

```swift
protocol FirstProtocol {
    // requirements
}

protocol AnotherProtocol {
    // requirements
}

struct AStructure: FirstProtocol, AnotherProtocol {
    // implementations
}

class AClass: Superclass, FirstProtocol, AnotherProtocol {
    // implementations
}
```

<div class="week11-note-line"><b>Order for a class</b><span>The superclass comes first, followed by protocols.</span></div>

<!--
Idea: Establish the declaration grammar before discussing requirements.
Say: "Structures and enums list protocols directly. A class places its single superclass before any protocol conformances."
Bridge: "A protocol can require readable or writable properties."
-->

---

<div class="eyebrow">Property requirements</div>

## `{ get }` requires reading, while `{ get set }` also requires writing

```swift
protocol HasConfiguration {
    var identifier: String { get }
    var enabled: Bool { get set }
    static var defaultEnabled: Bool { get }
}
```

<div class="week11-property-requirements">
  <div><code>identifier</code><span>must be readable</span></div>
  <div><code>enabled</code><span>must be readable and writable</span></div>
  <div><code>defaultEnabled</code><span>belongs to the conforming type</span></div>
</div>

<!--
Idea: Explain what the protocol does and does not specify.
Say: "The protocol names the property and its access level. It does not say whether the conforming type stores or computes it."
Bridge: "Two unrelated representations can therefore meet the same requirement."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">One property requirement</div>

## Stored and computed properties can both satisfy `{ get }`

<div class="columns equal">
<div>

```swift
protocol HasName {
    var fullName: String { get }
}

struct Person: HasName {
    var age: Int
    var fullName: String
}
```

<div class="week11-conformance-label"><b>STORED</b><span>Person stores the full name directly</span></div>
</div>
<div>

```swift
class Starship: HasName {
    var prefix: String?
    var name: String

    init(prefix: String? = nil, name: String) {
        self.prefix = prefix
        self.name = name
    }

    var fullName: String {
        (prefix.map { $0 + " " } ?? "") + name
    }
}
```

<div class="week11-conformance-label"><b>COMPUTED</b><span>Starship derives the full name</span></div>
</div>
</div>

<!--
Idea: Use the same pair from the notes to show representation independence.
Say: "Clients of HasName only know that fullName can be read. They need not know whether the value is stored or calculated."
Bridge: "That protocol name can itself appear as a variable type."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">Protocol as a type</div>

## One variable can hold any value that conforms

```swift
let enterprise = Starship(
    prefix: "USS",
    name: "Enterprise"
)

let john = Person(
    age: 35,
    fullName: "John Appleseed"
)

var named: any HasName = enterprise
named.fullName                 // "USS Enterprise"

named = john
named.fullName                 // "John Appleseed"
```

<div class="week11-protocol-view"><code>Starship</code><code>Person</code><span>viewed through</span><code>any HasName</code></div>

<!--
Idea: Explain the protocol-typed view as a guaranteed interface.
Say: "The concrete value may change from Starship to Person. The keyword any makes explicit that the variable stores some value whose concrete type conforms to HasName."
Bridge: "That promise also limits what clients may access."
-->

---

<!-- _class: compact -->

<div class="eyebrow">The protocol view</div>

## A protocol-typed variable exposes only protocol requirements

```swift
var named: any HasName = john

print(named.fullName)    // valid
print(named.age)         // compile-time error
```

<div class="week11-access-view">
  <div><b>VISIBLE</b><code>fullName</code><span>declared by HasName</span></div>
  <div><b>HIDDEN BY THIS TYPE</b><code>age</code><span>belongs to Person, not HasName</span></div>
</div>

<div class="week11-note-line"><b>The value is still a Person</b><span>The static type of <code>named</code> determines which members this expression may use.</span></div>

<!--
Idea: Avoid suggesting that the underlying property disappears.
Say: "The object still contains its age. The compiler only allows operations guaranteed by the variable's declared protocol type."
Bridge: "Protocols can require methods in the same way."
-->

---

<div class="eyebrow">Method requirements</div>

## A protocol declares a method signature without a body

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}
```

<div class="week11-contract">
  <div><b>INPUT</b><span>no arguments</span></div>
  <div><b>REQUIREMENT</b><code>random()</code></div>
  <div><b>OUTPUT</b><code>Double</code></div>
</div>

<div class="week11-note-line"><b>Protocol guarantee</b><span>Every conforming type provides a callable method with this signature.</span></div>

<!--
Idea: Frame a protocol requirement as a contract that client code can use.
Say: "The protocol does not specify the algorithm. It guarantees only that a Double-producing random method exists."
Bridge: "A predictable fake implementation is useful for testing."
-->

---

<div class="eyebrow">A conforming fake</div>

## The fake generator cycles through known values

```swift
class FakeRandomGenerator: RandomNumberGenerator {
    private var numbers = [0.2, 0.5, 0.8]
    private var index = 0

    func random() -> Double {
        let result = numbers[index]
        index = (index + 1) % numbers.count
        return result
    }
}

let generator = FakeRandomGenerator()
generator.random()    // 0.2
generator.random()    // 0.5
generator.random()    // 0.8
generator.random()    // 0.2
```

<!--
Idea: Explain why deterministic behavior is valuable rather than treating it as bad randomness.
Say: "The implementation is deliberately predictable. A test can know exactly which values a client will receive."
Bridge: "A protocol method that changes a value type must state that intention."
-->

---

<!-- _class: compact code-small dense -->

<div class="eyebrow">Mutating requirement</div>

## `mutating` lets structures and enums satisfy a state-changing method

```swift
protocol Toggleable {
    mutating func toggle()
}

enum Switch: Toggleable {
    case off, on

    mutating func toggle() {
        switch self {
        case .off: self = .on
        case .on:  self = .off
        }
    }
}

var lamp = Switch.off
lamp.toggle()    // on
```

<div class="week11-note-line"><b>Classes</b><span>They omit <code>mutating</code>: their methods already operate through a reference.</span></div>

<!--
Idea: Connect protocol syntax to value-type mutation from week 10.
Say: "The requirement must allow a conforming value type to replace or modify self. A class does not need the keyword in its implementation."
Bridge: "A client can depend on the protocol instead of a concrete generator class."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">Dependency on a protocol</div>

## `Die` accepts any random generator implementation

```swift
class Die {
    let sides: Int
    let generator: any RandomNumberGenerator

    init(sides: Int, generator: any RandomNumberGenerator) {
        self.sides = sides
        self.generator = generator
    }

    func roll() -> Int {
        Int(generator.random() * Double(sides)) + 1
    }
}
```

<div class="week11-dependency"><code>Die</code><span>depends on</span><code>RandomNumberGenerator</code><span>implemented by many concrete types</span></div>

<!--
Idea: Show the design benefit before running the example.
Say: "Die knows the operation it needs, not the class that supplies it. Any conforming implementation can be injected through the initializer."
Bridge: "The deterministic fake makes the die easy to test."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Testing through a protocol</div>

## Replacing the implementation does not change `Die`

```swift
let testDie = Die(
    sides: 6,
    generator: FakeRandomGenerator()
)

testDie.roll()    // 2
testDie.roll()    // 4
testDie.roll()    // 5
testDie.roll()    // 2
```

<div class="week11-generator-swap">
  <div><code>FakeRandomGenerator</code><span>predictable tests</span></div>
  <div><code>LinearCongruentialGenerator</code><span>production implementation</span></div>
  <b>same Die class</b>
</div>

<!--
Idea: Make substitutability concrete.
Say: "The protocol keeps Die independent of one random algorithm. A test uses the fake. A different conforming generator can be supplied later without editing Die."
Bridge: "The same protocol type can also describe every element in a collection."
-->

---

<div class="eyebrow">Collections of protocol values</div>

## One array can store unrelated types through a shared protocol

```swift
let peter = Person(age: 24, fullName: "Peter Parker")
let enterprise = Starship(prefix: "USS", name: "Enterprise")

let namedThings: [any HasName] = [peter, enterprise]

for item in namedThings {
    print(item.fullName)
}
```

<div class="week11-collection-types">
  <div><code>Person</code><span>Peter Parker</span></div>
  <div><code>Starship</code><span>USS Enterprise</span></div>
  <strong>[any HasName]</strong>
</div>

<!--
Idea: Distinguish the concrete elements from the element type visible in the loop.
Say: "The elements retain their concrete values, but item has the existential type any HasName. The loop can therefore read fullName from every element."
Bridge: "Swift's standard library defines important protocols such as Equatable."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">`Equatable` for a class</div>

## A class supplies its definition of value equality

```swift
class Point3D: Equatable {
    let x: Double
    let y: Double
    let z: Double

    init(x: Double, y: Double, z: Double) {
        self.x = x
        self.y = y
        self.z = z
    }

    static func == (left: Point3D, right: Point3D) -> Bool {
        left.x == right.x &&
        left.y == right.y &&
        left.z == right.z
    }
}
```

<div class="week11-note-line"><b>Equality, not identity</b><span>Two distinct Point3D instances can compare equal when their coordinates match.</span></div>

<!--
Idea: Reconnect Equatable to week 10's distinction between == and ===.
Say: "The class chooses a value-level equality rule. Swift already provides != from the Equatable conformance."
Bridge: "For many structures, the compiler can synthesize equality."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Synthesized equality</div>

## A structure gets `==` when all stored properties are `Equatable`

```swift
struct Point3D: Equatable {
    let x: Double
    let y: Double
    let z: Double
}

let p1 = Point3D(x: 0, y: 0, z: 0)
let p2 = Point3D(x: 0, y: 0, z: 0)

p1 == p2    // true
p1 != p2    // false
```

<div class="week11-synthesis"><code>Double is Equatable</code><span>all three properties qualify</span><code>Point3D equality is synthesized</code></div>

<!--
Idea: State the condition for synthesis, not merely the result.
Say: "Swift compares corresponding stored properties because every one of their types already supports equality."
Bridge: "Protocols can refine other protocols."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Protocol inheritance</div>

## A refined protocol includes inherited requirements

```swift
protocol Book {
    var title: String { get }
    var author: String { get }
}

protocol LendableBook: Book {
    var isOnLoan: Bool { get set }
    mutating func lend()
    mutating func returnBook()
}
```

<div class="week11-protocol-inheritance">
  <div><code>Book</code><span>title · author</span></div>
  <div><code>LendableBook</code><span>all Book requirements · loan state · operations</span></div>
</div>

<!--
Idea: Describe protocol inheritance as requirement accumulation.
Say: "Anything that conforms to LendableBook must also satisfy Book. The refined protocol adds mutable loan state and two operations."
Bridge: "Comparable provides a standard-library example."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">`Comparable` refines `Equatable`</div>

## Defining `<` lets Swift derive the remaining comparisons

```swift
struct ScreenCoord: Comparable {
    var x: Int
    var y: Int

    static func < (left: ScreenCoord, right: ScreenCoord) -> Bool {
        left.x < right.x ||
        (left.x == right.x && left.y < right.y)
    }
}

let a = ScreenCoord(x: 0, y: 0)
let b = ScreenCoord(x: 10, y: 10)

a < b     // true
a > b     // false
```

<div class="week11-note-line"><b>Generated behavior</b><span>Swift synthesizes <code>==</code> for the structure and derives <code>&gt;</code>, <code>&lt;=</code>, and <code>&gt;=</code> from the conformance.</span></div>

<!--
Idea: Show how one declared ordering relation supports the full comparison family.
Say: "The implementation orders by x first and uses y to break a tie. Comparable already requires Equatable."
Bridge: "Protocol-typed and superclass-typed values sometimes need their concrete type recovered."
-->

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Type casting

<p class="lead">The operators <code>is</code> and <code>as?</code> inspect a value's run-time type without changing the underlying object.</p>

<!--
Idea: Define checking and conditional casting together.
Say: "A variable can have a superclass or protocol type while containing a more specific value. Type casting lets code discover that specific type when necessary."
Bridge: "We begin with a small class hierarchy."
-->

---

<div class="eyebrow">Media hierarchy</div>

## Two subclasses add different information to one base class

```swift
class MediaItem {
    var name: String
    init(name: String) { self.name = name }
}

class Movie: MediaItem {
    var director: String
    init(name: String, director: String) {
        self.director = director
        super.init(name: name)
    }
}

class Song: MediaItem {
    var artist: String
    init(name: String, artist: String) {
        self.artist = artist
        super.init(name: name)
    }
}
```

<div class="week11-hierarchy"><code>MediaItem</code><code>Movie</code><code>Song</code></div>

<!--
Idea: Establish which properties require a more specific type.
Say: "Every element has a name. Only a Movie has a director, and only a Song has an artist."
Bridge: "A library can store both through the common superclass."
-->

---

<div class="eyebrow">Heterogeneous collection</div>

## The array exposes `MediaItem`, while each object keeps its concrete type

```swift
let library: [MediaItem] = [
    Movie(name: "The Lord of the Rings", director: "Peter Jackson"),
    Song(name: "Child in Time", artist: "Deep Purple"),
    Movie(name: "Bridge of Spies", director: "Steven Spielberg"),
    Song(name: "Wish You Were Here", artist: "Pink Floyd")
]
```

<div class="week11-static-runtime">
  <div><b>STATIC ELEMENT TYPE</b><code>MediaItem</code><span>what the loop can use directly</span></div>
  <div><b>RUN-TIME TYPES</b><code>Movie · Song</code><span>the concrete objects still stored</span></div>
</div>

<!--
Idea: Keep static and run-time type visually separate.
Say: "When we iterate, item has type MediaItem. The object itself remains a Movie or Song, which casting can reveal."
Bridge: "The is operator answers a yes-or-no type question."
-->

---

<div class="eyebrow">Type checking</div>

## `is` tests the concrete type without producing a converted value

```swift
var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}
```

<div class="week11-counts"><code>Movie</code><b>2</b><code>Song</code><b>2</b></div>

<div class="week11-note-line"><b>Result type</b><span>Each <code>is</code> expression returns a Boolean.</span></div>

<!--
Idea: Explain that is does not expose subclass-only properties.
Say: "The test can count types, but item still has static type MediaItem. To read director or artist, we need a downcast."
Bridge: "A conditional downcast returns an optional."
-->

---

<div class="eyebrow">Conditional downcast</div>

## `as?` returns the requested type or `nil`

<div class="week11-cast-results">
  <div><code>item as? Movie</code><span>when item is a Movie</span><b>Movie?</b><strong>present</strong></div>
  <div><code>item as? Movie</code><span>when item is a Song</span><b>Movie?</b><strong>nil</strong></div>
</div>

```swift
if let movie = item as? Movie {
    print(movie.director)
}
```

<div class="week11-note-line"><b>Safe failure</b><span>Optional binding enters the body only when the downcast succeeds.</span></div>

<!--
Idea: Connect as? to the optional model from week 9.
Say: "The operation cannot promise that every MediaItem is a Movie, so its result is Movie optional. if let unwraps only a successful cast."
Bridge: "The library loop can try both concrete subclasses."
-->

---

<div class="eyebrow">Downcasting in a loop</div>

## Each successful cast exposes subclass-specific properties

```swift
for item in library {
    if let movie = item as? Movie {
        print("Movie: \(movie.name), dir. \(movie.director)")
    } else if let song = item as? Song {
        print("Song: \(song.name), by \(song.artist)")
    }
}
```

<div class="week11-member-access">
  <div><code>movie</code><span>name + director</span></div>
  <div><code>song</code><span>name + artist</span></div>
</div>

<!--
Idea: Show why the cast is needed through the members gained.
Say: "After the Movie cast, the compiler permits director. After the Song cast, it permits artist. The common name property was already available."
Bridge: "Pattern matching can express the same cases."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Casting with `switch`</div>

## Type patterns bind a value of the matched type

```swift
for item in library {
    switch item {
    case let movie as Movie:
        print("Movie: \(movie.name), dir. \(movie.director)")

    case let song as Song:
        print("Song: \(song.name), by \(song.artist)")

    default:
        break
    }
}
```

<div class="week11-note-line"><b>Same operation</b><span>Each matching case performs a downcast and binds the concrete value.</span></div>

<!--
Idea: Present switch as an alternative organization, not a new casting rule.
Say: "The as pattern tests and binds in one case. A default remains necessary because MediaItem may have other subclasses or direct instances."
Bridge: "Any removes even the common superclass restriction."
-->

---

<div class="eyebrow">The `Any` type</div>

## `[Any]` can hold values with unrelated types

```swift
var values = [Any]()

values.append(0)
values.append(3.14159)
values.append("hello")
values.append((3.0, 5.0))
values.append(Movie(name: "Ghostbusters", director: "Ivan Reitman"))
values.append({ (name: String) in "Hello, \(name)" })
```

<div class="week11-any-types"><code>Int</code><code>Double</code><code>String</code><code>(Double, Double)</code><code>Movie</code><code>(String) -> String</code></div>

<!--
Idea: Show the breadth of Any, including a function value.
Say: "Any places no shared protocol or superclass requirement on these values. That flexibility means clients must inspect types before using type-specific operations."
Bridge: "A switch can combine value and type patterns."
-->

---

<!-- _class: compact code-small dense -->

<div class="eyebrow">Inspecting `Any`</div>

## A `switch` can distinguish values, types, tuples, and functions

```swift
for value in values {
    switch value {
    case 0 as Int:
        print("zero as Int")
    case let number as Double where number > 0:
        print("positive Double: \(number)")
    case let text as String:
        print("String: \(text)")
    case let (x, y) as (Double, Double):
        print("point: \(x), \(y)")
    case let movie as Movie:
        print("movie: \(movie.name)")
    case let greeting as (String) -> String:
        print(greeting("Michael"))
    default:
        print("another value")
    }
}
```

<!--
Idea: Keep the example complete while using compact code styling.
Say: "The pattern selects a concrete interpretation for each value. The where clause adds a value condition after a successful Double cast."
Bridge: "Casting may also target a protocol rather than a class."
-->

---

<div class="eyebrow">Casting to a protocol</div>

## `as?` can ask whether an unrelated value has a capability

```swift
protocol HasArea {
    var area: Double { get }
}

class Circle: HasArea {
    var radius: Double
    var area: Double { .pi * radius * radius }
    init(radius: Double) { self.radius = radius }
}

class Country: HasArea {
    var area: Double
    init(area: Double) { self.area = area }
}

class Animal {
    var legs: Int
    init(legs: Int) { self.legs = legs }
}
```

<!--
Idea: Establish that conformance, not inheritance, creates the shared relation.
Say: "Circle and Country have no common application superclass, but both promise an area. Animal does not."
Bridge: "The cast exposes the shared property only for conforming objects."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">Protocol conformance at run time</div>

## A successful cast gives a protocol-typed view

```swift
let objects: [Any] = [
    Circle(radius: 2),
    Country(area: 243_610),
    Animal(legs: 4)
]

for object in objects {
    if let objectWithArea = object as? any HasArea {
        print("Area: \(objectWithArea.area)")
    } else {
        print("No area")
    }
}
```

<div class="week11-area-results"><code>Circle</code><b>12.566...</b><code>Country</code><b>243610</b><code>Animal</code><b>No area</b></div>

<!--
Idea: State that the object itself is not converted into a different representation.
Say: "The Circle remains a Circle and the Country remains a Country. objectWithArea is a view that exposes only the HasArea requirement."
Bridge: "Generics solve a compile-time abstraction problem instead."
-->

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Generics

<p class="lead">A generic definition uses a type parameter that becomes a concrete type when the definition is used.</p>

<!--
Idea: Contrast generics with Any and run-time casting.
Say: "Any erases specific static information and may need casting later. Generics preserve one consistent concrete type throughout each use."
Bridge: "A stack shows why that matters."
-->

---

<div class="eyebrow">The non-generic limitation</div>

## `IntStack` repeats an implementation for one element type

```swift
struct IntStack {
    var items = [Int]()

    mutating func push(_ item: Int) {
        items.append(item)
    }

    mutating func pop() -> Int {
        items.removeLast()
    }
}
```

<div class="week11-note-line"><b>Limitation</b><span>A string stack would need another structure with the same algorithm and different types.</span></div>

<!--
Idea: Identify duplicated type-specific syntax as the motivation.
Say: "The storage and both method signatures hard-code Int. The stack algorithm itself does not depend on integer operations."
Bridge: "A type parameter replaces those three occurrences."
-->

---

<div class="eyebrow">Generic structure</div>

## `Element` keeps storage, input, and output consistent

```swift
struct Stack<Element> {
    var items = [Element]()

    mutating func push(_ item: Element) {
        items.append(item)
    }

    mutating func pop() -> Element {
        items.removeLast()
    }
}
```

<div class="week11-generic-consistency">
  <code>[Element]</code><span>stores</span><code>Element</code><span>and returns</span><code>Element</code>
</div>

<!--
Idea: Explain the repeated type parameter as a type relation.
Say: "Element is not Any. For one Stack value it stands for one concrete type, and the compiler enforces that type everywhere."
Bridge: "Creating a Stack supplies the concrete element type."
-->

---

<div class="eyebrow">Instantiating a generic type</div>

## `Stack<String>` specializes the generic definition

```swift
var words = Stack<String>()

words.push("one")
words.push("two")
words.push("three")
words.push("four")

let top = words.pop()
// "four"
```

<div class="week11-stack-view">
  <div><code>bottom</code><span>one</span></div>
  <div><span>two</span></div>
  <div><span>three</span></div>
  <div class="top"><code>top</code><span>four</span></div>
</div>

<!--
Idea: Make LIFO behavior visible alongside specialization.
Say: "The concrete type String replaces Element in the array and both methods. pop removes the last value pushed."
Bridge: "Some generic algorithms require operations that not every type provides."
-->

---

<div class="eyebrow">An unconstrained type parameter</div>

## A generic `T` does not guarantee that `==` exists

```swift
func findIndex<T>(of target: T, in array: [T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == target {
            return index
        }
    }
    return nil
}
```

<div class="week11-compile-error"><code>error: binary operator '==' cannot be applied to two 'T' operands</code></div>

<div class="week11-note-line"><b>Reason</b><span>The declaration promises to work for every possible <code>T</code>, including types with no equality operation.</span></div>

<!--
Idea: Explain the compiler error as a broken generic promise.
Say: "The function body uses a capability that the signature never required. The compiler cannot assume arbitrary values support equality."
Bridge: "A protocol constraint adds the missing guarantee."
-->

---

<!-- _class: compact code-small dense -->

<div class="eyebrow">Generic constraint</div>

## `T: Equatable` makes the equality operation valid

```swift
func findIndex<T: Equatable>(
    of target: T,
    in array: [T]
) -> Int? {
    for (index, value) in array.enumerated() {
        if value == target {
            return index
        }
    }
    return nil
}

findIndex(of: 9.3, in: [3.14, 0.1, 9.3])    // 2
findIndex(of: "cat", in: ["dog", "cat"])  // 1
```

<div class="week11-note-line"><b>Compile-time contract</b><span>The function accepts any one type that conforms to <code>Equatable</code>.</span></div>

<!--
Idea: Show that the constraint adds a capability without choosing one concrete type.
Say: "Double and String both satisfy the requirement, so one implementation works for both. The array and target still share the same T in each call."
Bridge: "A generic function may introduce more than one constrained type parameter."
-->

---

<!-- _class: compact code-small dense ultra-dense -->

<div class="eyebrow">Multiple constrained parameters</div>

## Each type parameter can state a different requirement

```swift
class Animal {
    let name: String
    init(_ name: String) { self.name = name }
}

protocol SoundEmitter { func emitSound() -> String }

func playSound<T: Animal, U: SoundEmitter>(
    animal: T, emitter: U
) {
    print("\(animal.name) makes: \(emitter.emitSound())")
}

class Dog: Animal {}
struct Whistle: SoundEmitter {
    func emitSound() -> String { "whistle" }
}

playSound(animal: Dog("Fido"), emitter: Whistle())
```

<div class="week11-constraints"><code>T: Animal</code><span>class inheritance constraint</span><code>U: SoundEmitter</code><span>protocol conformance constraint</span></div>

<!--
Idea: Correct the inconsistent names in the translated notes while preserving the example.
Say: "T must be Animal or a subclass. U may be any type that supplies emitSound through the protocol. The two parameters remain independent."
Bridge: "Extensions add functionality to an already declared type."
-->

---

<!-- _class: section -->

<div class="eyebrow">05</div>

# Extensions

<p class="lead">An extension adds functionality without editing the original type declaration.</p>

<!--
Idea: Define retroactive modeling in plain language.
Say: "The type must already exist, but we may add computed properties, initializers, methods, and subscripts even when we do not own its source code."
Bridge: "The extension syntax names the existing type."
-->

---

<div class="eyebrow">Extension syntax</div>

## `extension` reopens an existing type for new functionality

```swift
extension ExistingType {
    // computed properties
    // initializers
    // instance and type methods
    // subscripts
}
```

<div class="week11-extension-limits">
  <div><b>CAN ADD</b><span>computed behavior and new operations</span></div>
  <div><b>CANNOT ADD</b><span>new stored properties to an existing type</span></div>
</div>

<!--
Idea: Include the important storage limitation so the capability is not overstated.
Say: "An extension can derive new information and provide new behavior. It cannot change the stored instance layout by adding stored properties."
Bridge: "A computed property is the simplest example."
-->

---

<div class="eyebrow">Computed property extension</div>

## An extension can derive a new view of existing state

```swift
struct Person: HasName {
    var age: Int
    var fullName: String
}

extension Person {
    var isAdult: Bool {
        age >= 18
    }
}

let lucia = Person(age: 15, fullName: "Lucía")
lucia.isAdult    // false
```

<div class="week11-note-line"><b>No extra storage</b><span><code>isAdult</code> calculates its result from the existing <code>age</code> property.</span></div>

<!--
Idea: Show why a computed property fits the extension restriction.
Say: "The extension does not store another Boolean. It computes adulthood whenever the property is read."
Bridge: "An extension can also add another construction path."
-->

---

<!-- _class: compact code-small dense ultra-dense -->

<div class="eyebrow">Initializer extension</div>

## A new initializer can delegate to an existing memberwise initializer

```swift
struct Size {
    var width = 0.0, height = 0.0
}

struct Point {
    var x = 0.0, y = 0.0
}

struct Rectangle {
    var origin = Point()
    var size = Size()
}

extension Rectangle {
    init(center: Point, size: Size) {
        let x = center.x - size.width / 2
        let y = center.y - size.height / 2
        self.init(origin: Point(x: x, y: y), size: size)
    }
}
```

<div class="week11-note-line"><b>Preserved synthesis</b><span>Keeping the custom initializer in an extension leaves the structure's memberwise initializer available.</span></div>

<!--
Idea: Highlight a useful Swift-specific reason to place the initializer in an extension.
Say: "The extension adds center-based construction and delegates the actual stored values to the memberwise initializer."
Bridge: "Standard library types can receive new methods in the same way."
-->

---

<div class="eyebrow">Extending `Int`</div>

## A method can execute a closure `self` times

```swift
extension Int {
    func repetitions(_ task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}

3.repetitions({
    print("Hello!")
})
```

<div class="week11-repetitions"><code>3</code><span>calls task</span><b>Hello!</b><b>Hello!</b><b>Hello!</b></div>

<!--
Idea: Connect the extension with closures from week 9.
Say: "The receiver supplies the repetition count. The parameter is a closure with no arguments and no return value."
Bridge: "Trailing closure syntax makes the call read more naturally."
-->

---

<div class="eyebrow">Trailing closure call</div>

## The closure may follow the parentheses

```swift
3.repetitions {
    print("Goodbye!")
}
```

<div class="week11-call-anatomy"><code>3</code><span>receiver</span><code>repetitions</code><span>method</span><code>{ ... }</code><span>task closure</span></div>

<div class="week11-note-line"><b>Same method</b><span>Only the call syntax changes. The closure still has type <code>() -&gt; Void</code>.</span></div>

<!--
Idea: Reinforce the closure syntax sequence from week 9.
Say: "Because the closure is the final argument, Swift permits it after the method call."
Bridge: "A String extension can hide the details of String.Index."
-->

---

<div class="eyebrow">String indexing</div>

## A character position must first become a `String.Index`

```swift
let text = "Hello"
let position = 2

let index = text.index(
    text.startIndex,
    offsetBy: position
)

text[index]    // "l"
```

<div class="week11-index-types"><code>Int position</code><span>converted with index(_:offsetBy:)</span><code>String.Index</code><span>used by String subscript</span></div>

<!--
Idea: Avoid implying that String indices are integers.
Say: "Swift strings handle extended grapheme clusters, so their native index type is not Int. The conversion starts from startIndex and advances by a character offset."
Bridge: "An extension can package this conversion in a method."
-->

---

<div class="eyebrow">A convenience method</div>

## `at(_:)` converts the integer position internally

```swift
extension String {
    func at(_ position: Int) -> Character {
        let index = self.index(
            self.startIndex,
            offsetBy: position
        )
        return self[index]
    }
}

"Hello".at(3)    // "l"
```

<div class="week11-note-line"><b>Precondition</b><span>The position must lie within the string's valid character range.</span></div>

<!--
Idea: Keep the extension faithful while stating its boundary condition.
Say: "The method simplifies the successful case. It does not make an out-of-range position safe, so callers still need a valid offset."
Bridge: "A custom subscript can offer bracket notation for the same operation."
-->

---

<!-- _class: compact -->

<div class="eyebrow">A custom subscript</div>

## `subscript` defines bracket access for an integer position

```swift
extension String {
    subscript(position: Int) -> Character {
        let index = self.index(
            self.startIndex,
            offsetBy: position
        )
        return self[index]
    }
}

"Hello"[3]    // "l"
```

<div class="week11-subscript-equivalence"><code>"Hello".at(3)</code><span>same lookup</span><code>"Hello"[3]</code></div>

<!--
Idea: Correct the output typo in the translated notes.
Say: "Both forms advance three Character positions from the start, so the result in Hello is the second l. The subscript changes syntax, not the indexing cost or range requirement."
Bridge: "Stop here. The custom subscript is the final example in the class notes."
-->
