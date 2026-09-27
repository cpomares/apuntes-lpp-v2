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
<div class="week-marker">Week 3</div>

# Building lists with recursion

<p class="lead">Recursive lists and functions as values in Scheme</p>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

---

<div class="eyebrow">Today</div>

## Two main ideas

<div class="columns equal">
<div>

### Building lists

- Design recursive functions from examples
- Join, reverse, create, and filter lists

</div>
<div>

### Using functions as values

- Create functions with `lambda`
- Pass a function as an argument
- Use `apply`

</div>
</div>

---

<!-- _class: section -->

<div class="eyebrow">01</div>

# Recursive functions that build lists

<p class="lead">Start with a smaller problem. The recursive call solves it, then the current call uses its result.</p>

---

<div class="eyebrow">Designing recursive functions</div>

## Three questions for the general case

<div class="sequence">
  <div><b>1 · EXAMPLE</b><span>What result do we want for one concrete input?</span></div>
  <div><b>2 · RECURSIVE CALL RESULT</b><span>What useful result can a recursive call give us?</span></div>
  <div><b>3 · TOTAL RESULT</b><span>How can we use that result to build the answer?</span></div>
</div>

> After the general case, find the simplest input that needs no recursive call. That is the base case.

---

<div class="eyebrow">Function mi-append</div>

## The smaller problem

<div class="columns equal">
<div>

### Original problem

```racket
(mi-append
  '(a b c)
  '(d e f))
```

</div>
<div>

### Smaller problem

```racket
(mi-append
  '(b c)
  '(d e f))
```

</div>
</div>

> Remove the first element from the first list. Keep the second list unchanged.

---

<div class="eyebrow">Function mi-append</div>

## From the recursive call to the total result

<div class="recursive-result-flow">
  <div class="result-step">
    <span class="pair-label">1 · Example</span>
    <span class="step-question">What result do we want?</span>
    <code>(mi-append '(a b c)<br>&nbsp;&nbsp;'(d e f))</code>
    <strong class="example-result">'(a b c d e f)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">2 · Recursive call result</span>
    <code>(mi-append '(b c)<br>&nbsp;&nbsp;'(d e f))</code>
    <strong>'(b c d e f)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">3 · Total result</span>
    <span class="step-answer">Add <code>a</code> at the front</span>
    <code>(cons 'a<br>&nbsp;&nbsp;'(b c d e f))</code>
    <strong>'(a b c d e f)</strong>
  </div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `mi-append`

<div class="columns equal">
<div>

```racket
(define (mi-append l1 l2)
  (if (null? l1)
      l2
      (cons
        (first l1)
        (mi-append
          (rest l1)
          l2))))
```

</div>
<div>

### General case

Make the first list smaller and keep the second list unchanged.

Use `cons` to add the first element to the recursive result.

### Base case

When the first list is empty, return the second list.

</div>
</div>

---

<div class="eyebrow">Function mi-reverse</div>

## The first element waits

