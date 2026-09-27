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
<div class="week-marker">Week 10</div>

# Object-oriented programming with Swift

<p class="lead">Topic 6 · Classes, structures, properties, methods, initialization, and inheritance</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Present this week as Swift's object-oriented layer, connected to the value semantics already studied.
Say: "Swift supports object-oriented programming with both classes and structures, but their copy semantics are fundamentally different."
Bridge: "We will build the topic from that distinction."
-->

---

<div class="eyebrow">Today</div>

## Six parts of object-oriented Swift

<div class="sequence week10-roadmap">
  <div><b>1 · CONTEXT</b><span>Objects combine state and behavior</span></div>
  <div><b>2 · INSTANCES</b><span>Classes use references, structures use values</span></div>
  <div><b>3 · PROPERTIES</b><span>Stored, computed, observed, and shared values</span></div>
  <div><b>4 · METHODS</b><span>Behavior attached to an instance or a type</span></div>
  <div><b>5 · INITIALIZATION</b><span>Every stored property receives a valid value</span></div>
  <div><b>6 · INHERITANCE</b><span>Subclasses refine classes</span></div>
</div>

<!--
Idea: Follow the order of the class notes exactly.
Say: "The first two parts establish the semantic model. The remaining parts show how Swift defines state, behavior, construction, and specialization."
Bridge: "We begin with the central object-oriented idea."
-->

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Introduction, history and characteristics

<p class="lead">An object groups its internal state with the operations that can use or change that state.</p>

<!--
Idea: Keep the historical introduction focused on the idea used throughout the week.
Say: "Simula introduced classes in the 1960s, and Smalltalk popularized object-oriented programming in the 1980s. The lasting idea is the combination of state and behavior."
Bridge: "That combination appears in every class or structure we define."
-->

---

<div class="eyebrow">The object model</div>

## State and behavior belong to the same abstraction

<div class="week10-object-model">
  <div class="state"><b>STATE</b><code>properties</code><span>Data stored by an instance</span></div>
  <div class="object"><strong>INSTANCE</strong><span>A concrete value at run time</span></div>
  <div class="behavior"><b>BEHAVIOR</b><code>methods</code><span>Operations offered by the instance</span></div>
</div>

<div class="week10-note-line"><b>Class</b><span>A definition used to create instances</span></div>

<!--
Idea: Separate the compile-time definition from the run-time instance.
Say: "A class is the definition. An instance is a concrete run-time entity with its own state. Methods describe the operations available on that state."
Bridge: "Swift provides two closely related ways to define such abstractions."
-->

---

<div class="eyebrow">OOP in Swift</div>

## Classes and structures share most capabilities

<div class="week10-shared-capabilities">
  <div><code>properties</code><span>store or compute values</span></div>
  <div><code>methods</code><span>provide behavior</span></div>
  <div><code>init</code><span>establish initial state</span></div>
  <div><code>extension</code><span>add functionality</span></div>
  <div><code>protocol</code><span>declare a shared capability</span></div>
</div>

<!--
Idea: Correct the typo in the notes and state the actual common capabilities.
Say: "Classes and structures are much closer in Swift than in C or C++. Both support state, methods, initialization, extensions, and protocols."
Bridge: "Their central difference is how assignment behaves."
-->

---

<div class="eyebrow">The central distinction</div>

## A structure is a value type, while a class is a reference type

<div class="week10-type-split">
  <div class="value">
    <b>STRUCT</b>
    <code>var b = a</code>
    <span>copies the value</span>
  </div>
  <div class="reference">
    <b>CLASS</b>
    <code>var b = a</code>
    <span>copies the reference</span>
  </div>
</div>

<div class="week10-note-line"><b>Classes also add</b><span>inheritance, run-time type casting, and shared references to one instance</span></div>

<!--
Idea: Establish value versus reference semantics before any detailed examples.
Say: "The syntax can look similar, but assignment means two different things. With a struct, we get an independent value. With a class, two variables may name the same instance."
Bridge: "First we define one of each."
-->

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Classes and structures

<p class="lead">A type definition describes properties and behavior. Initialization creates a concrete instance.</p>

<!--
Idea: Introduce definitions before copy semantics.
Say: "The following examples use a screen coordinate as a value and a window as a reference object."
Bridge: "Their declarations differ only by one keyword."
-->

---

<div class="eyebrow">Definitions</div>

## `struct` and `class` introduce new types

<div class="columns equal">
<div>

```swift
struct ScreenCoords {
    var x = 0
    var y = 0
}
```

