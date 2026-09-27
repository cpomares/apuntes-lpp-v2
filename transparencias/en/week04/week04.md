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
<div class="week-marker">Week 4</div>

# Higher-order functions and closures

<p class="lead">Topic 2 · Functional Programming in Scheme</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Enlazar con la semana anterior: ya sabemos crear y pasar funciones; hoy completamos la idea de función como dato.
Say: "Last week we learned to create functions with lambda and pass them as arguments. Today we use that idea to build more general programs."
Bridge: "We will develop the topic in four steps."
-->

---

<div class="eyebrow">Today</div>

## Four uses of functions as values

<div class="sequence week04-roadmap">
  <div><b>1 · GENERALIZE</b><span>Pass a function to separate recursion from the operation</span></div>
  <div><b>2 · CREATE</b><span>Return a new function that captures its environment</span></div>
  <div><b>3 · STORE</b><span>Keep functions inside lists and invoke them later</span></div>
  <div><b>4 · COMPOSE</b><span>Combine <code>map</code>, <code>filter</code>, quantifiers, and folds</span></div>
</div>

<!--
Idea: Dar el mapa de la clase sin enumerar todo el tema.
Say: "We will pass functions, return functions, store them in lists, and finally compose higher-order functions."
Bridge: "We begin with three recursive functions that repeat the same pattern."
-->

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Generalization with function parameters

<p class="lead">The recursive structure stays the same. Only the operation applied to each number changes.</p>

<!--
Idea: La abstracción nace al localizar qué parte cambia y qué parte permanece.
Say: "The recursive structure is stable. The only changing part is the operation applied to each number."
Bridge: "Let us compare three versions."
-->

---

<!-- _class: compact code-small -->

<div class="eyebrow">Generalization</div>

## Separate what stays from what changes

<div class="generalization-grid">
<div class="generalization-skeleton">

### The recursive skeleton stays

```racket
(define (<sum-function> a b)
  (if (> a b)
      0
      (+ <value-for-a>
         (<sum-function> (+ a 1) b))))
```

</div>
<div class="generalization-variation">

### Only this expression changes

<div><code>a</code><span>sum the numbers</span></div>
<div><code>(* a a)</code><span>sum their squares</span></div>
<div><code>(* a a a)</code><span>sum their cubes</span></div>

</div>
</div>

<div class="generalization-result"><b>Generalize</b><span>Receive a function <code>f</code> and replace <code>&lt;value-for-a&gt;</code> with <code>(f a)</code>.</span></div>

<!--
Idea: La generalización consiste en conservar el esqueleto recursivo y convertir la única parte variable en un parámetro.
Say: "Generalization starts by separating the stable recursive skeleton from the expression that changes. We turn that changing expression into a function parameter."
Bridge: "The placeholder value-for-a now becomes the call f of a."
-->

---

<div class="eyebrow">The abstraction</div>

## The changing expression becomes `f`

<div class="columns equal">
<div>

```racket
(define (suma-f-x f a b)
  (if (> a b)
      0
      (+ (f a)
         (suma-f-x f (+ a 1) b))))
```

</div>
<div>

<div class="week04-abstraction-step">
  <div><span>Current number</span><code>a</code></div>
  <div><span>Changing operation</span><code>f</code></div>
  <div><span>Value to add</span><code>(f a)</code></div>
</div>

`f` controls **what to add**. The recursive function controls **how to traverse the interval**.

</div>
</div>

<!--
Idea: Separar política y recorrido: f decide la transformación y suma-f-x mantiene la recursión.
Say: "The parameter f represents the operation. Suma-f-x keeps the recursive traversal and delegates the changing step to f."
Bridge: "Now every previous function becomes a particular use of this abstraction."
-->

---

<div class="eyebrow">Using the abstraction</div>

## Named functions and lambda expressions both fit

```racket
(define (cubo x)
  (* x x x))

(suma-f-x cubo 1 10)                       ; ⇒ 3025
(suma-f-x (lambda (x) x) 1 10)             ; ⇒ 55
(suma-f-x (lambda (n) (/ n (- n 1))) 2 100)
```

