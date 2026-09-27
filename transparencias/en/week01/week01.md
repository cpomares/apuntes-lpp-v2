---
marp: true
theme: lpp
size: 16:9
paginate: true
footer: "Cristina Pomares Puig · LPP"
---

<!-- _class: cover week01-cover -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="eyebrow">Programming Languages and Paradigms</div>
<div class="week-marker">Week 1</div>

# Course overview and functional programming

<div class="cover-topic-list">
  <div><b>Topic 0</b><span>Course overview</span></div>
  <div><b>Topic 1</b><span>Programming Languages and Paradigms · Study at home</span></div>
  <div><b>Topic 2 · Part 1</b><span>Functional Programming in Scheme</span></div>
</div>

<div class="meta">
  <strong>Cristina Pomares Puig</strong>
  Departamento de Ciencia de la Computación e Inteligencia Artificial<br>
  Universidad de Alicante
</div>

<!--
Idea: Presentar el mapa de la semana sin desarrollar todavía los conceptos.
Say: "This week has three parts: the course overview, Topic 1 for independent study, and the first part of functional programming in Scheme."
Bridge: "Let us begin with the overall structure of the course."
-->

---

<div class="eyebrow">Course map</div>

## Three blocks, two languages

<div class="course-blocks course-map">
  <div><b>1</b><strong>Languages and functional programming</strong><span>Topics 1–2 · Scheme</span></div>
  <div><b>2</b><strong>Recursive processes and structures</strong><span>Topics 3–4 · Scheme</span></div>
  <div><b>3</b><strong>Functional programming and advanced OOP</strong><span>Topics 5–6 · Swift</span></div>
</div>

<p class="course-map-note">The concepts move from expressions and functions to recursion, recursive data, and their use in Swift.</p>

<!--
Idea: Mostrar la estructura global sin entrar en el detalle semanal.
Say: "The course moves from Scheme to recursive structures and then to Swift."
Bridge: "The planning shows when each block takes place."
-->

---

<div class="eyebrow">Course planning</div>

## Fourteen weeks across three blocks

<div class="course-plan">
  <div><b>Weeks 1–4</b><strong>Topics 0–2 · Scheme</strong><span>Course overview, functional programming, evaluation, and Scheme forms</span><em>Partial 1 · Week 6 · 5 March</em></div>
  <div><b>Weeks 5–8</b><strong>Topics 3–4 · Scheme</strong><span>Recursive processes and recursive data structures</span><em>Partial 2 · Week 10 · 20 April</em></div>
  <div><b>Weeks 9–14</b><strong>Topics 5–6 · Swift</strong><span>Functional programming, advanced OOP, and final review</span><em>Partial 3 · 29 May</em></div>
</div>

<p class="course-map-note">Moodle provides the detailed weekly dates, theory content, and practical activities.</p>

<!--
Idea: Señalar semanas, bloques y parciales. No leer todas las tarjetas palabra por palabra.
Say: "The fourteen weeks are organised into three teaching blocks, each followed by a partial exam."
Bridge: "The assessment follows the same three-block structure."
-->

---

<div class="eyebrow">Assessment</div>

## Three written exams cover the three blocks

<div class="assessment-bars">
  <div><span>Partial 1</span><strong>35%</strong><i style="--weight:35%"></i></div>
  <div><span>Partial 2</span><strong>30%</strong><i style="--weight:30%"></i></div>
  <div><span>Partial 3</span><strong>35%</strong><i style="--weight:35%"></i></div>
</div>

<p class="small">The course notes state that no minimum mark is required for an individual partial exam.</p>

<p class="exam-note"><strong>Exam rule:</strong> internet-connected devices remain inside bags placed on the floor.</p>

<!--
Idea: Explicar pesos, ausencia de nota mínima y norma de dispositivos.
Say: "There are three written exams, and there is no minimum mark for an individual partial exam."
Bridge: "Within this structure, every week follows the same working cycle."
-->

---

<div class="eyebrow">Weekly work</div>

## Each week combines preparation and practice