<div class="week10-type-label value"><b>VALUE TYPE</b><span>each variable owns a value</span></div>
</div>
<div>

```swift
class Window {
    var corner = ScreenCoords()
    var height = 0
    var width = 0
    var visible = true
    var label: String?
}
```

<div class="week10-type-label reference"><b>REFERENCE TYPE</b><span>variables can share an instance</span></div>
</div>
</div>

<!--
Idea: Use the same domain and property choices as the notes, with English names.
Say: "Both definitions contain stored properties. Swift infers the types of properties with initial values, while label explicitly uses an optional String."
Bridge: "Parentheses create concrete instances."
-->

---

<div class="eyebrow">Creating instances</div>

## Default values make the empty initializer available

```swift
var coords = ScreenCoords()
var window = Window()
```

<div class="week10-instance-values">
  <div><code>coords</code><span><code>x = 0</code><code>y = 0</code></span></div>
  <div><code>window</code><span><code>corner = (0, 0)</code><code>height = 0</code><code>width = 0</code><code>visible = true</code><code>label = nil</code></span></div>
</div>

<!--
Idea: Show the complete initial state produced by the empty initializer.
Say: "Every stored property already has a value. The optional label receives nil automatically."
Bridge: "Structures also receive an initializer built from their properties."
-->

---

<div class="eyebrow">Memberwise initialization</div>

## Structures receive a memberwise initializer

```swift
let a = ScreenCoords(x: 200, y: 400)
let b = ScreenCoords(x: 200)
let c = ScreenCoords()
```

<div class="week10-memberwise">
  <div><code>a</code><b>(200, 400)</b></div>
  <div><code>b</code><b>(200, 0)</b></div>
  <div><code>c</code><b>(0, 0)</b></div>
</div>

<div class="week10-note-line"><b>Only structures</b><span>A class does not receive a memberwise initializer.</span></div>

<!--
Idea: Make the difference between default values and explicit member values visible.
Say: "A property with a default value may be omitted. This automatically generated memberwise initializer belongs to structures, not classes."
Bridge: "Now assignment reveals the deeper semantic difference."
-->

---

<div class="eyebrow">Value semantics</div>

## Assigning a structure creates an independent copy

```swift
var coords1 = ScreenCoords(x: 600, y: 600)
var coords2 = coords1

coords2.x = 1000

coords1.x    // 600
coords2.x    // 1000
```

<div class="week10-copy-diagram">
  <div><code>coords1</code><b>x: 600</b><b>y: 600</b></div>
  <span>COPY</span>
  <div><code>coords2</code><b>x: 1000</b><b>y: 600</b></div>
</div>

<!--
Idea: Explain structure assignment without talking about memory addresses.
Say: "The assignment copies the current value. Changing coords2 later has no effect on coords1."
Bridge: "Class assignment preserves one shared instance instead."
-->

---

<div class="eyebrow">Reference semantics</div>

## Assigning a class creates another reference to the same instance

```swift
var window1 = Window()
window1.width = 800

var window2 = window1
window2.width = 1000

window1.width    // 1000
```

<div class="week10-reference-diagram">
  <code>window1</code><span>same Window instance</span><code>window2</code>
  <div><b>width: 1000</b></div>
</div>

<!--
Idea: Emphasize aliasing, not physical pointer details.
Say: "The variables are two names for one Window. Mutating the instance through either reference changes the state observed through both."
Bridge: "This difference also changes the meaning of let."
-->

---

<div class="eyebrow">Constants</div>

## `let` freezes a struct value but only the class reference

<div class="week10-let-split">
<div>
<b>STRUCT CONSTANT</b>

```swift
let coords = ScreenCoords(x: 4, y: 4)
coords.x = 8
// error
```

<span>Neither the variable nor its properties can change.</span>
</div>
<div>
<b>CLASS CONSTANT</b>

```swift
let window = Window()
window.label = "List"  // valid
window = Window()      // error
```

<span>The reference cannot change, but the referenced instance can.</span>
</div>
</div>

<!--
Idea: Avoid the misleading phrase that a let class instance is immutable.
Say: "For a class, let fixes which instance the variable references. It does not freeze the variable properties inside that instance."
Bridge: "When two class references exist, Swift can test whether they name the same instance."
-->

---

<div class="eyebrow">Identity and equality</div>

<!-- _class: compact -->

## `===` asks whether two references identify one instance

```swift
let first = Window()
let alias = first
let another = Window()

first === alias      // true
first === another    // false
```

<div class="week10-identity-table">
  <div class="header"><b>Operator</b><b>Question</b></div>
  <div><code>===</code><span>Do both references identify the same class instance?</span></div>
  <div><code>==</code><span>Do two values satisfy the type's definition of equality?</span></div>