<div class="recursive-result-flow">
  <div class="result-step">
    <span class="pair-label">1 · Example</span>
    <span class="step-question">What result do we want?</span>
    <code>(mi-reverse '(1 2 3 4))</code>
    <strong class="example-result">'(4 3 2 1)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">2 · Recursive call result</span>
    <code>(mi-reverse '(2 3 4))</code>
    <strong>'(4 3 2)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">3 · Total result</span>
    <span class="step-answer">Add <code>1</code> at the end</span>
    <code>(añade-al-final 1 '(4 3 2))</code>
    <strong>'(4 3 2 1)</strong>
  </div>
</div>

---

## Reverse the rest first

<div class="columns equal">
<div>

```racket
(mi-reverse '(1 2 3 4))
```

The smaller call gives:

```racket
(mi-reverse '(2 3 4))
; ⇒ (4 3 2)
```

</div>
<div>

We need to add `1` at the end:

```racket
(define (añade-al-final dato lista)
  (append lista
          (list dato)))
```

```racket
(añade-al-final 1 '(4 3 2))
; ⇒ (4 3 2 1)
```

</div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `mi-reverse`

```racket
(define (mi-reverse lista)
  (if (null? lista)
      '()
      (añade-al-final
        (first lista)
        (mi-reverse (rest lista)))))
```

The base case is the empty list. Its reverse is also the empty list.

---

<div class="eyebrow">Function lista-desde</div>

## A list from `x` down to `1`

<p class="sketch-intro">We answer the three questions with one concrete example.</p>

<div class="recursive-result-flow">
  <div class="result-step">
    <span class="pair-label">1 · Example</span>
    <span class="step-question">What result do we want?</span>
    <code>(lista-desde 5)</code>
    <strong class="example-result">'(5 4 3 2 1)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step trusted-result">
    <span class="pair-label">2 · Recursive call result</span>
    <span class="step-question">What result does the recursive call give us?</span>
    <code>(lista-desde 4)</code>
    <strong>'(4 3 2 1)</strong>
  </div>
  <span class="result-arrow">→</span>
  <div class="result-step total-solution">
    <span class="pair-label">3 · Total result</span>
    <span class="step-question">How do we obtain the total result?</span>
    <span class="step-answer">Add <code>5</code> at the front</span>
    <code>(cons 5 '(4 3 2 1))</code>
    <strong>'(5 4 3 2 1)</strong>
  </div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `lista-desde`

<div class="columns equal">
<div>

```racket
(define (lista-desde x)
  (if (= x 1)
      '(1)
      (cons x
            (lista-desde
              (- x 1)))))
```

</div>
<div>

### General case

Build the list from `x - 1` down to `1`. Add `x` at the front.

### Base case

When `x` is `1`, return `'(1)`.

</div>
</div>

---

<div class="eyebrow">Function filtra-pares</div>

## Keep only the even numbers

<p class="sketch-intro"><code>filtra-pares</code> receives a list and returns a new list containing only its even elements.</p>

<div class="filter-example">
  <div class="filter-call"><code>(filtra-pares '(1 2 3 4 5 6))</code></div>
  <div class="list-row filter-input">
    <span class="list-label">Input</span>
    <span class="list-bracket">(</span>
    <span class="atom skip">1</span><span class="atom keep">2</span>
    <span class="atom skip">3</span><span class="atom keep">4</span>
    <span class="atom skip">5</span><span class="atom keep">6</span>
    <span class="list-bracket">)</span>
  </div>
  <div class="filter-key"><code>even?</code><span class="skip-key">#f: skip</span><span class="keep-key">#t: keep</span></div>
  <span class="filter-arrow">↓</span>
  <div class="list-row filter-output">
    <span class="list-label">Result</span>
    <span class="list-bracket">(</span>
    <span class="atom keep">2</span><span class="atom keep">4</span><span class="atom keep">6</span>
    <span class="list-bracket">)</span>
  </div>
</div>

---

<div class="eyebrow">Function filtra-pares</div>

## Two cases for the first element

<div class="columns equal filter-cases">
<div class="filter-case">

### It is even

<p class="case-input"><code>(filtra-pares '(2 3 4 5 6))</code></p>

<span class="case-label">Recursive call</span>

```racket
(filtra-pares '(3 4 5 6))
; ⇒ '(4 6)
```

<p class="trusted-note">Result of the recursive call: <code>'(4 6)</code></p>

```racket
(cons 2 '(4 6))
; ⇒ '(2 4 6)
```

</div>
<div class="filter-case">

### It is odd

<p class="case-input"><code>(filtra-pares '(1 2 3 4 5 6))</code></p>

<span class="case-label">Recursive call</span>

```racket
(filtra-pares '(2 3 4 5 6))
; ⇒ '(2 4 6)
```

<p class="trusted-note">Result of the recursive call: <code>'(2 4 6)</code></p>

The first element is odd, so this recursive result is already the total solution.

</div>
</div>

---

<div class="eyebrow">Complete definition</div>

## Function `filtra-pares`

```racket
(define (filtra-pares lista)
  (cond
    ((null? lista) '())
    ((even? (first lista))
      (cons (first lista)
            (filtra-pares (rest lista))))
    (else
      (filtra-pares (rest lista)))))
```

```racket
(filtra-pares '(1 2 3 4 5 6))
; ⇒ '(2 4 6)
```

---

<!-- _class: section -->

<div class="eyebrow">02</div>

# Functions with a variable number of arguments

<p class="lead">Extra arguments form a list. A dot in the parameter list collects them.</p>

---

## Two forms with variable arguments

<div class="columns equal">
<div>

### Required arguments first

```racket
(define (f x y . extras)
  <body>)

(f 1 2 3 4 5)
```

`x = 1`, `y = 2` and `extras = (3 4 5)`.

</div>
<div>

### All arguments in one list

```racket
(define (g . args)
  <body>)

(g 1 2 3 4)
```

`args` contains `(1 2 3 4)`.

</div>
</div>

---

<div class="eyebrow">Example</div>

## Function `mi-suma`

```racket
(define (mi-suma x y . lista-nums)
  (if (null? lista-nums)
      (+ x y)
      (+ x (+ y
              (suma-lista lista-nums)))))
```

Can this kind of function call itself recursively?

> The next call needs separate arguments, but the remaining values are inside a list.

---

<!-- _class: section -->

<div class="eyebrow">03</div>

# Functions as first-class data types

<p class="lead">Functions are first-class values. We can use them wherever we use other values.</p>

---

## What does “first-class” mean?

<div class="four-up">
  <div><b>SAVED</b><span>Give it a name</span></div>
  <div><b>PASSED</b><span>Give it to another function</span></div>
  <div><b>RETURNED</b><span>Return it from a function</span></div>
  <div><b>STORED</b><span>Place it inside a data structure</span></div>
</div>

This week we focus on naming functions and passing them as arguments.

---

<div class="eyebrow">The lambda special form</div>

## `lambda` creates a function

<div class="columns equal">
<div>

```racket
(lambda (<arg1> ... <argn>)
  <body>)
```

The expression creates a procedure without giving it a name.

</div>
<div>

```racket
(lambda (x)
  (* x x))
; ⇒ #<procedure>
```

This procedure receives a number and returns its square.

</div>
</div>

---

<div class="eyebrow">A lambda expression</div>

## An anonymous function at runtime

<p class="sketch-intro">Scheme evaluates the <code>lambda</code> expression while the program runs. The result is a procedure value with no name.</p>

<div class="lambda-runtime-flow">
  <div class="lambda-expression"><code>(lambda (x) (* x x))</code></div>
  <div class="lambda-arrow"><span>evaluated at runtime</span>→</div>
  <div class="procedure-value"><strong>#&lt;procedure&gt;</strong><span>anonymous function</span></div>
  <div class="lambda-use"><span class="pair-label">Direct call</span><code>((lambda (x) (* x x)) 5)</code><span>⇒</span><strong>25</strong></div>
</div>

---

## Name or call a lambda

<div class="columns equal">
<div>

### Give it a name

```racket
(define f
  (lambda (x)
    (* x x)))

(f 3)
; ⇒ 9
```

</div>
<div>

### Call it directly

```racket
((lambda (x)
   (* x x))
 3)
; ⇒ 9
```

</div>
</div>

---

<div class="eyebrow">Syntactic sugar</div>

## Two ways to write the same definition

<div class="columns equal">
<div>

```racket
(define (cuadrado x)
  (* x x))
```

</div>
<div>

```racket
(define cuadrado
  (lambda (x)
    (* x x)))
```

</div>
</div>

The first form is a shorter way to write the second one.

---

## A name can refer to a procedure

<div class="columns equal name-procedure">
<div>

```racket
(define suma +)
(suma 1 2 3 4)
; ⇒ 10
```

```racket
(procedure? suma)
; ⇒ #t

(procedure? '+)
; ⇒ #f
```

The quote changes the value. `'+` is a symbol, not a function.

</div>
<div>

<div class="alias-flow">
  <div class="alias-name"><code>+</code><span>original name</span></div>
  <span class="alias-arrow">→</span>
  <div class="alias-procedure"><strong>#&lt;procedure:+&gt;</strong></div>
  <span class="alias-arrow">←</span>
  <div class="alias-name"><code>suma</code><span>new name</span></div>
</div>

<div class="symbol-flow"><code>'+</code><span>is a symbol</span><code>(procedure? '+) ; ⇒ #f</code></div>

Both `+` and `suma` refer to the same procedure. Quoting `+` produces a symbol instead.

</div>
</div>

---

<!-- _class: section -->

<div class="eyebrow">04</div>

# Functions as arguments to other functions

<p class="lead">A function can be an argument. A parameter can refer to it and call it inside the body.</p>

---

<div class="eyebrow">Function aplica</div>

## Receive a function and two values

<div class="columns equal">
<div>

```racket
(define (aplica f x y)
  (f x y))
```

```racket
(aplica * 4 5)                       ; ⇒ 20
(aplica string-append
        "hello" "bye")
; ⇒ "hellobye"
```

`f` must accept two arguments. The expression `(f x y)` calls it.

</div>
<div class="aplica-flow">

<div class="apply-expression">(aplica + 2 3)</div>
<div class="argument-bindings"><code>f = +</code><code>x = 2</code><code>y = 3</code></div>
<div class="flow-caption">The body <code>(f x y)</code> becomes</div>
<div class="apply-expression">(+ 2 3)</div>
<div class="flow-arrow">↓</div>
<div class="apply-result">5</div>

</div>
</div>

---

## Use our own function or a lambda

<div class="columns equal">
<div>

```racket
(define (join-with-dash s1 s2)
  (string-append
    s1 "-" s2))

(aplica join-with-dash
        "hello" "bye")
; ⇒ "hello-bye"
```

</div>
<div>

```racket
(aplica
  (lambda (x y)
    (sqrt
      (+ (* x x)
         (* y y))))
  3 4)
; ⇒ 5
```

</div>
</div>

---

<div class="eyebrow">Function aplica-2</div>

## Apply one function after another

<div class="columns equal">
<div>

```racket
(define (aplica-2 f g x)
  (f (g x)))
```

```racket
(define (suma-5 x) (+ x 5))
(define (doble x) (+ x x))

(aplica-2 suma-5 doble 3)
```

The inner function `g` runs first. Its result becomes the argument of `f`.

</div>
<div class="compose-flow">
  <div class="compose-value">3</div>
  <div class="compose-function"><span><i>g</i> runs first</span><code>(doble 3)</code></div>
  <div class="compose-value">6</div>
  <div class="compose-function"><span>then <i>f</i></span><code>(suma-5 6)</code></div>
  <div class="compose-value result">11</div>
</div>
</div>

---

## The same idea with lambda expressions

```racket
(aplica-2
  (lambda (x) (* x 2))
  (lambda (x) (+ x 5))
  10)
; ⇒ 30
```

The inner function adds `5`. The outer function multiplies the result by `2`.

---

<!-- _class: semantic -->

<div class="semantic-grid">
<div class="semantic-copy">

<div class="eyebrow">Function apply</div>

## A list becomes arguments

<p>Here the function is <code>+</code>. The elements keep their order and become separate arguments.</p>

</div>
<div class="apply-stack">

<span class="flow-stage">Call to apply</span>
<div class="apply-expression">(apply + '(1 2 3 4))</div>
<div class="flow-arrow">↓</div>
<span class="flow-stage">Elements of the list</span>
<div class="list-row">
  <span class="atom head">1</span>
  <span class="atom pass">2</span>
  <span class="atom">3</span>
  <span class="atom pass">4</span>
</div>
<div class="flow-arrow">↓</div>
<span class="flow-stage">Call created by apply</span>
<div class="apply-expression">(+ 1 2 3 4)</div>
<span class="flow-stage">Result</span>
<div class="apply-result">10</div>

</div>
</div>

---

## Using `apply`

<div class="columns equal">
<div>

```racket
(apply + '(1 2 3 4))
; ⇒ 10
```

This has the same effect as:

```racket
(+ 1 2 3 4)
; ⇒ 10
```

</div>
<div>

```racket
(apply
  (lambda (x y)
    (+ x (* 2 y)))
  '(2 5))
; ⇒ 12
```

The number of list elements must match the function's arity.

</div>
</div>

---

<div class="eyebrow">Example suma-parejas</div>

## Add any number of pairs

<div class="columns equal">
<div>

```racket
(suma-parejas
  '(1 . 2)
  '(3 . 4)
  '(5 . 6))
; ⇒ (9 . 12)
```

</div>
<div>

```racket
(define (suma-pareja p1 p2)
  (cons
    (+ (car p1) (car p2))
    (+ (cdr p1) (cdr p2))))
```

```racket
(suma-pareja '(1 . 2) '(3 . 4))
; ⇒ (4 . 6)
```

</div>
</div>

---

<!-- _class: compact -->

## Recursion with variable arguments

<div class="sketch-columns recursion-apply">
<div>

```racket
(define (suma-parejas . parejas)
  (if (null? parejas)
      '(0 . 0)
      (suma-pareja
        (first parejas)
        (apply suma-parejas
               (rest parejas)))))
```

`(rest parejas)` is a list. `apply` uses its elements as the arguments of the recursive call.

</div>
<div>

<div class="pair-flow">

  <div class="pair-source">
    <span class="pair-label">parejas</span>
    <code>'((1 . 2) (3 . 4) (5 . 6))</code>
  </div>

  <div class="pair-branches">
    <div class="pair-branch first-branch">
      <span class="pair-label">first parejas</span>
      <span class="pair-arrow">↓</span>
      <code>'(1 . 2)</code>
    </div>
    <div class="pair-branch rest-branch">
      <span class="pair-label">rest parejas</span>
      <span class="pair-arrow">↓</span>
      <code>'((3 . 4) (5 . 6))</code>
    </div>
  </div>

  <div class="pair-apply">
    <span class="pair-label">Recursive call with apply</span>
    <code>(suma-parejas '(3 . 4) '(5 . 6))</code>
    <span class="pair-arrow">↓</span>
    <span class="pair-result-wrap"><small>Recursive call result</small><code class="pair-result">'(8 . 10)</code></span>
  </div>

  <div class="pair-combine">
    <code>(suma-pareja '(1 . 2) '(8 . 10))</code>
    <span class="pair-arrow">↓</span>
    <code class="pair-final">'(9 . 12)</code>
  </div>

</div>

</div>
</div>

---

<div class="eyebrow">Recursive definition</div>

## Two cases define `suma-parejas`

<div class="recursive-pattern">

<div class="pattern-case">
  <span class="pattern-label">Base case</span>
  <div class="pattern-equation">(suma-parejas) = '(0 . 0)</div>
  <p class="pattern-note">With no pairs, the neutral result is the pair of zeros.</p>
</div>

<div class="pattern-case general">
  <span class="pattern-label">General case</span>
  <div class="pattern-equation">(suma-pareja<br>&nbsp;&nbsp;(first parejas)<br>&nbsp;&nbsp;(apply suma-parejas (rest parejas)))</div>
  <p class="pattern-note">Use the result returned by the recursive call on <code>(rest parejas)</code>, then combine it with the first pair.</p>
</div>

</div>