> Passing a function removes duplicated recursion without fixing one particular operation.

<!--
Idea: Mostrar que el parámetro puede recibir un nombre de función o una lambda.
Say: "A function parameter accepts either a named function or a lambda expression. The recursive algorithm does not change."
Bridge: "Functions can also travel in the opposite direction: a function can return a new function."
-->

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Functions that return functions

<p class="lead">A function can create another function at runtime. The returned function remembers the environment where it was created.</p>

<!--
Idea: Introducir la closure como función creada en ejecución que conserva su entorno léxico.
Say: "A function may return a new function. That new function can remember variables from the scope where it was created."
Bridge: "That combination is called a closure."
-->

---

<div class="eyebrow">Function construye-sumador</div>

## Procedures are evaluated in the scope where they are created

<div class="columns equal hand-global-definition">
<div>

```racket
(define k 10)

(define (construye-sumador k)
  (lambda (x)
    (+ x k)))
```

</div>
<div class="handwritten-stage hand-scope hand-global-scope">
  <b>Global scope</b>
  <div><code>k</code><span>10</span></div>
  <div><code>construye-sumador</code><span>#&lt;procedure&gt;</span></div>
  <p><code>construye-sumador</code> is created here</p>
</div>
</div>

<div class="handwritten-note hand-key-rule">Therefore, <code>construye-sumador</code> is evaluated in the <u>global scope</u>.</div>

<!--
Idea: Establecer primero la regla usada en la explicación: los procedimientos se evalúan en el ámbito donde se crean.
Say: "Defining construye-sumador creates a procedure in the global scope. Procedures are evaluated in the scope where they are created. Therefore, when we later call construye-sumador, its evaluation starts from the global scope."
Bridge: "Now we evaluate a call to this procedure."
-->

---

<div class="eyebrow">Closures · Step 1</div>

## Calling the constructor creates its local scope

<div class="handwritten-stage hand-constructor-call">
  <div class="hand-scope hand-muted-scope">
    <b>Global scope</b>
    <div><code>construye-sumador</code><span>#&lt;procedure&gt;</span></div>
  </div>
  <div class="hand-call-center">
    <code>(define g</code>
    <code>&nbsp;&nbsp;(construye-sumador 100))</code>
    <span>evaluate the procedure</span>
    <strong>⇢</strong>
  </div>
  <div class="hand-scope hand-green">
    <b>Local scope of construye-sumador</b>
    <div><code>k</code><span>100</span></div>
  </div>
</div>

<div class="handwritten-note">The call binds <code>k</code> to <b>100</b> in the local scope of <code>construye-sumador</code>.</div>

<!--
Idea: La llamada evalúa el procedimiento construye-sumador desde el ámbito global y crea su ámbito local con k=100.
Say: "The definition of g calls construye-sumador with one hundred. Construye-sumador is evaluated in the global scope, where it was created. The call creates the local scope of construye-sumador and binds k to one hundred."
Bridge: "The body of construye-sumador is a lambda expression, and that expression is evaluated inside this local scope."
-->

---

<div class="eyebrow">Closures · Step 2</div>

## `lambda` creates the function associated with `g`

<div class="handwritten-stage hand-lambda-created">
  <div class="hand-scope hand-green hand-constructor-scope-large">
    <b>Local scope of construye-sumador</b>
    <div><code>k</code><span>100</span></div>
    <p><code>(lambda (x) (+ x k))</code> is evaluated here</p>
    <div class="hand-runtime-function"><span>creates at runtime</span><code>#&lt;procedure:lambda&gt;</code></div>
  </div>
  <div class="hand-arrow hand-arrow-right">returned and associated with&nbsp; ⇢</div>
  <div class="hand-name-link">
    <code>g</code>
    <span>closure</span>
    <small>function + captured scope</small>
  </div>
</div>