</div>

<!--
Idea: Separate reference identity from value equality.
Say: "Identity is built into classes. Equality is a value-level relation that the type designer defines, usually through Equatable."
Bridge: "Function parameters preserve the same value and reference behavior."
-->

---

<div class="eyebrow">Structure parameters</div>

## A normal parameter cannot mutate a structure value

```swift
func move(
    coords: ScreenCoords,
    dx: Int,
    dy: Int
) {
    coords.x += dx
    coords.y += dy
}

// error: 'coords' is a 'let' constant
```

<div class="week10-note-line"><b>Parameter rule</b><span>A function receives its parameters as constants.</span></div>

<!--
Idea: Connect parameter immutability with value semantics.
Say: "The local parameter binding is constant. A structure value therefore cannot have its properties changed inside this function."
Bridge: "The functional alternative returns a new value."
-->

---

<div class="eyebrow">Functional update</div>

<!-- _class: compact code-small -->

## A function can return a modified structure

```swift
func moved(
    coords: ScreenCoords,
    dx: Int,
    dy: Int
) -> ScreenCoords {
    return ScreenCoords(
        x: coords.x + dx,
        y: coords.y + dy
    )
}

let start = ScreenCoords()
let end = moved(coords: start, dx: 100, dy: 100)
```

<div class="week10-before-after"><code>start (0, 0)</code><span>new value</span><code>end (100, 100)</code></div>

<!--
Idea: Preserve the nonmutating approach from the notes.
Say: "The input remains unchanged. The result is a different ScreenCoords value containing the requested position."
Bridge: "A class parameter behaves differently because its instance remains shared."
-->

---

<div class="eyebrow">Class parameters</div>

## A constant reference can still mutate its instance

```swift
func move(window: Window, dx: Int, dy: Int) {
    window.corner = moved(
        coords: window.corner,
        dx: dx,
        dy: dy
    )
}

let window = Window()
move(window: window, dx: 500, dy: 500)
window.corner    // (500, 500)
```

<div class="week10-note-line"><b>Visible side effect</b><span>The caller and the parameter refer to the same Window instance.</span></div>

<!--
Idea: Be precise about what is constant and what changes.
Say: "The function cannot make its parameter refer to another Window. It can change properties of the shared Window instance."
Bridge: "That side effect is one reason Swift often favors structures."
-->

---

<div class="eyebrow">Choosing a representation</div>

## Copy semantics favor structures, while shared identity favors classes

<div class="week10-choice">
  <div><b>USE A STRUCTURE</b><span>The value contains a small set of data</span><span>Copies should be independent</span><span>No inheritance relationship is needed</span></div>
  <div><b>USE A CLASS</b><span>Several parts of the program must share one instance</span><span>Identity matters</span><span>Inheritance or run-time casting is required</span></div>
</div>

<!--
Idea: State the criteria as semantic decisions rather than a blanket rule.
Say: "A coordinate is naturally a value. A shared object graph or an inheritance hierarchy needs reference identity, so a class is appropriate."
Bridge: "Both representations describe state through properties."
-->

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Properties

<p class="lead">Stored properties hold state. Computed properties derive a value. Observers react to assignment.</p>

<!--
Idea: Establish the three roles covered by this section.
Say: "Swift uses one dot syntax for properties, even though the implementation behind that syntax may store, compute, or observe a value."
Bridge: "Stored properties are the simplest case."
-->

---

<div class="eyebrow">Stored properties</div>

## `var` may change, while `let` receives one value

```swift
struct FixedLengthRange {
    var firstValue: Int
    let length: Int
}

var range = FixedLengthRange(firstValue: 0, length: 3)
range.firstValue = 6

// range now represents 6, 7, 8
```

<div class="week10-property-map">
  <div><code>firstValue</code><span>stored variable</span><b>6</b></div>
  <div><code>length</code><span>stored constant</span><b>3</b></div>
</div>

<!--
Idea: Show that let and var can coexist inside one mutable structure value.
Say: "The range can move because firstValue is variable. Its length remains fixed after initialization."
Bridge: "Some useful properties need not store another value at all."
-->

---

<div class="eyebrow">Computed properties</div>

## A rectangle can derive its center from origin and size

<div class="columns image-right">
<div>

<div class="week10-computed-dependency">
  <code>origin</code><span>stored</span>
  <code>size</code><span>stored</span>
  <code>center</code><span>computed</span>
</div>