<div class="week-workflow">
  <div><b>1</b><strong>Prepare</strong><span>Read the notes and follow the theory examples.</span></div>
  <div><b>2</b><strong>Practise</strong><span>Work on the worksheet during the lab and at home.</span></div>
  <div><b>3</b><strong>Submit</strong><span>Upload your work to Moodle at the end of the week.</span></div>
  <div><b>4</b><strong>Review</strong><span>Compare your reasoning with the published solution.</span></div>
</div>

<p class="course-map-note">Two seminars introduce Scheme and Swift. Twelve weekly worksheets develop fluency.</p>

<!--
Idea: Explicar la rutina semanal y la importancia de intentar los ejercicios.
Say: "Every week follows the same cycle: prepare, practise, submit, and review."
Bridge: "All current information and submissions are available through two course resources."
-->

---

<div class="eyebrow">Course resources</div>

## Where each kind of information lives

<div class="columns equal resource-columns">
<div>

### Moodle

- Weekly planning and announcements
- Worksheet submission
- Questions for the teaching team

</div>
<div>

### Course notes website

- Theory notes and worked examples
- Seminar material
- Practical worksheets for Scheme and Swift

</div>
</div>

<!--
Idea: Diferenciar Moodle de la web de apuntes.
Say: "Use Moodle for weekly organisation and submissions, and use the course website for notes, examples, and worksheets."
Bridge: "The resources help only if you use them as part of an active study cycle."
-->

---

<div class="eyebrow">Learning strategy</div>

## A productive study cycle

<div class="learning-loop">
  <div><b>Attempt</b><span>Work on the problem before reading its solution.</span></div>
  <div><b>Run</b><span>Test the example and observe each result.</span></div>
  <div><b>Explain</b><span>Compare solutions and justify every evaluation step.</span></div>
  <div><b>Vary</b><span>Change the problem, then ask about unresolved reasoning.</span></div>
</div>

> Memorising a published solution does not develop the reasoning required to solve a new problem.

<!--
Idea: Insistir en intentar, ejecutar, explicar y variar.
Say: "Do not memorise a solution. Try the problem, run the code, explain the result, and then change something."
Bridge: "Topic 1 gives the background vocabulary for the rest of the course."
-->

---

<!-- _class: section -->

<div class="eyebrow">Topic 1 · Study at home</div>

# Programming Languages

<p class="lead">Read Topic 1 in the course notes. It provides the language and paradigm background required for the rest of the course.</p>

<div class="self-study-notice"><b>Before continuing</b><span>Make sure you can distinguish the main programming paradigms and recognise that modern languages may support more than one.</span></div>

<!--
Idea: Dejar inequívoco que el Tema 1 se estudia en casa.
Say: "Topic 1 is required independent study. We will not present it in class, but you need its terminology."
Bridge: "The lecture itself starts with Topic 2."
-->

---

<!-- _class: section -->

<div class="eyebrow">Topic 2 · Part 1</div>

# Functional Programming

<p class="lead">Part 1 introduces programs as compositions of functions and expressions.</p>

<!--
Idea: Abrir el tema con una pregunta sencilla: entrada, función, resultado.
Say: "We now start Topic 2. The central idea is that programs can be built by composing functions."
Bridge: "First, we need a precise idea of what a function does."
-->

---

<div class="eyebrow">Definition</div>

## A function connects an input with a result

<div class="columns equal pure-definition">
<div>

```racket
(define (square x)
  (* x x))

(square 4) ; ⇒ 16
```

</div>
<div>

<strong>The result depends only on <code>x</code></strong>

- The function reads no hidden state.
- The function changes no external value.
- Calling it again with `4` returns `16` again.

</div>
</div>

<!--
Idea: Una función pura depende solo de sus argumentos y no cambia nada fuera.
Say: "For the same input, this function always returns the same output, and it changes no external value."
Bridge: "Pure functions are one of four functional ideas developed in this course."
-->

---

<div class="eyebrow">Functional paradigm</div>

## Four ideas developed across the course

<div class="four-up functional-features">
  <div><b>PURE FUNCTIONS</b><span>Today · no hidden state or side effects</span></div>
  <div><b>IMMUTABLE VALUES</b><span>Today · definitions do not change</span></div>
  <div><b>RECURSION AND LISTS</b><span>Later · recursive functions process recursive data</span></div>
  <div><b>FUNCTION VALUES</b><span>Later · functions can be passed and returned</span></div>