<div class="handwritten-note hand-key-rule">This scope does not disappear: the function associated with <code>g</code> is enclosed in the scope where it was created.</div>

<!--
Idea: Lambda se evalúa dentro del ámbito local de construye-sumador y crea en ejecución la función que se asocia a g. Ese ámbito queda capturado.
Say: "Inside the local scope of construye-sumador, Scheme evaluates the lambda expression. Lambda creates a new function at runtime, and that function becomes associated with g. The local scope does not disappear because the new function is enclosed in the scope where it was created. That is why it is called a closure."
Bridge: "Calling the constructor again repeats the process with a new local scope."
-->

---

<div class="eyebrow">Closures · Step 3</div>

## Each constructor call creates a different local scope

<div class="hand-two-calls">
  <div class="hand-call-column">
    <code class="hand-call-code">(construye-sumador 100)</code>
    <div class="hand-down">↓ creates</div>
    <div class="hand-scope hand-green"><b>Local scope of construye-sumador</b><small>first invocation</small><div><code>k</code><span>100</span></div></div>
    <div class="hand-down">↑ enclosed by</div>
    <div class="hand-closure-mini"><code>g</code><span>function created here</span></div>
  </div>
  <div class="hand-call-column">
    <code class="hand-call-code">(construye-sumador 50)</code>
    <div class="hand-down">↓ creates</div>
    <div class="hand-scope hand-yellow"><b>Local scope of construye-sumador</b><small>second invocation</small><div><code>k</code><span>50</span></div></div>
    <div class="hand-down">↑ enclosed by</div>
    <div class="hand-closure-mini"><code>f</code><span>function created here</span></div>
  </div>
</div>

<div class="handwritten-note hand-center">Each closure keeps the local scope created by its own constructor call.</div>

<!--
Idea: Cada invocación a construye-sumador crea un ámbito local distinto, nombrado por la función y la invocación.
Say: "The first invocation creates a local scope of construye-sumador where k is one hundred. The function associated with g closes over that scope. The second invocation creates another local scope of construye-sumador where k is fifty, and the function associated with f closes over this second scope."
Bridge: "Now we evaluate g. Because g was created inside the first constructor scope, its execution takes place inside that captured scope."
-->

---

<div class="eyebrow">Closures · Step 4</div>

## `g` is evaluated inside the scope where it was created

<div class="hand-g-execution">
  <div class="hand-scope hand-muted-scope hand-global-call">
    <b>Global scope</b>
    <div><code>k</code><span>10</span></div>
    <div><code>g</code><span>closure</span></div>
  </div>
  <div class="hand-call-start"><code>(g 3)</code><span>evaluate g where it was created&nbsp; ⇢</span></div>
  <div class="hand-scope hand-green hand-captured-outer">
    <b>Local scope of construye-sumador</b>
    <div><code>k</code><span>100</span></div>
    <div class="hand-scope hand-blue hand-call-inner">
      <b>Local scope of the call to g</b>
      <div><code>x</code><span>3</span></div>
      <p>evaluate <code>(+ x k)</code> here</p>
    </div>
  </div>
</div>

<div class="hand-lookup-line"><span><code>x</code> comes from the call to <code>g</code>: <b>3</b></span><span><code>k</code> comes from the captured constructor scope: <b>100</b></span><strong><code>(+ 3 100)</code> ⇒ 103</strong></div>

<div class="handwritten-note hand-key-rule">The global value <code>k = 10</code> is not used.</div>

<!--
Idea: El ámbito local de la invocación a g aparece dentro del ámbito capturado de construye-sumador. x pertenece a la llamada y k al ámbito capturado.
Say: "When we evaluate g, its execution takes place inside the local scope of construye-sumador where g was created. The call to g creates its own local scope and binds x to three. The body uses x from the call to g and k from the enclosing constructor scope. Therefore, the result is one hundred and three. The global k equal to ten is not used."
Bridge: "This is the key idea: procedures are evaluated in the scope where they are created, not where they are called. If functions are values, we can also store them in data structures."
-->

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Functions in data structures