<p class="week10-explain">Reading <code>center</code> calculates a point. Assigning <code>center</code> updates <code>origin</code>.</p>
</div>
<div>

![Moving a rectangle by assigning a new center](../../../docs/teoria/tema06-programacion-orientada-objetos-swift/imagenes/computedProperties.png)

</div>
</div>

<!--
Idea: Use the diagram from the topic because it clarifies the geometry behind the getter and setter.
Say: "Center is redundant state, so the rectangle does not store it. The getter derives it. The setter converts a requested center into a new origin."
Bridge: "The code makes those two directions explicit."
-->

---

<div class="eyebrow">Computed getter</div>

## Reading `center` creates a point from stored values

```swift
struct Point {
    var x = 0.0, y = 0.0
}

struct Size {
    var width = 0.0, height = 0.0
}

struct Rectangle {
    var origin = Point()
    var size = Size()

    var center: Point {
        get {
            Point(
                x: origin.x + size.width / 2,
                y: origin.y + size.height / 2
            )
        }
    }
}
```

<!--
Idea: Isolate the getter before adding the setter.
Say: "No center field exists. Each read uses the current origin and size, so the result cannot become inconsistent with them."
Bridge: "A setter can translate an assigned center back into stored state."
-->

---

<div class="eyebrow">Computed setter</div>

<!-- _class: compact code-small -->

## Assigning `center` moves the rectangle by changing `origin`

```swift
var center: Point {
    get {
        Point(
            x: origin.x + size.width / 2,
            y: origin.y + size.height / 2
        )
    }
    set {
        origin.x = newValue.x - size.width / 2
        origin.y = newValue.y - size.height / 2
    }
}
```

<div class="week10-center-calculation">
  <code>new center (15, 15)</code><span>size (10, 10)</span><code>new origin (10, 10)</code>
</div>

<!--
Idea: Explain newValue with the concrete example in the notes.
Say: "Swift gives an unnamed setter parameter the default name newValue. Subtracting half the size finds the origin that places the center at the assigned point."
Bridge: "A property that only derives information needs no setter."
-->

---

<div class="eyebrow">Read-only computation</div>

## A getter-only property can omit the `get` block

```swift
struct Cuboid {
    var width = 0.0
    var height = 0.0
    var depth = 0.0

    var volume: Double {
        width * height * depth
    }
}

let box = Cuboid(width: 4, height: 5, depth: 2)
box.volume    // 40
```

<div class="week10-note-line"><b>No stored volume</b><span>The result always reflects the three current dimensions.</span></div>

<!--
Idea: Show the concise modern Swift form.
Say: "Because volume has no meaningful independent assignment, the property exposes only a getter."
Bridge: "Observers solve a different problem: reacting when stored state changes."
-->

---

<div class="eyebrow">Property observers</div>

## `willSet` sees the incoming value and `didSet` sees the old one

<div class="week10-observer-order">
  <div><code>oldValue</code><b>200</b></div>
  <span><code>willSet(newValue)</code></span>
  <div><code>assignment</code><b>360</b></div>
  <span><code>didSet(oldValue)</code></span>
  <div><code>stored value</code><b>360</b></div>
</div>

<div class="week10-note-line"><b>Observer rule</b><span>They run on every assignment, even when the new value equals the current value.</span></div>

<!--
Idea: Explain the order before showing a full class.
Say: "willSet runs before storage and receives the value about to arrive. didSet runs after storage and can compare against the former value."
Bridge: "A step counter makes both moments concrete."
-->

---

<div class="eyebrow">Observer example</div>

<!-- _class: compact code-small -->

## The counter reports an update before and after assignment

```swift
class StepCounter {
    var totalSteps = 0 {
        willSet(newTotal) {
            print("Updating to \(newTotal)")
        }
        didSet {
            if totalSteps > oldValue {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}

let counter = StepCounter()
counter.totalSteps = 200
```

<div class="week10-output"><code>Updating to 200</code><code>Added 200 steps</code></div>

<!--
Idea: Keep the output next to the observer that produces it.
Say: "At willSet time the stored value is still zero. At didSet time the property contains 200 and oldValue contains zero."
Bridge: "didSet may also repair an unwanted assignment."
-->

---

<div class="eyebrow">Correcting an assignment</div>

<!-- _class: compact code-small -->

## `didSet` can restore the previous valid value

```swift
class StepCounter {
    var totalSteps = 0 {
        didSet {
            if totalSteps < 0 {
                totalSteps = oldValue
            }
        }
    }
}

let counter = StepCounter()
counter.totalSteps = 200
counter.totalSteps = -10
counter.totalSteps          // 200
```