</div>

<!--
Idea: Separar lo que se explica hoy de lo que llegará en semanas posteriores.
Say: "Today we focus on pure functions and immutable values. Recursion, lists, and functions as values come later."
Bridge: "Functional programming also belongs to the wider declarative family."
-->

---

<div class="eyebrow">Declarative and imperative programming</div>

## Two ways to describe a computation

<div class="columns equal paradigm-contrast">
<div>

### Declarative

- Declare values and the desired result.
- Do not specify intermediate state changes.
- Follow a mathematical model.

<strong>Examples:</strong> spreadsheets, Prolog, functional programming, and SwiftUI.

</div>
<div>

### Imperative

- Specify the execution steps.
- Use assignment to update values.
- Allow mutation and mutable local state.

<strong>Examples:</strong> C, Java, and traditional JavaScript.

</div>
</div>

<!--
Idea: Contrastar resultado frente a pasos. Esta es la frase central de la comparación.
Say: "A declarative program describes the result. An imperative program describes the steps."
Bridge: "Functional composition lets us connect results without a sequence of assignments."
-->

---

<div class="eyebrow">Execution steps and composition</div>

## Composition connects results directly

<div class="columns equal">
<div>

### Intermediate variables

```c
int a = square(8);
int b = doubleValue(a);
int c = square(b);
return c;
```

</div>
<div>

### Functional composition

```racket
(square
  (double-value
    (square 8)))
```

</div>
</div>

<p class="concept-note"><strong>Substitution:</strong> because <code>square</code> is pure, <code>(square 3)</code> can be replaced by <code>9</code> without changing the result.</p>

<!--
Idea: Usar el mismo cálculo para explicar composición y sustitución.
Say: "The functional version passes each result directly to the next function. A pure call can also be replaced by its value."
Bridge: "Imperative programs model the same computation through changing state."
-->

---

<div class="eyebrow">Imperative programming</div>

## Assignment changes program state

<div class="imperative-principles">
  <div><b>Memory</b><span>A variable names a location whose contents may change.</span></div>
  <div><b>Assignment</b><span>A command stores a new value in that location.</span></div>
  <div><b>Sequence</b><span>The order of commands determines the result.</span></div>
</div>

```c
int x = 10;
x = x + 1;
```

<!--
Idea: Introducir memoria, asignación y orden con una sola mutación.
Say: "Here, x names a memory location. The assignment changes the value stored in that location."
Bridge: "Mutable state becomes harder to follow when it is shared or hidden."
-->

---

<div class="eyebrow">Consequences of mutable state</div>

## State can escape through aliases or persist between calls

<div class="columns equal mutable-consequences">
<div>

### Shared object

```java
Point2D p1 = new Point2D(3.0, 2.0);
Point2D p2 = p1;

p2.setCoordX(10.0);
p1.getCoordX();       // 10.0
```

</div>
<div>

### Hidden local state

```c
int counter() {
  static int c = 0;
  c++;
  return c;
}
```

<p><code>counter()</code> may return <code>1</code>, then <code>2</code>, then <code>3</code>.</p>

</div>
</div>

<!--
Idea: Mostrar dos problemas distintos: aliasing y estado que persiste.
Say: "A change may be visible through another reference, or it may remain hidden between two calls."
Bridge: "This gives variables a different meaning in the two programming models."
-->

---

<div class="eyebrow">Declarative and imperative models</div>

## Different meanings of a variable

<div class="comparison-table">
  <div class="header"><span></span><b>Declarative</b><b>Imperative</b></div>
  <div><strong>Focus</strong><span>Values, relationships, and results</span><span>Commands and state changes</span></div>
  <div><strong>Variable</strong><span>Name for a value</span><span>Name for a memory location</span></div>
  <div><strong>Order</strong><span>Derived from expression dependencies</span><span>Specified by the command sequence</span></div>
</div>

