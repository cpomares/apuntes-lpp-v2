# Lab 4: Recursive Functions That Return Lists

## Before the Lab Session ##

- Before starting this lab, it is important that you review the solution to
  lab 3. You can ask your lab instructor any questions you may have.

- The following exercises are based on the theory concepts covered last week.
Before the lab session, you should review all the concepts and **try in
DrRacket** all the examples from the following sections of topic 2
[_Functional
Programming_](../../theory/topic02-functional-programming/topic02-functional-programming.md#43-recursive-functions-that-build-lists):

    - 4.3. _Recursive functions that build lists_
    - 4.4. _Functions with a variable number of arguments_
    - 5 _Functions as first-class data types_ (up to and including
      section 5.3. _Function apply_)


## Exercises


### Exercise 1 ###

a) Implement the recursive function `(contiene-prefijo prefijo
lista-pal)`, which receives a string and a list of words. It returns a
list with the Booleans resulting from checking whether the string is a
prefix of each word in the list.

You must define a helper function `(es-prefijo? pal1 pal2)` that checks
whether word 1 is a prefix of word 2.

!!! Hint "Hint"
    You can use the function `(substring palabra inicio final)`, which returns
    the substring of `palabra` from position `inicio` to position `final`
    (not included).

Examples:

```racket
(es-prefijo? "ante" "anterior") ; ⇒ #t
(contiene-prefijo "ante" '("anterior" "antígona" "antena" "anatema")) 
; ⇒ (#t #f #t #f)
```

b) We are going to generalize the solution to exercise 5 from lab 2 and
implement the recursive function `(cadenas-mayores lista1 lista2)`, taking into
account that the lists it receives have an undetermined number of strings. If
one list is longer than the other, all its strings must be added to the resulting
list.

Examples:

```racket
(cadenas-mayores '("hola" "que" "tal") '("adios")) 
; ⇒ ("adios" "que" "tal")
(cadenas-mayores '("hola" "que" "tal") '("meme" "y" "adios"))
; ⇒ ("hola" "que" "adios")
(cadenas-mayores '("la" "primera" "práctica" "de" "recursión")
                 '("confiar" "en" "la" "recursión" "facilita" "su" "resolución"))
; ⇒ ("confiar" "primera" "práctica" "recursión" "recursión" "su" "resolución")
```

### Exercise 2 ###


a) Implement the recursive function `(inserta-pos dato pos lista)`, which
receives a datum, a position, and a list, and returns the resulting list after
inserting the datum at the indicated position in the list. If the position is 0,
the datum is inserted at the head. We assume that the position will always be
positive and less than or equal to the length of the list.

Examples:

```racket
(inserta-pos 'b 2 '(a a a a)) ; ⇒ '(a a b a a)
(inserta-pos 'b 0 '(a a a a)) ; ⇒ '(b a a a a)
```

b) Implement the recursive function `(inserta-ordenada n
lista-ordenada)`, which receives a number and a list of numbers sorted from
smallest to largest, and returns the resulting list after inserting number `n`
in the correct position so that the list remains sorted.

Example:

```racket
(inserta-ordenada 10 '(-8 2 3 11 20)) ; ⇒ (-8 2 3 10 11 20)
```

c) Using the previous function `inserta-ordenada`, implement the recursive
function `(ordena lista)`, which receives a list of numbers and returns a sorted
list.

Example:

```racket
(ordena '(2 -1 100 4 -6)) ; ⇒ (-6 -1 2 4 100)
```

### Exercise 3 ###

a) Implement the recursive function `(mueve-al-principio lista dato)`, which
receives a list and a datum contained in the list. The function must return the
resulting list after moving the first occurrence of the datum to the beginning of
the list, leaving the rest of the list unchanged. We assume that the datum passed
as a parameter is contained in the list.

Example:

```racket
(mueve-al-principio '(a b e c d e f) 'e) ; ⇒ (e a b c d e f)
(mueve-al-principio '(a b c d e f g) 'a) ; ⇒ (a b c d e f g)
```

b) Implement a recursive function `(comprueba-simbolos lista-simbolos
lista-num)`, which receives a list of symbols and a list of integers (both with
the same length) and returns a list of pairs. Each pair is formed by the symbol
at the i-th position of `lista-simbolos` and the integer at that same position
of `lista-num`, as long as that number matches the length of the string
corresponding to the symbol. You can use the predefined functions
`string-length` and `symbol->string`.

Example:

```racket
(comprueba-simbolos '(este es un ejercicio de examen) '(2 1 2 9 1 6))
; ⇒ ((un . 2) (ejercicio . 9) (examen . 6))
```



### Exercise 4 ###

We are going to implement different versions of functions that expand an
original list.

In the first part, we will define a helper function that must be used in all the
remaining parts.

a) Write the recursive function `(expande-pareja pareja)`, which receives a pair
formed by a datum and a number _n_, and returns the list formed by _n_
repetitions of the datum.

Example:

```racket
(expande-pareja '(hola . 3)) ; ⇒ (hola hola hola)
(expande-pareja '(#t . 5)) ; ⇒ (#t #t #t #t #t)
```