<div class="week10-note-line"><b>Important</b><span>Assigning inside <code>didSet</code> replaces the value without calling the observer again.</span></div>

<!--
Idea: Explain why this correction does not recurse indefinitely.
Say: "The negative assignment happens, didSet detects it, and the previous value is restored. Swift does not call the property's observers recursively for that correction."
Bridge: "Some state belongs to the type rather than to one instance."
-->

---

<div class="eyebrow">Type properties</div>

## `static` stores one value for the whole type

<div class="week10-static-split">
  <div><b>INSTANCE PROPERTY</b><code>item.value</code><span>one value per instance</span></div>
  <div><b>TYPE PROPERTY</b><code>Value.total</code><span>one value shared by the type</span></div>
</div>

```swift
struct Value {
    var value = 0 {
        didSet { Value.total += value }
    }
    static var total = 0
}
```

<!--
Idea: Distinguish ownership before the multi-instance example.
Say: "Every Value instance owns value. The type Value itself owns one total shared by all instances. We access it through the type name."
Bridge: "Changes made by several instances accumulate in that one property."
-->

---

<div class="eyebrow">Shared type state</div>

## Three instances update one type property

```swift
var a = Value()
var b = Value()
var c = Value()

a.value = 10
b.value = 20
c.value = 30

Value.total    // 60
```

<div class="week10-shared-total">
  <code>a: 10</code><code>b: 20</code><code>c: 30</code><b>Value.total: 60</b>
</div>

<div class="week10-note-line"><b>Access through the type</b><span><code>a.total</code> is invalid because <code>total</code> does not belong to an instance.</span></div>

<!--
Idea: Show one shared destination for three updates.
Say: "The instances remain separate. Only the static property is shared and addressed as Value.total."
Bridge: "Methods attach behavior to the same kinds of types."
-->

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Methods

<p class="lead">Instance methods work with one value or object. Type methods belong to the type itself.</p>

<!--
Idea: Introduce the two method levels in direct parallel with instance and type properties.
Say: "A method is a function associated with a type. The receiver determines which instance state the method can access."
Bridge: "A counter provides a simple instance-method example."
-->

---

<div class="eyebrow">Instance methods</div>

<!-- _class: compact code-small -->

## Calls use dot syntax on a concrete instance

```swift
class Counter {
    var count = 0

    func increment() {
        count += 1
    }

    func increment(by amount: Int) {
        count += amount
    }

    func reset() {
        count = 0
    }
}
```

```swift
let counter = Counter()
counter.increment()
counter.increment(by: 5)    // count is 6
counter.reset()             // count is 0
```

<!--
Idea: Keep definition and use together.
Say: "Each call has an implicit receiver, counter. Inside the method, unqualified count refers to that receiver's property."
Bridge: "Argument labels help a method call read naturally."
-->

---

<div class="eyebrow">Argument labels</div>

<!-- _class: compact code-small -->

## External labels describe the call, while local names serve the body

```swift
class Counter {
    var count = 0

    func increment(
        by amount: Int,
        numberOfTimes: Int
    ) {
        count += amount * numberOfTimes
    }
}

let counter = Counter()
counter.increment(by: 5, numberOfTimes: 3)
```

<div class="week10-argument-map">
  <div><code>by</code><span>external label</span><code>amount</code><span>local name</span></div>
  <div><code>numberOfTimes</code><span>external and local name</span></div>
</div>

<!--
Idea: Connect method labels to the function-label rules from week 8.
Say: "The call reads increment by five, number of times three. Inside the method, the first value is named amount."
Bridge: "The receiver itself also has a name inside the method."
-->

---

<div class="eyebrow">The current instance</div>

## `self` disambiguates a property from a parameter

```swift
struct Point {
    var x = 0.0
    var y = 0.0

    func isRight(of x: Double) -> Bool {
        return self.x > x
    }
}

let point = Point(x: 4, y: 5)
point.isRight(of: 1)    // true
```

<div class="week10-self-map"><code>self.x</code><span>property of the Point</span><code>x</code><span>method parameter</span></div>

<!--
Idea: Show the one situation where self is required.
Say: "Without self, x names the parameter because it shadows the property. self.x explicitly selects the property of the receiving point."
Bridge: "A structure method still cannot mutate self unless it says so."
-->

---

<div class="eyebrow">Nonmutating value method</div>

## A structure method can return a new value

```swift
struct Point {
    var x = 0.0
    var y = 0.0

    func moved(dx: Double, dy: Double) -> Point {
        return Point(x: x + dx, y: y + dy)
    }
}

let start = Point(x: 1, y: 1)
let end = start.moved(dx: 2, dy: 3)
```