<!--
Idea: Cerrar la comparación sin convertirla en un resumen general.
Say: "In the declarative model, a variable names a value. In the imperative model, it usually names a location that can change."
Bridge: "Scheme makes the declarative evaluation process visible in its expressions."
-->

---

<!-- _class: section -->

<div class="eyebrow">Topic 2 · Part 1</div>

# Expression evaluation in Scheme

<p class="lead">Evaluation proceeds from the inside out as Scheme composes functions and evaluates expressions.</p>

<!--
Idea: Cambiar del contraste conceptual a la mecánica de Scheme.
Say: "We now move from programming models to the concrete evaluation of Scheme expressions."
Bridge: "The first visible difference is prefix notation."
-->

---

<div class="eyebrow">Evaluating expressions</div>

## Prefix notation

<div class="columns equal">
<div>

```racket
2                 ; ⇒ 2
(+ 2 3)           ; ⇒ 5
(+)               ; ⇒ 0
(+ 2 4 5 6)       ; ⇒ 17
(+ (* 2 3) (- 3 1)) ; ⇒ 8
```

</div>
<div class="prefix-anatomy">
  <code>(+ 2 3)</code>
  <div><span>function</span><strong>+</strong></div>
  <div><span>arguments</span><strong>2, 3</strong></div>
</div>
</div>

<!--
Idea: Identificar siempre primer elemento como función y resto como argumentos.
Say: "In a Scheme call, the function comes first and the arguments follow it inside the same parentheses."
Bridge: "Let us apply this notation to a nested expression."
-->

---

<!-- _class: question -->

<div class="eyebrow">Inside-out evaluation</div>

## What is the value of this expression?

```racket
(+ (* 2 3)
   (- 3 (/ 12 3)))
```

<p class="prompt">Evaluate the innermost primitive expressions first. Replace each one with its result.</p>

<!--
Idea: Dar tiempo real para que calculen; no resolver de inmediato.
Say: "Take a moment and evaluate the innermost expressions first. What value do you obtain?"
Bridge: "Now we can compare the answer with the evaluation sequence."
-->

---

<div class="eyebrow">Inside-out evaluation</div>

## One expression becomes one value

<div class="evaluation-ladder week01-evaluation">
  <code>(+ (* 2 3) (- 3 (/ 12 3)))</code>
  <span>↓ evaluate the innermost division</span>
  <code>(+ (* 2 3) (- 3 4))</code>
  <span>↓ evaluate multiplication and subtraction</span>
  <code>(+ 6 -1)</code>
  <strong>5</strong>
</div>

<!--
Idea: Leer la escalera de arriba abajo y justificar cada reemplazo.
Say: "Each step replaces one completed expression with its value until only the final number remains."
Bridge: "A user-defined function follows the same principle: its body is an expression."
-->

---

<div class="eyebrow">Defining functions</div>

## A function body is an expression

<div class="columns equal">
<div>

```racket
(define (square x)
  (* x x))
```

There is no `return` statement. The body evaluates to the function result.

</div>
<div>

```racket
(square 10)
; ⇒ 100

(square
  (+ 10
     (square (+ 2 4))))
; ⇒ 2116
```

</div>
</div>

<!--
Idea: Recalcar que no existe return; el valor del cuerpo es el resultado.
Say: "A Scheme function has no return statement. The value of its body becomes the function result."
Bridge: "Small functions can then be reused to define larger ones."
-->

---

<div class="eyebrow">Auxiliary functions</div>

## Build larger functions from smaller ones

<div class="columns equal">
<div>

### Repeated implementation

```racket
(define (sum-of-squares x y)
  (+ (* x x)
     (* y y)))
```

</div>
<div>

### Reused abstraction

```racket
(define (square x)
  (* x x))

(define (sum-of-squares x y)
  (+ (square x)
     (square y)))
```

</div>
</div>

<!--
Idea: Comparar repetición con reutilización de square.
Say: "The second definition names the repeated idea once and reuses it."
Bridge: "The same form of composition can create a complete processing pipeline."
-->

---

<div class="eyebrow">Function composition</div>

## A pipeline evaluates from the inside out

```racket
(define (drive-vehicle images)
  (derive-actions
    (recognise
      (filter-data
        (extract-features images)))))
```