<p class="lead">A list can contain procedures. Store them, retrieve them, and invoke them like other values.</p>

<!--
Idea: Completar la idea de first-class: las funciones pueden formar parte de estructuras de datos.
Say: "Functions are values, so a list can store procedures just as it stores numbers or strings."
Bridge: "We build the list with the function values themselves."
-->

---

<div class="eyebrow">Building a function list</div>

## A list stores procedure values, not calls

```racket
(define lista
  (list cuadrado suma-1 doble))

(define lista2
  (cons (lambda (x) (+ x 5))
        lista))
```

<div class="procedure-list-diagram">
  <div class="procedure-list-name"><code>lista2</code><span>⇢</span></div>
  <div class="procedure-list-cell lambda-cell"><code>(lambda (x) (+ x 5))</code><small>procedure value</small></div>
  <div class="procedure-list-cell"><code>cuadrado</code><small>procedure value</small></div>
  <div class="procedure-list-cell"><code>suma-1</code><small>procedure value</small></div>
  <div class="procedure-list-cell"><code>doble</code><small>procedure value</small></div>
</div>

<div class="procedure-list-rule"><code>cuadrado</code><span>stores the procedure</span><code>(cuadrado 10)</code><span>calls it</span></div>

<!--
Idea: Diferenciar cuadrado de (cuadrado ...). En la lista guardamos el procedimiento, no su resultado.
Say: "The list contains the procedure values cuadrado, suma-1, and doble. There are no call parentheses around them."
Bridge: "To use one, we first retrieve it from the list."
-->

---

<div class="eyebrow">Invoking a stored function</div>

## Retrieval and invocation are two separate operations

<div class="columns equal">
<div>

### Retrieve

```racket
(first lista2)
; ⇒ #<procedure>
```

The result is a procedure value.

</div>
<div>

### Invoke

```racket
((first lista2) 10)
; ⇒ 15
```

The outer parentheses call that value.

</div>
</div>

<!--
Idea: Detenerse en el doble paréntesis igual que en la closure.
Say: "First returns a procedure. The outer parentheses then invoke that procedure with ten."
Bridge: "A recursive function can retrieve and invoke every procedure in the list."
-->

---

<div class="eyebrow">Function aplica-funcs</div>

## Apply the list from right to left

```racket
(define lista
  (list cuadrado cubo suma-1))

(aplica-funcs lista 5)
```

<div class="nested-call">
  <code>(cuadrado (cubo (suma-1 5)))</code>
  <strong>⇒ 46656</strong>
</div>

> The last function in the list runs first.

<!--
Idea: Antes del código recursivo, fijar claramente el orden deseado con la expresión anidada.
Say: "The list is written cuadrado, cubo, suma-1, but the nested call evaluates suma-1 first."
Bridge: "The recursive call naturally builds this right-to-left order."
-->

---

<div class="eyebrow">Recursive definition</div>

## The first function waits for the recursive result

```racket
(define (aplica-funcs lista-funcs x)
  (if (null? lista-funcs)
      x
      ((first lista-funcs)
       (aplica-funcs (rest lista-funcs) x))))
```

<div class="columns equal week04-cases">
<div><strong>Base case</strong><span>No functions remain, so return <code>x</code>.</span></div>
<div><strong>General case</strong><span>Apply the first function to the result produced by the rest.</span></div>
</div>

<!--
Idea: Relacionarlo con mi-reverse: la primera operación espera al resultado recursivo.
Say: "The recursive call processes the rest first. Then the first procedure is applied to that result."
Bridge: "Functions that receive or return functions have a general name."
-->

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Higher-order functions

<p class="lead">Functions control list processing. The traversal stays reusable while a function parameter supplies the changing behaviour.</p>

<!--
Idea: Conectar suma-f-x y aplica-funcs con la definición de orden superior.
Say: "The traversal can stay fixed while a function parameter supplies the behaviour that changes."
Bridge: "This is the central role of a higher-order function."
-->