<div class="week10-before-after"><code>start (1, 1)</code><span>returns</span><code>end (3, 4)</code></div>

<!--
Idea: Reuse the functional update pattern in method form.
Say: "The receiver remains unchanged. The method computes and returns another Point."
Bridge: "Swift also supports an explicitly mutating structure method."
-->

---

<div class="eyebrow">Mutating value method</div>

<!-- _class: compact code-small -->

## `mutating` permits a structure method to change `self`

```swift
struct Point {
    var x = 0.0
    var y = 0.0

    mutating func move(dx: Double, dy: Double) {
        x += dx
        y += dy
    }
}

var point = Point(x: 1, y: 1)
point.move(dx: 2, dy: 3)
// point is now (3, 4)
```

<div class="week10-note-line"><b>Receiver must be variable</b><span>A mutating method cannot be called on a structure stored in a <code>let</code> constant.</span></div>

<!--
Idea: Tie mutating to the value held by the caller.
Say: "The method changes the Point value itself, so the receiving variable must permit reassignment."
Bridge: "A mutating method may replace the complete value, not just individual properties."
-->

---

<div class="eyebrow">Replacing `self`</div>

<!-- _class: compact code-small -->

## A mutating enum method can move to another case

```swift
enum ThreeStateSwitch {
    case off, low, high

    mutating func next() {
        switch self {
        case .off:  self = .low
        case .low:  self = .high
        case .high: self = .off
        }
    }
}

var ovenLight = ThreeStateSwitch.low
ovenLight.next()    // high
ovenLight.next()    // off
```

<div class="week10-state-cycle"><code>off</code><code>low</code><code>high</code><span>then off again</span></div>

<!--
Idea: Show assignment to self with the clearest example from the notes.
Say: "The enum value has no mutable fields here. The method mutates it by replacing the entire value with another case."
Bridge: "Behavior can also belong to the type rather than to an instance."
-->

---

<div class="eyebrow">Type methods</div>

## `static func` is called on the type

```swift
class Window {
    static var registered: [Window] = []

    static func register(_ window: Window) {
        registered.append(window)
    }
}

let first = Window()
Window.register(first)
Window.registered.count    // 1
```

<div class="week10-static-flow"><code>Window.register(first)</code><span>updates</span><code>Window.registered</code></div>

<!--
Idea: Pair a type method with the type property it manages.
Say: "The call has no Window instance as receiver. It operates on the registry owned by the Window type."
Bridge: "Before any instance can receive a method call, Swift must initialize all its stored state."
-->

---

<!-- _class: section -->

<div class="eyebrow">05</div>

# Initialization

<p class="lead">An initializer prepares a valid instance and assigns every nonoptional stored property.</p>

<!--
Idea: State the safety guarantee at the center of Swift initialization.
Say: "Swift does not allow a newly created instance to contain indeterminate stored state."
Bridge: "Default property values can satisfy that guarantee automatically."
-->

---

<div class="eyebrow">Initialization rule</div>

## Every stored property has a value before initialization finishes

<div class="week10-init-sources">
  <div><b>PROPERTY DEFAULT</b><code>var x = 0.0</code></div>
  <div><b>INITIALIZER</b><code>init(x: Double) { self.x = x }</code></div>
  <div><b>OPTIONAL DEFAULT</b><code>var label: String?</code><span>starts as nil</span></div>
</div>

<div class="week10-note-line"><b>No return statement</b><span>An initializer configures the new instance rather than returning a separate result.</span></div>

<!--
Idea: Show the three ways a stored property can become initialized in the examples.
Say: "A normal stored property needs a default or an initializer assignment. An optional without an explicit value starts as nil."
Bridge: "Swift can synthesize initializers when the definition is simple enough."
-->

---

<div class="eyebrow">Synthesized initializers</div>

<!-- _class: compact code-small -->

## Default and memberwise initialization depend on the type definition

<div class="week10-init-table">
  <div class="header"><b>Initializer</b><b>Structure</b><b>Class</b></div>
  <div><code>Type()</code><span>available when every property has a default</span><span>available when every property has a default</span></div>
  <div><code>Type(x:y:)</code><span>memberwise initializer</span><span>not synthesized</span></div>
</div>

```swift
struct Point2D { var x = 0.0; var y = 0.0 }
class Segment { var p1 = Point2D(); var p2 = Point2D() }

let p = Point2D(x: 10, y: 10)
let s = Segment()
```