<div class="composition-order"><span>1 · features</span><span>2 · filter</span><span>3 · recognise</span><span>4 · actions</span></div>

<!--
Idea: Seguir el orden desde la llamada interior hacia fuera.
Say: "Read the nested calls from the inside out: extract, filter, recognise, and finally derive the actions."
Bridge: "The substitution model makes this evaluation process precise."
-->

---

<!-- _class: section -->

<div class="eyebrow">Topic 2 · Part 1</div>

# The Substitution Model of Computation

<p class="lead">Evaluation becomes rewriting. Replace identifiers and function calls until only primitive expressions remain.</p>

<!--
Idea: Presentar sustitución como reescritura, no como ejecución en memoria.
Say: "The substitution model explains evaluation by rewriting an expression step by step."
Bridge: "The first three rules are the same in both evaluation orders. Rule four changes."
-->

---

<div class="eyebrow">Substitution model</div>

## Rules 1–3 are common to both orders

<div class="rule-list">
  <div><b>1</b><strong>Primitive value</strong><span>A number evaluates to itself.</span></div>
  <div><b>2</b><strong>Identifier</strong><span>Return the value associated with it by <code>define</code>.</span></div>
  <div><b>3</b><strong>Primitive call</strong><span>Evaluate its arguments, then apply the primitive function.</span></div>
</div>

> Rule 4 has two versions, depending on the evaluation order.

<!--
Idea: Las reglas 1, 2 y 3 son comunes. No presentar todavía una regla 4 genérica porque cambia con el orden.
Say: "These first three rules are shared by both evaluation orders. Rule four is different in applicative and normal order."
Bridge: "Let us state both versions of rule four precisely."
-->

---

<div class="eyebrow">Rule 4</div>

## Two versions of rule 4

<div class="columns equal evaluation-orders">
<div>

### Applicative order

1. Evaluate the arguments.
2. Replace the function call with its body.
3. Replace each formal parameter with the corresponding **evaluated value**.
4. Evaluate the resulting expression with the same rules.

</div>
<div>

### Normal order

1. Replace the function call with its body.
2. Replace each formal parameter with the corresponding **unevaluated argument expression**.
3. Evaluate the resulting expression with the same rules.

</div>
</div>

> Scheme uses applicative order.

<!--
Idea: Enfatizar que son dos formulaciones distintas de la misma regla 4, tal como aparece en las notas.
Say: "In applicative order, rule four evaluates the arguments before substitution. In normal order, rule four substitutes the unevaluated argument expressions."
Bridge: "We will use one definition to follow both orders."
-->

---

<div class="eyebrow">Example</div>

## Definitions for both evaluation orders

```racket
(define (double-value x)
  (+ x x))

(define (square y)
  (* y y))

(define a 2)

(double-value (square a))
```

Both orders return `8` for these pure functions.

<!--
Idea: Presentar las definiciones una vez antes de las dos trazas.
Say: "Both strategies use the same definitions and produce eight because these functions are pure."
Bridge: "First, let us follow the order used by Scheme."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Applicative order</div>

## Arguments are evaluated before substitution

```text
(double-value (square a))  ; start
(double-value (square 2))  ; R2: replace a
(double-value (* 2 2))     ; R4: expand square
(double-value 4)           ; R3: apply *
(+ 4 4)                    ; R4: expand double-value
8                          ; R3: apply +
```

<div class="order-caption">The inner call becomes a value before <code>double-value</code> is expanded.</div>

<!--
Idea: Seguir la traza sin saltar pasos; Scheme usa este orden.
Say: "Scheme evaluates square first, obtains four, and only then expands double-value."
Bridge: "Normal order performs the substitutions in the opposite order."
-->

---

<!-- _class: compact -->

<div class="eyebrow">Normal order</div>

## Substitution happens before argument evaluation

```text
(double-value (square a))       ; start
(+ (square a) (square a))       ; R4: expand double-value
(+ (* a a) (* a a))             ; R4: expand square
(+ (* 2 2) (* 2 2))             ; R2: replace a
(+ 4 (* 2 2))                    ; R3: apply *
(+ 4 4)                          ; R3: apply *
8                                ; R3: apply +
```

