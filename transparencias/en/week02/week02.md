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
<div class="week-marker">Week 2</div>

# Recursion, pairs, and lists

<p class="lead">How Scheme builds recursive solutions and composite data</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

---

<div class="eyebrow">Today</div>

## Three connected ideas

<div class="sequence week02-agenda">
  <div><b>1 · RECURSION</b><span>Solve a smaller version of the same problem</span></div>
  <div><b>2 · PAIRS</b><span>Combine two values into one immutable object</span></div>
  <div><b>3 · LISTS</b><span>Build recursive structures from pairs</span></div>
</div>

> The same recursive idea appears in both programs and data.

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Recursion

<p class="lead">Trust the recursive call: ask it to solve a smaller problem, then use the result it returns.</p>

---

<div class="eyebrow">Recursive definitions</div>

## Two cases describe the function

<div class="recursive-pattern">
  <div class="pattern-case">
    <span class="pattern-label">Base case</span>
    <div class="pattern-equation">The simplest input</div>
    <p class="pattern-note">Return its result directly. No recursive call is needed.</p>
  </div>
  <div class="pattern-case general">
    <span class="pattern-label">General case</span>
    <div class="pattern-equation">A smaller call + the remaining work</div>
    <p class="pattern-note">The recursive call must receive a simpler version of the problem.</p>
  </div>
</div>

---

<div class="eyebrow">Function suma-hasta</div>

## Sum the numbers from `0` to `x`

<div class="columns equal">
<div>

```racket
(suma-hasta 5)
; ⇒ 0 + 1 + 2 + 3 + 4 + 5
; ⇒ 15
```

The smaller problem is the sum up to `4`.

</div>
<div class="sum-stack">
  <span>5</span><span>4</span><span>3</span><span>2</span><span>1</span><span>0</span>
  <strong>15</strong>
</div>
</div>

---

<div class="eyebrow">Function suma-hasta</div>

## Use the result of the smaller call

<div class="recursive-result-flow">
  <div class="result-step">
    <span class="pair-label">Original problem</span>
    <code>(suma-hasta 5)</code>
    <strong class="example-result">15</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">Recursive call</span>
    <code>(suma-hasta 4)</code>
    <strong>10</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">Total result</span>
    <span class="step-answer">Add the remaining number</span>
    <code>(+ 10 5)</code>
    <strong>15</strong>
  </div>
</div>

---

<!-- _class: semantic -->

<div class="semantic-grid">
<div class="semantic-copy">

<div class="eyebrow">Rely on recursion</div>

## Treat the recursive result as known

<p>Do not trace every nested call while designing the function. Decide what the smaller call should return and use that value.</p>

</div>
<div class="evaluation-ladder">
  <code>(+ (suma-hasta (- 5 1)) 5)</code>
  <span>↓ simplify the argument</span>
  <code>(+ (suma-hasta 4) 5)</code>
  <span>↓ trust the recursive call</span>
  <code>(+ 10 5)</code>
  <strong>15</strong>
</div>
</div>

---

<div class="eyebrow">Function suma-hasta</div>

## The general case

<div class="columns equal">
<div>

```racket
(define (suma-hasta x)
  (+ (suma-hasta (- x 1))
     x))
```

</div>
<div>

### Smaller problem

`(- x 1)` moves closer to the simplest input.

### Remaining work

Add `x` to the result returned by recursion.

</div>
</div>

---

<div class="eyebrow">Function suma-hasta</div>

## The base case completes the definition

<div class="columns equal">
<div>

```racket
(define (suma-hasta x)
  (if (= x 0)
      0
      (+ (suma-hasta (- x 1))
         x)))
```

</div>
<div class="base-case-visual">
  <span class="pair-label">Simplest input</span>
  <code>(suma-hasta 0)</code>
  <strong>0</strong>
  <p>No addition and no recursive call.</p>
</div>
</div>

---

<div class="eyebrow">Function alfabeto-hasta</div>

## Build a string up to one character

```racket
(alfabeto-hasta #\h)
; ⇒ "abcdefgh"
```

<div class="alphabet-strip">
  <span>a</span><span>b</span><span>c</span><span>d</span><span>e</span><span>f</span><span>g</span><span class="current">h</span>
</div>

The smaller call builds the string up to the previous character.

---

<div class="eyebrow">Function alfabeto-hasta</div>

## From the smaller string to the answer