<!--
Idea: Clarify synthesis without overstating every special case.
Say: "Defining a custom initializer changes which synthesized initializers remain available. The key classroom distinction is that structures receive the memberwise form and classes do not."
Bridge: "A custom initializer can perform conversion as it establishes state."
-->

---

<div class="eyebrow">Custom initialization</div>

<!-- _class: compact code-small -->

## Argument labels select different ways to build one type

```swift
struct Celsius {
    var temperature: Double

    init(fromFahrenheit value: Double) {
        temperature = (value - 32) / 1.8
    }

    init(fromKelvin value: Double) {
        temperature = value - 273.15
    }
}

let boiling = Celsius(fromFahrenheit: 212)
let freezing = Celsius(fromKelvin: 273.15)
```

<div class="week10-init-results"><code>boiling.temperature</code><b>100</b><code>freezing.temperature</code><b>0</b></div>

<!--
Idea: Use the labels as part of the API meaning.
Say: "Both initializers receive a Double, so the label communicates the unit and selects the correct conversion."
Bridge: "An underscore removes the external label when the unit is already obvious."
-->

---

<div class="eyebrow">Initializer labels</div>

## `_` removes the external argument label

```swift
extension Celsius {
    init(_ celsius: Double) {
        temperature = celsius
    }
}

let bodyTemperature = Celsius(37)
```

<div class="week10-call-comparison">
  <div><code>Celsius(fromFahrenheit: 212)</code><span>the label explains a conversion</span></div>
  <div><code>Celsius(37)</code><span>the unlabeled value already uses Celsius</span></div>
</div>

<!--
Idea: Connect initializer labels with function and method argument labels.
Say: "Initializers normally expose argument labels. The underscore explicitly opts out when a concise call remains clear."
Bridge: "Optionals can remain nil while required constant properties receive their one value."
-->

---

<div class="eyebrow">Constants and optionals</div>

<!-- _class: compact code-small -->

## Initialization may set a `let` property and leave an optional as `nil`

```swift
class SurveyQuestion {
    let text: String
    var answer: String?

    init(text: String) {
        self.text = text
    }
}

let question = SurveyQuestion(
    text: "Do you like cheese?"
)

question.answer    // nil
```

<div class="week10-note-line"><b>After initialization</b><span><code>text</code> cannot change, while <code>answer</code> may receive a String later.</span></div>

<!--
Idea: Show two different initialization rules in one small class.
Say: "The initializer gives the constant text its only value. The optional answer needs no explicit assignment and starts as nil."
Bridge: "One initializer can delegate common work to another."
-->

---

<!-- _class: compact code-small dense -->

<div class="eyebrow">Initializer delegation</div>

## One structure initializer can call another with `self.init`

```swift
struct Rectangle {
    var origin = Point()
    var size = Size()

    init() {}

    init(origin: Point, size: Size) {
        self.origin = origin
        self.size = size
    }

    init(center: Point, size: Size) {
        let x = center.x - size.width / 2
        let y = center.y - size.height / 2
        self.init(origin: Point(x: x, y: y), size: size)
    }
}
```

<div class="week10-delegation"><code>init(center:size:)</code><span>calculates origin</span><code>init(origin:size:)</code></div>

<!--
Idea: Explain delegation as reuse of one established initialization path.
Say: "The center-based initializer performs only the conversion it uniquely needs, then delegates the stored-property assignments."
Bridge: "Inheritance adds a second initialization level, the superclass."
-->

---

<!-- _class: section -->

<div class="eyebrow">06</div>

# Inheritance

<p class="lead">A subclass inherits class behavior, adds specialization, and may override inherited members.</p>

<!--
Idea: Restrict inheritance to classes.
Say: "Structures do not form inheritance hierarchies. A subclass starts from a superclass and refines it."
Bridge: "The vehicle example begins with a base class."
-->

---

<div class="eyebrow">Base class</div>

## A base class defines state and behavior shared by subclasses

```swift
class Vehicle {
    var currentSpeed = 0.0

    var description: String {
        "traveling at \(currentSpeed) km/h"
    }

    func makeNoise() -> String {
        ""
    }
}
```

<div class="week10-note-line"><b>Swift detail</b><span>A class need not inherit from a universal base class.</span></div>

<!--
Idea: Present the common interface before any subclasses.
Say: "Vehicle supplies a speed, a computed description, and a method that subclasses can refine. Swift has no language-level abstract class requirement here."
Bridge: "A subclass names its superclass after a colon."
-->

---

<div class="eyebrow">Subclassing</div>

<!-- _class: compact -->

## A subclass inherits existing members and adds its own