---

<div class="eyebrow">Definition</div>

## A higher-order function receives or returns a function

<div class="hof-tools">
  <div><code>map</code><span>Transform every element</span></div>
  <div><code>filter</code><span>Keep selected elements</span></div>
  <div><code>exists?</code><span>Check whether one element passes</span></div>
  <div><code>for-all?</code><span>Check whether every element passes</span></div>
  <div><code>foldr / foldl</code><span>Combine a list into one result</span></div>
</div>

<!--
Idea: Definición inclusiva: recibe funciones o devuelve una función. Las notas usan ambas formulaciones.
Say: "A higher-order function takes another function as an argument or returns a function as its result."
Bridge: "Three families cover most of today's list processing."
-->

---

<div class="eyebrow">Three questions</div>

## The result shape reveals what each operation does

<div class="operation-shapes">
  <div class="operation-row map-row">
    <b><code>map</code></b>
    <code>'(1 2 3 4)</code>
    <span><code>cuadrado</code><small>transform each</small></span>
    <code>'(1 4 9 16)</code>
    <strong>same length</strong>
  </div>
  <div class="operation-row filter-row">
    <b><code>filter</code></b>
    <code>'(1 2 3 4)</code>
    <span><code>even?</code><small>keep when true</small></span>
    <code>'(2 4)</code>
    <strong>selected elements</strong>
  </div>
  <div class="operation-row fold-row">
    <b><code>foldl</code></b>
    <code>'(1 2 3 4)</code>
    <span><code>+ 0</code><small>combine</small></span>
    <code>10</code>
    <strong>one result</strong>
  </div>
</div>

<!--
Idea: Comparar las formas de salida con el mismo dato de entrada para que la diferencia sea visible antes de estudiar cada función.
Say: "Map transforms every element and preserves the length. Filter keeps only the elements for which the predicate is true. A fold combines the whole list into one result."
Bridge: "We begin with map."
-->

---

<div class="eyebrow">Function map</div>

## Transform every element and preserve the length

```text
(map transform list) -> list
(transform element)  -> element
```

<div class="element-flow">
  <code>'(1 2 3 4 5)</code>
  <strong><code>cuadrado</code></strong>
  <code>'(1 4 9 16 25)</code>
</div>

> One input element produces one output element.

<!--
Idea: Explicar el contrato antes de los ejemplos. map conserva el número de elementos.
Say: "Map calls the transform once for each element and builds a result list of the same length."
Bridge: "The transform may be named or written as a lambda."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Using map</div>

## The transformation determines the result type

```racket
(map cuadrado '(1 2 3 4 5))
; ⇒ (1 4 9 16 25)

(map (lambda (str) (string-append "Hello-" str))
     '("my" "name" "is" "Ana"))
; ⇒ ("Hello-my" "Hello-name" "Hello-is" "Hello-Ana")

(map (lambda (s)
       (string-length (symbol->string s)))
     '(This is a list of symbols))
; ⇒ (4 2 1 4 2 7)
```

<!--
Idea: map no obliga a conservar el tipo de los elementos, solo produce uno por cada entrada.
Say: "Map always preserves the list length, but the transformation may change the type of each element."
Bridge: "Its recursive implementation follows the usual list template."
-->

---

<div class="eyebrow">Recursive implementation</div>

## `mi-map` transforms the first element and recurses

```racket
(define (mi-map f lista)
  (if (null? lista)
      '()
      (cons (f (first lista))
            (mi-map f (rest lista)))))
```

<div class="columns equal week04-cases">
<div><strong>Base case</strong><span>An empty input produces an empty list.</span></div>
<div><strong>General case</strong><span>Transform the first element and attach the transformed rest.</span></div>
</div>

<!--
Idea: Comparar con funciones recursivas de semana 3; la única novedad es (f (first list)).
Say: "The recursion is the familiar list pattern. The function parameter controls what happens to the first element."
Bridge: "Scheme map can also move through several lists in parallel."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Map with several lists</div>