The expression for `square` appears twice before either copy is evaluated.

<!--
Idea: Señalar la duplicación de square como diferencia observable.
Say: "Normal order expands double-value first, so the unevaluated square expression appears twice."
Bridge: "With pure functions the result is unchanged, but side effects reveal the difference."
-->

---

<div class="eyebrow">Pure and non-pure functions</div>

## Evaluation order can expose a side effect

```racket
(define (zero x)
  (- x x))

(zero (random 10))
```

<div class="columns equal random-orders">
<div><strong>Applicative</strong><span>Evaluate <code>random</code> once, then subtract the value from itself.</span></div>
<div><strong>Normal</strong><span>Substitution can create two separate calls to <code>random</code>.</span></div>
</div>

<!--
Idea: No hace falta calcular números concretos; basta contar llamadas a random.
Say: "Applicative order calls random once. Normal order may duplicate the call, so the subtraction may no longer produce zero."
Bridge: "This is why evaluation rules matter, especially for Scheme special forms."
-->

---

<!-- _class: section -->

<div class="eyebrow">Topic 2 · Part 1</div>

# Special functions and forms in Scheme

<p class="lead">Some expressions define their own evaluation rules. Today we introduce <code>define</code>, <code>if</code>, <code>cond</code>, and <code>quote</code>.</p>

<div class="special-form-contrast">
  <div><b>Ordinary function</b><span>Evaluate every argument, then apply the function.</span></div>
  <div><b>Special form</b><span>Uses its own evaluation rule and may delay or skip an expression.</span></div>
</div>

<p class="continuation-note">This is not a complete list. We will introduce more special forms in later weeks.</p>

<!--
Idea: Definir la diferencia antes de estudiar cada forma y dejar claro que hoy solo introducimos las primeras.
Say: "An ordinary function evaluates all its arguments first. A special form decides its own evaluation rule. Today we introduce four of them, and we will meet more in later weeks."
Bridge: "The first special form associates a name with a value."
-->

---

<div class="eyebrow">Special form define</div>

## Associate a name with a value

```racket
(define <identifier> <expression>)
```

<div class="define-flow">
  <div><b>1</b><span>Evaluate the expression</span></div>
  <div><b>2</b><span>Associate the resulting value with the identifier</span></div>
</div>

```racket
(define base 10)
(define height 12)
(define area (/ (* base height) 2)) ; ⇒ 60
```

<!--
Idea: define no evalúa el identificador como si fuera un argumento normal.
Say: "Define evaluates the expression, then associates the resulting value with the identifier."
Bridge: "The function-definition form treats even more of its parts as syntax."
-->

---

<div class="eyebrow">Special form define</div>

## A function definition does not run its body

```racket
(define (<function-name> <arguments>)
  <body>)
```

<div class="columns equal">
<div>

### Definition time

- The name and parameter list are treated as syntax.
- The body is stored as procedure code.

</div>
<div>

### Call time

```racket
(double-value 5) ; ⇒ 10
```

Bind `x` to `5`, then evaluate the body.

</div>
</div>

> `define` controls which parts are evaluated and when. That special evaluation rule makes it a special form.

<!--
Idea: Contrastar tiempo de definición y tiempo de llamada.
Say: "When we define a function, Scheme stores the body. It evaluates that body only when the function is called."
Bridge: "The if form also chooses which expression to evaluate."
-->

---

<div class="eyebrow">Special form if</div>

## Only one branch is evaluated

```racket
(if <condition>
    <true-expression>
    <false-expression>)
```

<div class="branch-flow">
  <code>(> 10 5)</code>
  <div><span>#t</span><code>(substring "Hello" 1 4)</code><strong>"ell"</strong></div>
  <div><span>#f</span><code>(/ 12 0)</code><em>not evaluated</em></div>
</div>

<!--
Idea: La rama no elegida no se evalúa; por eso la división por cero no falla.
Say: "If evaluates the condition and exactly one branch. The other branch is ignored."
Bridge: "Cond extends the same idea to several conditions."
-->

---

<div class="eyebrow">Special form cond</div>