b) We are going to implement two versions of the function `(expande-parejas
pareja_1 ... pareja_n)`, which receives a variable number of arguments (all
optional) and returns a list where the pairs have been "expanded", creating a
list with as many elements as the number indicated by each pair. All arguments
are optional; if there are no arguments, the empty list will be returned.

Example:

```racket
(expande-parejas '(#t . 3) '("LPP" . 2) '(b . 4)) 
; ⇒ (#t #t #t "LPP" "LPP" b b b b)
```

b.1) Write a solution in which the `expande-parejas` function calls a recursive
function `(expande-lista lista-parejas)` that works on a list of pairs.

b.2) Write a solution in which the `expande-parejas` function itself is
recursive. Call it `expande-parejas-2` and be careful that the recursive call is
also made to `expande-parejas-2` itself.

!!! Hint "Hint"
    Review [section
    5.3.1](../../theory/topic02-functional-programming/topic02-functional-programming.md#531-apply-function-and-recursive-functions)
    of the theory notes, which explains how to use `apply` to implement
    recursive functions with a variable number of arguments.

c) Implement the recursive function `(expande lista)`. It receives a list in
which some positive integers are interleaved. It returns the original list with
the elements following the numbers expanded as many times as indicated by the
number. The list will never contain two consecutive numbers, and there will
always be an element after a number.

For its implementation, you must also use the function `(expande-pareja
pareja)` defined in part a).

Example:

```racket
(expande '(4 clase ua 3 lpp aulario)) 
; ⇒ (clase clase clase clase ua lpp lpp lpp aulario)
```

In the example, 4 indicates that the following element (`clase`) must be
repeated 4 times in the expanded list, and 3 indicates that the following
element (`lpp`) will be repeated 3 times.


### Exercise 5 ###

a) Indicate what the following Scheme expressions return. Some expressions may
contain an error. If so, indicate that too and explain what type of error it is.
Do it without the interpreter, and then check with the interpreter whether your
answer was correct.


```racket
((lambda (x) (* x x)) 3) ; ⇒ ?
((lambda () (+ 6 4))) ; ⇒ ?
((lambda (x y) (* x (+ 2 y))) (+ 2 3) 4) ; ⇒ ?
((lambda (x y) (* x (+ 2 x))) 5) ; ⇒ ?


(define f (lambda (a b) (string-append "***" a b "***")))
(define g f)
(procedure? g) ; ⇒ ?
(g "Hola" "Adios") ; ⇒ ?
```

b) We have seen in theory that the `define` special form for constructing
functions is _syntactic sugar_, and that the Scheme interpreter converts it into
an equivalent expression using the `lambda` special form.

Write the equivalent expressions, using the `lambda` special form, for the
following function definitions:

```racket
(define (suma-3 x)
   (+ x 3))
    
(define (factorial x)
   (if (= x 0)
      1
      (* x (factorial (- x 1)))))
```


c) Given the following function definitions, indicate what the invocations would
return. Some expressions may contain an error. If so, indicate that too and
explain what type of error it is.

Do it without the interpreter, and then check with the interpreter whether your
answer was correct.


```racket
(define (doble x)
   (* 2 x))
   
(define (foo f g x y)
   (f (g x) y))

(define (bar f p x y)
   (if (and (p x) (p y))
       (f x y)
       'error))
       
(foo + 10 doble 15) ; ⇒ ?
(foo doble + 10 15) ; ⇒ ?
(foo + doble 10 15) ; ⇒ ?
(foo string-append (lambda (x) (string-append "***" x)) "Hola" "Adios") ; ⇒ ?

(bar doble number? 10 15) ; ⇒ ?
(bar string-append string? "Hola" "Adios") ; ⇒ ?
(bar + number? "Hola" 5) ; ⇒ ?
```

### Exercise 6 ###

We are going to keep playing cards with Scheme. You will have to implement a
series of helper functions that will let you perform a card trick at the end of
the exercise.

Start by downloading the
[`lpp.rkt` file](https://raw.githubusercontent.com/domingogallardo/apuntes-lpp/master/src/lpp.rkt)
again. We have included in it a new function `(cartas n)` that lets you generate
a list of _n_ random cards from a deck of up to 48 cards. For example:

```racket
(cartas 10) ; ⇒ (9♣ 7♠ Q♠ 4♥ 8♠ 3♠ 7♦ A♠ A♥ K♠)
(cartas 5) ; ⇒ (7♣ 3♣ 6♣ 7♠ 5♣)
```

At most, you can pass 48 as the parameter to randomly generate the 48 cards of a
French deck without tens.

!!! Note "The `cartas` function does not follow the functional paradigm"
    The `cartas` function returns a random list of cards. It does not follow the
    functional paradigm because it returns different values when called with the
    same parameters.

a) Define a function `(coloca tres-listas un dos tres)`, which receives a list
with three lists and three elements, and returns the result of placing the
elements at the head of the three lists.

Example:

```racket
(coloca '(() () ()) 'a 'b 'c) ; ⇒ '((a) (b) (c))
(coloca '((a) (a) (a)) 'b 'b 'b) ; ⇒ '((b a) (b a) (b a))
(coloca '((a) (b c) (d e f)) 'g 'h 'i) ; ⇒ '((g a) (h b c) (i d e f)))
```

b) Using the previous function as a helper, implement a recursive function
`(reparte-tres lista-cartas)`, which receives a list of cards with a number of
cards that is a multiple of 3 and returns the result of dealing those cards one
by one into three piles. The cards in positions 0, 3, 6, etc. will go in one
pile. The cards in positions 1, 4, 7, etc. will go in the second pile. And the
cards in positions 2, 5, 8, etc. will go in the third pile.

The result will be a list with three lists representing those three piles of
cards.

Example:

```racket
(define doce-cartas '(A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣))
(reparte-tres doce-cartas) ; ⇒ '((A♣ 4♣ 7♣ J♣) (2♣ 5♣ 8♣ Q♣) (3♣ 6♣ 9♣ K♣))
```

c) Implement a recursive function `(elemento-central lista)`, which receives a
list with an odd number of elements (greater than or equal to one) and returns
its central element.

!!! Note "Hint"
    Suppose you define a recursive helper function `(quita-ultimo lista)`, which
    returns a list without the last element.

    Could you use this function to pass a simpler case to the recursive call and
    have the recursive call return the central element?


Example:

```racket
(elemento-central '(a b c d e f g)) ; ⇒ d
```

d) Once you have implemented the previous functions, all that remains is to copy
the following definitions so you can perform the card trick. These are functions
that reassemble the deck from the three piles depending on whether the chosen
card is in the left, center, or right pile.

And the `adivina` function is the one that returns the chosen card in the trick.

```racket
(define (izquierda tres-listas)
  (append (third tres-listas)
          (first tres-listas)
          (second tres-listas)))

(define (centro tres-listas)
  (append (third tres-listas)
          (second tres-listas)
          (first tres-listas)))

(define (derecha tres-listas)
  (append (second tres-listas)
          (third tres-listas)
          (first tres-listas)))

(define (adivina lista)
  (elemento-central lista))
```

Finally, before starting the trick, a couple of considerations about programs
with random numbers.

The following function, with the constant 90 as an argument, always generates
the random sequence that lets you follow the example. If it is changed to another
constant, the sequence will also always be repeated, although it will be a
different one. Always having the same random sequence makes it possible to debug
the program while always working with the same random example.

```racket
(random-seed 90)
```
If a variable value is used instead of a constant, a different random sequence is
obtained each time the program is executed.

Example:

```racket
(random-seed (modulo (current-milliseconds) (expt 2 31)))
```

And now we can start the card trick.

1. We deal a list of cards and store it in the variable `t1`. We could play with
3, 9, 15, 21, or 27 cards. We are going to do it with 27:

    ```racket
    (define t1 (reparte-tres (cartas 27)))
    ```

2. We display the piles and ask the spectator to think of a card without saying
it. For example, the ace of clubs.

    ```racket
    t1 ; ⇒ ((J♣ 8♦ K♥ J♠ 2♠ 8♥ Q♣ 4♦ A♥) (5♥ 9♣ 5♦ Q♠ A♦ 9♥ 5♠ 9♦ Q♦) (7♣ 3♠ 6♥ 6♣ 7♥ 3♣ 4♣ A♣ J♥))
    ```

3. We ask the spectator which pile contains the chosen card. We join the piles
   using the function corresponding to the pile's location (`izquierda`,
   `derecha`, or `centro`). In this case, the ace of clubs is in the right pile,
   so we use the `derecha` function. Then we deal the resulting deck into three
   piles again and store them in the variable `t2`:

    ```racket
    (define t2 (reparte-tres (derecha t1)))
    ```

4. We display the piles again and ask where the card is. In this case, it is in
   the center.

    ```racket
    t2 ; ⇒  ((5♥ Q♠ 5♠ 7♣ 6♣ 4♣ J♣ J♠ Q♣) (9♣ A♦ 9♦ 3♠ 7♥ A♣ 8♦ 2♠ 4♦) (5♦ 9♥ Q♦ 6♥ 3♣ J♥ K♥ 8♥ A♥))
    ```

    We join the piles using the `centro` function and deal again, storing the
    result in the variable `t3`:

    ```racket
    (define t3 (reparte-tres (centro t2)))
    ```

5. We display the piles:

    ```racket
    t3 ; ⇒  ((5♦ 6♥ K♥ 9♣ 3♠ 8♦ 5♥ 7♣ J♣) (9♥ 3♣ 8♥ A♦ 7♥ 2♠ Q♠ 6♣ J♠) (Q♦ J♥ A♥ 9♦ A♣ 4♦ 5♠ 4♣ Q♣))
    ```

    And we ask where the card is. In this case, the ace of clubs is in the right
    pile. We join the piles again using the `derecha` function, and we can now
    call the `adivina` function with the resulting deck. This function will
    magically return the chosen card:

    ```racket
    (adivina (derecha t3)) ; ⇒ A♣
    ```

----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