## One element is taken from each list at every position

```racket
(map + '(1 2 3) '(10 20 30))
; ⇒ (11 22 33)

(map cons '(1 2 3) '(10 20 30))
; ⇒ ((1 . 10) (2 . 20) (3 . 30))

(map > '(12 3 40) '(20 0 10))
; ⇒ (#f #t #t)
```

> The input lists have the same length. The transformation receives as many arguments as `map` receives lists.

<!--
Idea: Aclarar la correspondencia por posición y la aridad de la función transformadora.
Say: "With two lists, map takes two elements at each position, so the transform must accept two arguments."
Bridge: "Filter asks a different question: should this element remain in the list?"
-->

---

<div class="eyebrow">Function filter</div>

## Keep the original elements that satisfy a predicate

```text
(filter predicate list) -> list
(predicate element)     -> boolean
```

```racket
(filter even? '(1 2 3 4 5 6 7 8))
; ⇒ (2 4 6 8)

(filter (lambda (pareja) (>= (car pareja) (cdr pareja)))
        '((10 . 4) (2 . 4) (8 . 8) (10 . 20)))
; ⇒ ((10 . 4) (8 . 8))
```

<!--
Idea: Filter no transforma los datos; conserva algunos de los elementos originales.
Say: "The predicate returns a Boolean. Filter keeps the original element when that result is true."
Bridge: "The recursive definition therefore needs two general cases."
-->

---

<div class="eyebrow">Recursive implementation</div>

## `mi-filter` either keeps or skips the first element

```racket
(define (mi-filter pred lista)
  (cond
    ((null? lista) '())
    ((pred (first lista))
     (cons (first lista)
           (mi-filter pred (rest lista))))
    (else
     (mi-filter pred (rest lista)))))
```

<!--
Idea: Las dos ramas difieren solo en si aparece cons. La recursión avanza en ambos casos.
Say: "When the predicate succeeds, cons keeps the first element. Otherwise the function skips it and continues with the rest."
Bridge: "Sometimes we need only a Boolean answer rather than a filtered list."
-->

---

<div class="eyebrow">Predicates over a list</div>

## `exists?` and `for-all?` answer different questions

<div class="comparison-table quantifier-table">
  <div class="header"><b>Function</b><b>Question</b><b>Empty list</b></div>
  <div><strong><code>exists?</code></strong><span>Does at least one element satisfy the predicate?</span><span><code>#f</code></span></div>
  <div><strong><code>for-all?</code></strong><span>Does every element satisfy the predicate?</span><span><code>#t</code></span></div>
</div>

```racket
(exists? even? '(1 2 3 4 5 6)) ; ⇒ #t
(for-all? even? '(2 4 6))       ; ⇒ #t
```

<!--
Idea: Explicar los casos vacíos desde la pregunta lógica, no como algo arbitrario.
Say: "No element can witness existence in an empty list, so exists returns false. No element violates a universal condition, so for-all returns true."
Bridge: "Their recursive definitions mirror or and and."
-->

---

<div class="eyebrow">Recursive definitions</div>

## `or` stops on success, while `and` stops on failure

<div class="columns equal">
<div>

```racket
(define (exists? pred lista)
  (if (null? lista)
      #f
      (or (pred (first lista))
          (exists? pred
                   (rest lista)))))
```

</div>
<div>

```racket
(define (for-all? pred lista)
  (or (null? lista)
      (and (pred (first lista))
           (for-all? pred
                     (rest lista)))))
```

</div>
</div>

<!--
Idea: Recordar que or y and son formas especiales y pueden evitar la llamada recursiva.
Say: "Or stops when it finds one success. And stops when it finds one failure. Their short-circuit evaluation avoids unnecessary recursive calls."
Bridge: "Map and filter return lists, and quantifiers return Booleans. A fold can return any accumulated value."
-->

---

<!-- _class: section -->

<div class="eyebrow">05</div>

# `foldr` and `foldl`