## Test conditions in order

<div class="columns equal">
<div>

```racket
(cond
  ((> 3 4) "first")
  ((< 2 1) "second")
  ((= 3 1) "third")
  (else "no condition is true"))
```

</div>
<div class="cond-flow">
  <span>#f · continue</span>
  <span>#f · continue</span>
  <span>#f · continue</span>
  <strong>else · return its value</strong>
</div>
</div>

<!--
Idea: Leer condiciones de arriba abajo y detenerse en la primera verdadera.
Say: "Cond tests each condition in order and returns the expression from the first matching clause."
Bridge: "Quote uses a different rule: it prevents evaluation altogether."
-->

---

<div class="eyebrow">Special form quote</div>

## Return a symbol without evaluating it

<div class="columns equal">
<div>

```racket
(quote x)
; ⇒ x

'hello
; ⇒ hello
```

The apostrophe is an abbreviation for `quote`.

</div>
<div>

```racket
(define x 12)

(symbol? 'x) ; ⇒ #t
(symbol? x)  ; ⇒ #f
```

`'x` is the symbol. `x` evaluates to the number `12`.

</div>
</div>

<!--
Idea: Diferenciar x, que se evalúa, de 'x, que produce el símbolo.
Say: "Without quote, x is evaluated. With quote, Scheme returns the symbol itself."
Bridge: "A symbol may look like text, but it is not a string."
-->

---

<div class="eyebrow">Symbols</div>

## Symbols and strings are different data types

<div class="comparison-table symbol-table">
  <div class="header"><span></span><b>Symbol</b><b>String</b></div>
  <div><strong>Example</strong><span><code>'hello</code></span><span><code>"hello"</code></span></div>
  <div><strong>Structure</strong><span>Atomic identifier</span><span>Sequence of characters</span></div>
  <div><strong>Typical role</strong><span>Name or label in data</span><span>Text for people or processing</span></div>
</div>

<!--
Idea: Símbolo atómico frente a secuencia de caracteres.
Say: "A symbol is an atomic label. A string is a sequence of characters."
Bridge: "Quote can preserve not only one symbol, but also a complete parenthesised expression."
-->

---

<div class="eyebrow">Quote and expressions</div>

## Quoted parentheses create data

```racket
'(1 2 3)
'(a b c)
'(* (+ 1 2) 5)
```

<div class="quoted-expression">
  <span>without quote</span><code>(* (+ 1 2) 5)</code><strong>15</strong>
  <span>with quote</span><code>'(* (+ 1 2) 5)</code><strong>a list</strong>
</div>

<!--
Idea: Las mismas palabras y paréntesis pueden ser código o datos.
Say: "Without quote, Scheme evaluates the expression. With quote, the same structure becomes list data."
Bridge: "The list function also creates a list, but it evaluates its elements first."
-->

---

<div class="eyebrow">list and quote</div>

## One evaluates its elements, the other preserves them

<div class="columns equal">
<div>

### Function `list`

```racket
(list 1
      (/ 2 3)
      (+ 2 3))
; ⇒ (1 2/3 5)
```

</div>
<div>

### Special form `quote`

```racket
'(1
  (/ 2 3)
  (+ 2 3))
; ⇒ (1 (/ 2 3) (+ 2 3))
```

</div>
</div>

<!--
Idea: list es función ordinaria; quote es forma especial.
Say: "List evaluates each argument before building the list. Quote preserves every element exactly as written."
Bridge: "Finally, we need two operations for constructing and joining lists."
-->

---

<div class="eyebrow">cons and append</div>

## Add one element or join whole lists

<div class="columns equal">
<div>

### `cons`

```racket
(cons 1 '(2 3 4))
; ⇒ (1 2 3 4)
```

The first argument is one element.

</div>
<div>

### `append`

```racket
(append '(1 2) '(3 4))
; ⇒ (1 2 3 4)
```

The arguments are lists.

</div>
</div>

<!--
Idea: cons añade un elemento; append une listas completas.
Say: "Use cons when the first argument is one element. Use append when both arguments are lists."
Bridge: "We stop here. The next class continues with recursion over lists."
-->