```swift
class Bicycle: Vehicle {
    var hasBasket = false
}

let bicycle = Bicycle()
bicycle.hasBasket = true
bicycle.currentSpeed = 10
bicycle.description
// "traveling at 10.0 km/h"
```

<div class="week10-inheritance-row"><code>Vehicle</code><span>currentSpeed · description · makeNoise()</span><code>Bicycle</code><span>hasBasket</span></div>

<!--
Idea: Make inherited and added members visible separately.
Say: "Bicycle receives every accessible Vehicle member without redeclaring it, then adds hasBasket."
Bridge: "Inheritance can continue through more than one level."
-->

---

<div class="eyebrow">Multilevel inheritance</div>

## A subclass receives features from the complete chain

```swift
class Tandem: Bicycle {
    var currentPassengers = 0
}

let tandem = Tandem()
tandem.hasBasket = true
tandem.currentPassengers = 2
tandem.currentSpeed = 18
```

<div class="week10-hierarchy">
  <div><code>Vehicle</code><span>speed and description</span></div>
  <div><code>Bicycle</code><span>basket</span></div>
  <div><code>Tandem</code><span>passenger count</span></div>
</div>

<!--
Idea: Show accumulation down the hierarchy.
Say: "Tandem can use the member it defines, the Bicycle member, and the Vehicle members."
Bridge: "A subclass may also replace an inherited implementation."
-->

---

<div class="eyebrow">Method overriding</div>

<!-- _class: compact -->

## `override` supplies subclass behavior for an inherited method

```swift
class Train: Vehicle {
    override func makeNoise() -> String {
        "Choo choo"
    }
}

let train = Train()
train.makeNoise()    // "Choo choo"
```

<div class="week10-override-map">
  <div><code>Vehicle.makeNoise()</code><span>returns an empty string</span></div>
  <div><code>Train.makeNoise()</code><span>returns "Choo choo"</span></div>
</div>

<!--
Idea: Explain override as a checked declaration, not accidental name reuse.
Say: "The keyword tells the compiler to verify that a matching member exists in a superclass. The Train implementation runs for a Train instance."
Bridge: "An overriding property can reuse the superclass result."
-->

---

<div class="eyebrow">Property overriding</div>

<!-- _class: compact code-small -->

## `super` accesses the inherited implementation

```swift
class Car: Vehicle {
    var gear = 1

    override var description: String {
        super.description + " in gear \(gear)"
    }
}

let car = Car()
car.currentSpeed = 50
car.gear = 3
car.description
// "traveling at 50.0 km/h in gear 3"
```

<div class="week10-description-build"><code>super.description</code><span>plus gear text</span><code>Car.description</code></div>

<!--
Idea: Show refinement rather than complete replacement.
Say: "The subclass asks the superclass to build the common part, then appends information specific to Car."
Bridge: "A subclass may observe an inherited property without replacing its storage."
-->

---

<div class="eyebrow">Observing inherited state</div>

## A subclass observer can synchronize another property

```swift
class AutomaticCar: Car {
    override var currentSpeed: Double {
        didSet {
            gear = min(Int(currentSpeed / 25) + 1, 5)
        }
    }
}

let automatic = AutomaticCar()
automatic.currentSpeed = 100
automatic.gear    // 5
```

<div class="week10-speed-gear"><code>speed 100</code><span>didSet calculation</span><code>gear 5</code></div>

<!--
Idea: Connect inheritance back to property observers.
Say: "AutomaticCar keeps the inherited speed property and adds a reaction. Whenever speed changes, the observer updates gear."
Bridge: "Subclass initialization must also respect the superclass state."
-->

---

<!-- _class: compact code-small dense ultra-dense -->

<div class="eyebrow">Subclass initialization</div>

## A designated subclass initializer initializes its properties before `super.init`

```swift
class Vehicle {
    var currentSpeed: Double

    init(speed: Double) {
        currentSpeed = speed
    }
}

class Bicycle: Vehicle {
    var hasBasket: Bool

    init(hasBasket: Bool, speed: Double) {
        self.hasBasket = hasBasket
        super.init(speed: speed)
    }
}

let bicycle = Bicycle(hasBasket: true, speed: 5)
```

<div class="week10-init-order"><code>Bicycle.hasBasket</code><span>then</span><code>Vehicle.currentSpeed</code></div>

<!--
Idea: State the initialization order shown by the notes.
Say: "The subclass first initializes the stored property it introduces. It then delegates initialization of inherited state to the superclass."
Bridge: "Stop here. Week 11 continues with protocols, type casting, generic types, extensions, and operator functions."
-->