<p class="lead">Many elements become one result. <code>foldr</code> and <code>foldl</code> differ in the order in which they combine elements.</p>

<!--
Idea: Presentar fold como reducción de una lista a un único resultado.
Say: "A fold traverses a list and combines its elements into one result. The direction affects the sequence of calls."
Bridge: "We begin with foldr."
-->

---

<div class="eyebrow">Function foldr</div>

## Combine from right to left

```text
(foldr combine base list) -> result
(combine element result)  -> result
```

<div class="fold-model">
  <code>'(1 2 3)</code>
  <span>with base <code>0</code></span>
  <strong><code>(combine 1 (combine 2 (combine 3 0)))</code></strong>
</div>

> The first argument of `combine` comes from the list. The second is the result accumulated from the right.

<!--
Idea: Los nombres element y result aclaran el papel de cada parámetro.
Say: "Foldr combines the last element with the base first. Each earlier element then combines with the accumulated result."
Bridge: "Addition makes the sequence easy to follow."
-->

---

<div class="eyebrow">Foldr call sequence</div>

## The accumulated result moves to the left

```racket
(define (suma dato resultado)
  (+ dato resultado))

(foldr suma 0 '(1 2 3)) ; ⇒ 6
```

<div class="fold-steps">
  <div><code>(suma 3 0)</code><strong>3</strong></div>
  <div><code>(suma 2 3)</code><strong>5</strong></div>
  <div><code>(suma 1 5)</code><strong>6</strong></div>
</div>

<!--
Idea: Recorrer los tres pasos y señalar cómo el resultado pasa al segundo parámetro de la siguiente llamada.
Say: "Three combines with the base. Then two combines with three, and one combines with five."
Bridge: "A non-commutative function makes the direction visible."
-->

---

<div class="eyebrow">Order matters</div>

## String concatenation exposes the nesting

```racket
(foldr string-append "****"
       '("hello" "how" "are-you"))
; ⇒ "hellohoware-you****"
```

```text
(string-append "are-you" "****")
(string-append "how" "are-you****")
(string-append "hello" "howare-you****")
```

> Addition hides the direction because it is commutative. String concatenation does not.

<!--
Idea: Usar strings para que el alumnado vea el efecto del orden que la suma oculta.
Say: "With addition, both directions look equivalent. String append reveals exactly where each element is placed."
Bridge: "The recursive definition of foldr creates this nesting directly."
-->

---

<div class="eyebrow">Recursive implementation</div>

## `mi-foldr` combines after the recursive call

```racket
(define (mi-foldr combina base lista)
  (if (null? lista)
      base
      (combina (first lista)
               (mi-foldr combina base
                         (rest lista)))))
```

```racket
(foldr * 1 '(1 2 3 4 5 6 7 8)) ; ⇒ 40320
(foldr cons '() '(1 2 3 4))     ; ⇒ (1 2 3 4)
```

<!--
Idea: La llamada recursiva ocupa el segundo argumento de combine, por eso la combinación se construye de derecha a izquierda.
Say: "The recursive call computes the result for the rest of the list. The first element is combined only after that result exists."
Bridge: "Foldl uses the same combine profile but changes the sequence."
-->

---

<div class="eyebrow">Function foldl</div>

## Left-to-right calls produce a different nesting

<div class="columns equal">
<div>

### `foldr`

```racket
(foldr string-append "****"
       '("hello" "how" "are-you"))
; ⇒ "hellohoware-you****"

(foldr cons '() '(1 2 3 4))
; ⇒ (1 2 3 4)
```

</div>
<div>

### `foldl`

```racket
(foldl string-append "****"
       '("hello" "how" "are-you"))
; ⇒ "are-youhowhello****"

(foldl cons '() '(1 2 3 4))
; ⇒ (4 3 2 1)
```

</div>
</div>

> We will implement `foldl` when we study tail recursion.

<!--
Idea: No decir solo que recorre al revés. Comparar resultados con operaciones no conmutativas.
Say: "Foldl processes the list from left to right, but combine still receives the element first and the accumulated result second."
Bridge: "Now we can replace explicit recursion with combinations of these reusable traversals."
-->