<div class="recursive-result-flow alphabet-flow">
  <div class="result-step">
    <span class="pair-label">Original problem</span>
    <code>(alfabeto-hasta #\h)</code>
    <strong class="example-result">"abcdefgh"</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">Recursive call</span>
    <code>(alfabeto-hasta #\g)</code>
    <strong>"abcdefg"</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">Total result</span>
    <span class="step-answer">Append the current character</span>
    <code>(string-append "abcdefg" "h")</code>
    <strong>"abcdefgh"</strong>
  </div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `alfabeto-hasta`

<div class="columns equal">
<div>

```racket
(define (anterior char)
  (integer->char
    (- (char->integer char) 1)))

(define (alfabeto-hasta char)
  (if (equal? char #\a)
      "a"
      (string-append
        (alfabeto-hasta
          (anterior char))
        (string char))))
```

</div>
<div>

### Base case

The alphabet up to `#\a` is simply `"a"`.

### General case

Build the string up to the previous character, then append the current one.

</div>
</div>

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Recursion and lists

<p class="lead">The rest of a non-empty list is the smaller problem. Recursion can process everything except the first element.</p>

---

<div class="eyebrow">List selectors</div>

## `first` and `rest`

<div class="columns equal">
<div>

```racket
(define lista1 '(1 2 3 4))

(first lista1) ; ⇒ 1
(rest lista1)  ; ⇒ (2 3 4)
```

</div>
<div class="list-split">
  <div class="list-row"><span class="list-bracket">(</span><span class="atom head">1</span><span class="atom pass">2</span><span class="atom pass">3</span><span class="atom pass">4</span><span class="list-bracket">)</span></div>
  <div class="split-labels"><span><code>first</code></span><span><code>rest</code></span></div>
</div>
</div>

---

<div class="eyebrow">Function suma-lista</div>

## Sum every number in a list

```racket
(suma-lista '(12 3 5 1 8))
; ⇒ 29
```

<div class="list-row sum-list-row">
  <span class="list-bracket">(</span>
  <span class="atom head">12</span><span class="atom pass">3</span><span class="atom pass">5</span><span class="atom pass">1</span><span class="atom pass">8</span>
  <span class="list-bracket">)</span><span class="sum-equals">= 29</span>
</div>

---

<div class="eyebrow">Function suma-lista</div>

## The recursive call handles the rest

<div class="recursive-result-flow">
  <div class="result-step">
    <span class="pair-label">Original problem</span>
    <code>(suma-lista<br>'(12 3 5 1 8))</code>
    <strong class="example-result">29</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">Recursive call</span>
    <code>(suma-lista<br>'(3 5 1 8))</code>
    <strong>17</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">Total result</span>
    <span class="step-answer">Add the first element</span>
    <code>(+ 12 17)</code>
    <strong>29</strong>
  </div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `suma-lista`

<div class="columns equal">
<div>

```racket
(define (suma-lista lista)
  (if (null? lista)
      0
      (+ (first lista)
         (suma-lista
           (rest lista)))))
```

</div>
<div>

### General case

Add the first number to the sum returned for the rest.

### Base case

The sum of an empty list is `0`.

</div>
</div>

---

<div class="eyebrow">Function veces</div>

## Count an identifier in a list

```racket
(veces '(a b a a b b) 'a)
; ⇒ 3
```

<div class="count-strip">
  <span class="match">a</span><span>b</span><span class="match">a</span><span class="match">a</span><span>b</span><span>b</span>
</div>

For each first element, decide whether to add `1` to the recursive result.

---

<div class="eyebrow">Function veces</div>

## Two possibilities in the general case

<div class="columns equal filter-cases">
<div class="filter-case">

### The first element matches

```racket
(+ 1
   (veces (rest lista) id))
```

The first element contributes one occurrence.

</div>
<div class="filter-case">

### The first element differs

```racket
(veces (rest lista) id)
```

The result for the rest is already the total result.

</div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `veces`

```racket
(define (veces lista id)
  (cond
    ((null? lista) 0)
    ((equal? (first lista) id)
      (+ 1 (veces (rest lista) id)))
    (else
      (veces (rest lista) id))))
```

The empty list contains zero occurrences.

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Composite data types in Scheme

<p class="lead">A pair combines two values. Pairs build larger immutable structures from smaller values.</p>

---

<div class="eyebrow">The pair data type</div>

## Build a pair with `cons`

<div class="columns equal">
<div>

```racket
(cons 1 2)
; ⇒ (1 . 2)

(define c (cons 1 2))
```

The dot separates the left and right parts.

</div>
<div class="pair-cell large">
  <div><span>car</span><strong>1</strong></div>
  <div><span>cdr</span><strong>2</strong></div>
</div>
</div>

---

<div class="eyebrow">cons and quote</div>

## Construction and literal data

<div class="columns equal">
<div>

### `cons` evaluates its arguments

```racket
(define a 1)
(define b 2)

(cons a b)
; ⇒ (1 . 2)
```

</div>
<div>

### `quote` preserves the symbols

```racket
'(a . b)
; ⇒ (a . b)

'(1 . 2)
; ⇒ (1 . 2)
```

</div>
</div>

---

<div class="eyebrow">Pair selectors</div>

## `car` returns the left part, `cdr` the right

<div class="columns equal">
<div>

```racket
(define c (cons 1 2))

(car c) ; ⇒ 1
(cdr c) ; ⇒ 2
```

```racket
(car (cons x y)) = x
(cdr (cons x y)) = y
```

</div>
<div class="pair-selectors">
  <div class="pair-cell"><div><strong>1</strong></div><div><strong>2</strong></div></div>
  <div class="selector-labels"><span>car</span><span>cdr</span></div>
</div>
</div>

---

<div class="eyebrow">Pairs accept any values</div>

## Type and immutability

<div class="columns equal">
<div>

```racket
(pair? 3)          ; ⇒ #f
(pair? (cons 3 4)) ; ⇒ #t

(define c (cons 'hello #f))
(car c) ; ⇒ 'hello
(cdr c) ; ⇒ #f
```

</div>
<div>

### Immutable objects

Functional programs create a new pair instead of changing the contents of an existing pair.

Mutation belongs to the imperative programming paradigm, which we will study later.

</div>
</div>

---

<div class="eyebrow">First-class objects</div>

## What can we do with a pair?

<div class="four-up">
  <div><b>ASSIGN</b><span>Store it in a variable</span></div>
  <div><b>PASS</b><span>Use it as an argument</span></div>
  <div><b>RETURN</b><span>Produce it as a result</span></div>
  <div><b>NEST</b><span>Place it inside another structure</span></div>
</div>

Pairs are first-class objects because all four operations are possible.

---

<div class="eyebrow">Pairs as arguments and results</div>

## Add two pairs component by component

<div class="columns equal">
<div>

```racket
(define (suma-parejas p1 p2)
  (cons
    (+ (car p1) (car p2))
    (+ (cdr p1) (cdr p2))))
```

</div>
<div class="pair-addition">
  <code>'(1 . 2)</code><span>+</span><code>'(3 . 4)</code>
  <span class="pair-down">↓</span>
  <code class="pair-sum">'(4 . 6)</code>
</div>
</div>

---

<div class="eyebrow">One function, several data types</div>

## Select the operation at runtime

```racket
(define (suma x y)
  (cond
    ((and (number? x) (number? y))
      (+ x y))
    ((and (pair? x) (pair? y))
      (suma-parejas x y))
    ((and (string? x) (string? y))
      (string-append x y))
    (else 'error)))
```

The predicates decide which operation fits the arguments.

---

<div class="eyebrow">Nested pairs</div>

## A pair can contain other pairs

<div class="columns equal">
<div>

```racket
(define p
  (cons (cons 1 2)
        (cons 3 4)))
```

The outer pair contains two inner pairs.

</div>
<div>

<img class="note-image pair-note-image" src="../../../notas-clase/semana02/imagenes/pareja-pareja2.png" alt="Box-and-pointer diagram of one pair containing two pairs">

</div>
</div>

---

<div class="eyebrow">Box-and-pointer diagrams</div>

## Read the expression from inside to outside

<div class="columns equal">
<div>

```racket
(define p
  (cons
    (cons 1
      (cons 3 4))
    2))
```

1. Build `(cons 3 4)`.
2. Use it as the right part of `(cons 1 ...)`.
3. Place that pair on the left of the outer pair.

</div>
<div class="inside-out">
  <code>(cons 3 4)</code>
  <span>↓</span>
  <code>(cons 1 <b>pair</b>)</code>
  <span>↓</span>
  <code>(cons <b>pair</b> 2)</code>
</div>
</div>

---

<!-- _class: question -->

<div class="eyebrow">Check your understanding</div>

## Which `car` and `cdr` expression returns `3`?

<div class="columns equal">
<div>

```racket
(define p
  (cons
    (cons 1 (cons 3 4))
    2))

(define p2
  (cons 5 (cons p 6)))
```

</div>
<div>

<p class="prompt">Draw the pairs first. Then follow one pointer at a time from <code>p2</code> to the value <code>3</code>.</p>

</div>
</div>

---

<div class="eyebrow">Functions c????r</div>

## A compact name for nested selectors

<div class="columns equal">
<div>

```racket
(cdr (cdr (car p)))
```

The selectors execute from the inside out: `car`, then `cdr`, then `cdr`.

</div>
<div>

```racket
(cddar p)
```

Read the letters between `c` and `r` from right to left.

There are 30 combinations with one to four selector letters.

</div>
</div>

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Lists in Scheme

<p class="lead">A list is a chain of pairs. Each pair stores one element and the rest of the list.</p>

---

<div class="eyebrow">Lists and pairs</div>

## Test the relationship

<div class="columns equal">
<div>

```racket
(define p1 (cons 1 2))

(pair? p1) ; ⇒ #t
(list? p1) ; ⇒ #f
```

A general pair does not have to be a list.

</div>
<div>

```racket
(define lista '(1 2 3))

(list? lista) ; ⇒ #t
(pair? lista) ; ⇒ #t
```

A non-empty list starts with a pair.

</div>
</div>

---

<!-- _class: semantic -->

<div class="semantic-grid">
<div class="semantic-copy">

<div class="eyebrow">Recursive definition</div>

## Two forms make a list

<p>Every non-empty list contains one item and another list. The definition ends at the empty list.</p>

</div>
<div class="list-definition">
  <div class="definition-case"><strong>Empty list</strong><code>'()</code></div>
  <div class="definition-or">or</div>
  <div class="definition-case"><strong>Pair</strong><span><code>car</code> = first item</span><span><code>cdr</code> = rest of the list</span></div>
</div>
</div>

---

<div class="eyebrow">The one-element list</div>

## `(1)` is one pair ending in `'()`

<div class="columns equal">
<div>

```racket
(cons 1 '())
; ⇒ '(1)
```

- The left part stores `1`.
- The right part stores the empty list.

```racket
(pair? (cons 1 '())) ; ⇒ #t
(list? (cons 1 '())) ; ⇒ #t
```

</div>
<div>

<img class="note-image one-list-image" src="../../../notas-clase/semana02/imagenes/pareja-lista.png" alt="Box-and-pointer diagram of a one-element list">

</div>
</div>

---

<div class="eyebrow">The list (1 2 3)</div>

## Every `cdr` contains another list

```racket
(cons 1
  (cons 2
    (cons 3
      '())))
```

<img class="sketch-wide list-note-image" src="../../../notas-clase/semana02/imagenes/lista.png" alt="Box-and-pointer diagram of the list 1 2 3">

---

<div class="eyebrow">The empty list</div>

## The endpoint of every proper list

<div class="columns equal">
<div>

```racket
(list? '())   ; ⇒ #t
(pair? '())   ; ⇒ #f
(symbol? '()) ; ⇒ #f
(null? '())   ; ⇒ #t
```

</div>
<div class="empty-list-visual">
  <code>'()</code>
  <span>terminates the chain</span>
  <p>Racket also defines <code>null</code> as the empty list.</p>
</div>
</div>

---

<div class="eyebrow">Lists with composite elements</div>

## An association list stores key-value pairs

<div class="columns equal">
<div>

```racket
(list
  (cons 'a 1)
  (cons 'b 2)
  (cons 'c 3))
```

</div>
<div class="association-list">
  <div><code>a</code><span>1</span></div>
  <div><code>b</code><span>2</span></div>
  <div><code>c</code><span>3</span></div>
</div>
</div>

The outer list links three elements. Each element is itself a pair.

---

<div class="eyebrow">Lists of lists</div>

## A list element can be another list

<div class="columns equal">
<div>

```racket
(define lista
  (list 1
        (list 1 2 3)
        3))
```

</div>
<div>

```racket
(define lista
  '(1 (1 2 3) 3))
```

Both definitions create the same nested list.

</div>
</div>

<div class="nested-list-strip"><span>1</span><span class="nested"><i>1</i><i>2</i><i>3</i></span><span>3</span></div>

---

<!-- _class: question -->

<div class="eyebrow">Reverse the diagram</div>

## Which Scheme expression builds this structure?

<img class="sketch-wide complex-list-image" src="../../../notas-clase/semana02/imagenes/lista-complicada.png" alt="Complex box-and-pointer diagram to translate into Scheme">

<p class="prompt">Identify the outer list first. Then translate each composite element.</p>

---

<div class="eyebrow">Reverse the diagram</div>

## One expression for the structure

```racket
(define p1
  (list
    (cons (cons 1 2)
          (cons 3 4))
    (list 5 6
          (cons 7
                (cons 8 9)))
    10))
```

The outer constructor is `list`. The inner structures use `list` or `cons` according to how each chain ends.

---

<div class="eyebrow">Interpreter output</div>

## Proper list notation hides part of the pair structure

<div class="columns equal">
<div>

```racket
(define p
  (cons 1 (cons 2 3)))

p
; ⇒ (1 2 . 3)
```

</div>
<div>

```racket
(print-pareja p)
; ⇒ (1 . (2 . 3))
```

The second representation makes every pair explicit.

</div>
</div>

---

<div class="eyebrow">Abstraction</div>

## Use list operations for list problems

<div class="columns equal">
<div>

### List abstraction

```racket
(first lista)
(rest lista)
(list-ref lista n)
(cons dato lista)
```

</div>
<div>

### Pair implementation

`car` and `cdr` explain how lists are represented, but most list functions should work at the list level.

> Choose operations that express the problem clearly.

</div>
</div>