---

<!-- _class: section -->

<div class="eyebrow">06</div>

# Composition of higher-order functions

<p class="lead">Each result becomes the next input. The code states the transformation while higher-order functions perform the traversal.</p>

<!--
Idea: Composición como tubería de datos, no como lista de llamadas aisladas.
Say: "Each higher-order function performs one list operation. Its result becomes the input of the next operation."
Bridge: "A recursive function can often be expressed as one call to map."
-->

---

<div class="eyebrow">Function suma-n</div>

## `map` replaces explicit recursion

<div class="columns equal">
<div>

### Recursive version

```racket
(define (suma-n n lista)
  (if (null? lista)
      '()
      (cons (+ (first lista) n)
            (suma-n n (rest lista)))))
```

</div>
<div>

### Higher-order version

```racket
(define (suma-n n lista)
  (map (lambda (x)
         (+ x n))
       lista))
```

</div>
</div>

```racket
(suma-n 10 '(1 2 3 4)) ; ⇒ (11 12 13 14)
```

<!--
Idea: La lambda captura n, conectando composición con closures.
Say: "Map provides the traversal. The lambda provides the transformation and captures n from the call to suma-n."
Bridge: "Foldr provides the traversal when the desired result is one accumulated value."
-->

---

<div class="eyebrow">Function suma-parejas</div>

## `foldr` accumulates one result

```racket
(define (suma-parejas lista-parejas)
  (foldr (lambda (pareja resultado)
           (+ (car pareja)
              (cdr pareja)
              resultado))
         0
         lista-parejas))

(suma-parejas
  (list (cons 3 6) (cons 2 9)
        (cons -1 8) (cons 9 3)))
; ⇒ 39
```

<!--
Idea: Identificar los tres papeles: combine, base y lista.
Say: "The lambda adds both components of the current pair to the accumulated result. Zero is the initial accumulated value."
Bridge: "Several higher-order functions can form one processing pipeline."
-->

---

<div class="eyebrow">Composition pipeline</div>

## Transform first, then reduce or filter

<div class="columns equal">
<div>

### Add `n`, then total

```racket
(define (suma-n-total n lista)
  (foldr + 0
    (map (lambda (x) (+ x n))
         lista)))

(suma-n-total 100 '(1 2 3 4))
; ⇒ 410
```

</div>
<div>

### Add each pair, then count

```racket
(define (cuenta-mayores-que n lista-parejas)
  (length
    (filter (lambda (x) (> x n))
      (map (lambda (pareja)
             (+ (car pareja) (cdr pareja)))
           lista-parejas))))
```

</div>
</div>

<!--
Idea: Leer de dentro hacia fuera: map produce datos intermedios y fold/filter consumen ese resultado.
Say: "Read each pipeline from the inside out. Map produces an intermediate list, and the outer operation consumes that list."
Bridge: "The final example composes a quantifier inside a filter predicate."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Nested higher-order functions</div>

## Keep the words that contain a character

```racket
(define (letra-en-pal? caracter palabra)
  (exists? (lambda (c)
             (equal? c caracter))
           (string->list palabra)))

(define (contienen-letra caracter lista-pal)
  (filter (lambda (pal)
            (letra-en-pal? caracter pal))
          lista-pal))

(contienen-letra #\a
  '("In" "a" "place" "of" "La" "Mancha"))
; ⇒ ("a" "place" "La" "Mancha")
```

<div class="composition-order week04-final-flow">
  <span><code>string->list</code> exposes the characters</span>
  <span><code>exists?</code> tests one word</span>
  <span><code>filter</code> selects the words</span>
</div>

<!--
Idea: Terminar aplicando tres niveles de abstracción, sin diapositiva de resumen.
Say: "String-to-list exposes the characters. Exists checks one word, and filter uses that predicate to select the words."
Bridge: "This is the style of functional decomposition we will keep using in the next classes."
-->
