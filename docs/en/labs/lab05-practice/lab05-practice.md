
# Lab 5: Functions as First-Class Data and Higher-Order Functions

## Before the Lab Session ##

- Before starting this lab, it is important that you review the solution to
  lab 4. You can ask your lab instructor any questions you may have.

- The following exercises are based on the theory concepts covered last week.
Before the lab session, you should review all the concepts and **try in
DrRacket** all the examples from the following sections of topic 2
[_Functional
Programming_](../../theory/topic02-functional-programming/topic02-functional-programming.md#54-generalization):

    - 5.4. Generalization.
    - 5.5. Functions that return other functions.
    - 5.6. Functions in data structures.
    - 5.7. Higher-order functions.

## Exercises

Download the [`lpp.rkt` file](https://raw.githubusercontent.com/domingogallardo/apuntes-lpp/master/src/lpp.rkt)
by right-clicking and selecting the _Save as_ option, saving it as `lpp.rkt`.
Save it in the same folder where you have the `lab5.rkt` file.

The file contains the definitions of the higher-order functions `exists?` and
`for-all?`.

### Exercise 1 ###

a) Define the recursive function `(aplica-veces f1 f2 n x)`, which applies the
functions `f2` and `f1` to the number `x`, `n` times.

For example, `(aplica-veces doble suma-2 3 5)` should return the result of adding
2 to 5 (7), then calculating the double (14), then adding 2 to the result again
(16), calculating its double again (32), and finally adding 2 to the result (34)
and calculating its double. That is, it applies the functions `suma-2` and
`doble` 3 times, taking 5 as the initial number. The result will be 68.

Examples:

```racket
(aplica-veces (lambda (x) (+ x 1)) (lambda (x) (+ x 2)) 2 10) ; ⇒ 16
(aplica-veces (lambda (x) (* x x)) (lambda (x) (+ x 1)) 4 3) ; ⇒ 7072978201
```

b) Implement the recursive function `(mueve-al-principio-condicion pred
lista)`, which receives a predicate and a list. The function is a
generalization of the function from the previous lab and must return the
resulting list after moving the first occurrence of the datum that satisfies the
predicate to the beginning of the list, leaving the rest of the list unchanged.

Unlike in the previous lab, the list might not contain any element that satisfies
the predicate. In that case, the original list is returned.

!!! Hint 
    We consider the smallest list to have one element.


Examples:

```racket
(mueve-al-principio-condicion number? '(a b c 1 d 1 e) ; ⇒ (1 a b c d 1 e)
(mueve-al-principio-condicion number? '(1 a b 1 c)) ; ⇒ (1 a b 1 c)
(mueve-al-principio-condicion number? '(a b c d)) ; ⇒ (a b c d)
```

!!! Hint "Hint"
    Allowing the possibility that no element satisfies the predicate forces us
    to change the solution from the previous lab quite a bit.

    For example, look at the function `(inserta-en-segunda-posicion
    dato lista)` from the solution. If there is no element in the list that
    satisfies the condition, this function must **add the datum at the head**
    instead of inserting it in the second position. In fact, we could rename the
    helper function and call it `inserta-segundo-cond` or something similar.


c) We are going to generalize the function from the previous lab
`(comprueba-simbolos)`, calling it `(comprueba pred lista1
lista2)` and passing it a comparison predicate as a parameter. The function will
now be able to process any kind of lists (of symbols, strings, lists, etc.). The
function passed as a parameter is responsible for comparing whether the element
from the first list satisfies the condition with the element from the second.

Implement the function `(comprueba pred lista1 lista2)`.

Example:

```racket
(comprueba (lambda (x y)
             (= (string-length (symbol->string x)) y))
           '(este es un ejercicio de examen) 
           '(2 1 2 9 1 6))
; ⇒ ((un . 2) (ejercicio . 9) (examen . 6))

(comprueba (lambda (x y)
              (= (string-length x) (string-length y)))
             '("aui" "a" "ae" "c" "aeiou")
             '("hola" "b" "es" "que" "cinco"))
; ⇒ (("a" . "b") ("ae" . "es") ("aeiou" . "cinco"))
```


### Exercise 2 ###

We want to sort from smallest to largest a list that may contain any kind of
element, not only numbers. To do this, we are going to generalize exercise 2 from
the previous lab by adding an additional parameter (a predicate), which we will
call `menor-igual?`.

a) Generalize the `inserta-ordenada` and `ordena` functions by adding this
additional parameter, a predicate that checks whether one datum from the list is
less than or equal to another. Call the resulting functions
`inserta-ordenada-genérica` and `ordena-genérica`.

```racket
(ordena-generica '(3 5 1) <=) ;=> (1 3 5)
```

b) Complete the following three tests. In the first one, you must sort a list of
strings by their length; in the second one, the list of strings by lexicographic
order; and in the third one, a list of number pairs by the sum of their left and
right parts:

```racket
(check-equal? (ordena-generica '("Hola" "me" "llamo" "Iñigo" "Montoya") ________ ) '("me" "Hola" "llamo" "Iñigo" "Montoya"))
(check-equal? (ordena-generica '("Hola" "me" "llamo" "Iñigo" "Montoya") ________ ) '("Hola" "Iñigo" "Montoya" "llamo" "me"))
(check-equal? (ordena-generica '((2 . 2) (1 . 1) (3 . 0) (5 . 1)) ________ ) '((1 . 1) (3 . 0) (2 . 2) (5 . 1)))
```

c) Define the function `(ordena-cartas lista-cartas)`, which sorts a list of
cards from smallest to largest value using the previous function
`ordena-generica`. You must include the `valor-carta` function and its helper
functions defined in previous labs.


Example:

```racket
(ordena-cartas '(Q♠ J♣ 5♣ Q♥ J♦)) ; ⇒ (5♣ J♣ J♦ Q♠ Q♥)
```

### Exercise 3 ###

a) Indicate what the following expressions return, without using the
interpreter. Then check whether you were right.

```racket
(map (lambda (x)
         (cond 
            ((symbol? x) (symbol->string x))
            ((number? x) (number->string x))
            ((boolean? x) (if x "#t" "#f"))
            (else "desconocido"))) '(1 #t hola #f (1 . 2))) ; ⇒ ?
         
(filter (lambda (x) 
            (equal? (string-ref (symbol->string x) 1) #\a)) 
    '(alicante barcelona madrid almería)) ; ⇒ ?

(foldr (lambda (dato resultado)
          (string-append dato "*" resultado)) "" 
          '("Hola" "que" "tal")) ; ⇒ ?

(foldr append '() '((1 2) (3 4 5) (6 7) (8))) ; ⇒ ?

(foldl (lambda (dato resultado)
         (string-append
          (symbol->string (car dato))
          (symbol->string (cdr dato))
          resultado)) "" '((a . b) (hola . adios) (una . pareja))) ; ⇒ ?

(foldr (lambda (dato resultado)
           (cons (+ (car resultado) dato)
                 (+ (cdr resultado) 1))) '(0 . 0) '(1 1 2 2 3 3)) ; ⇒ ?

(apply + (map cdr '((1 . 3) (2 . 8) (2 . 4)))) ; ⇒ ?

(apply min (map car (filter (lambda (p)
                                  (> (car p) (cdr p))) 
                                  '((3 . 1) (1 . 20) (5 . 2))))) ; ⇒ ?
```

b) Without using the DrRacket interpreter, fill in the following blanks to obtain
the expected result. Then use the interpreter to check whether you were right.


```racket 

; Los siguientes ejercicios utilizan esta definición de lista

(define lista '((2 . 7) (3 . 5) (10 . 4) (5 . 5)))


; Queremos obtener una lista donde cada número es la suma de las
; parejas que son pares

(filter ________
        (________ (lambda (x) (+ (car x)
                                 (cdr x)))
               lista))
; ⇒ (8 14 10)

; Queremos obtener una lista de parejas invertidas donde la "nueva"
; parte izquierda es mayor que la derecha.

(filter ___________
        (map ____________ lista))
; ⇒ ((7 . 2) (5 . 3))

; Queremos obtener una lista cuyos elementos son las partes izquierda
; de aquellas parejas cuya suma sea par.

(foldr __________ '()
        (_________ (lambda (x) (even? (+ (car x) (cdr x)))) lista))
; ⇒ (3 10 5)
```

c) Fill in the following blanks **with a single expression** that uses some
previously defined function (`f` or `g`). Check with the interpreter whether you
did it correctly.


```racket
(define (f1 x) (lambda (y z) (string-append y z x)))
(define g1 (f1 "a"))
(check-equal? ____________________ "claselppa")



(define (f2 x) (lambda (y z) (list y x z)))
_____________
(check-equal? (g2 "hola" "clase") (list "hola" "lpp" "clase"))


(define (f3 g3) (lambda(z x) (g3 z x)))
(check-equal? _____________________  '(3 . 4))
```

### Exercise 4 ###

a) Using higher-order functions, implement the function
`(contar-datos-iguales-fos lista-parejas)`, which receives a list of pairs and
returns the number of pairs whose two data items are equal.

```racket
(contar-datos-iguales-fos 
   '((2 . 3) ("hola" . "hola") (\#a . \#a) (true . false))) 
; ⇒ 2
(contar-datos-iguales-fos 
   '((2 . "hola") ("hola" . 3) (\#a . true) (\#b . false))) 
; ⇒ 0
```

b) Using higher-order functions, implement the function
`(expande-lista-fos lista-parejas)`, which does the same as the function
`(expande-lista lista-parejas)` from the previous lab. As in the previous lab,
you must use the `expande-pareja` function.

```
(expande-lista-fos '((#t . 3) ("LPP" . 2) (b . 4))) 
; ⇒ (#t #t #t "LPP" "LPP" b b b b))
```

c) Using higher-order functions, implement the function
`(comprueba-simbolos-fos lista-simbolos lista-num)`, which does the same as the
`comprueba-simbolos` function from exercise 3b) of the previous lab.

Example:

```
(comprueba-simbolos-fos '(este es un ejercicio de examen) '(2 1 2 9 1 6))
; ⇒ ((un . 2) (ejercicio . 9) (examen . 6))
```

### Exercise 5 ###

a) Using higher-order functions, implement the function `(suma-n-izq n
lista-parejas)`, which receives a list of pairs and returns another list where
`n` has been added to all the left parts.

Example

```racket
(suma-n-izq 10 '((1 . 3) (0 . 9) (5 . 8) (4 . 1)))
; ⇒ ((11 . 3) (10 . 9) (15 . 8) (14 . 1))
```

b) Complete the definition of the following higher-order function
`(busca-mayor mayor? lista)`, which searches for the largest element in a list.
It receives a predicate `mayor?` that compares two elements of the list and
returns `#t` or `#f` depending on whether the first one is greater than the
second.

By using a predicate as an argument, we are defining a generic function that we
can use to obtain the largest element of lists of numbers, strings, pairs, etc.
In each case, we must pass the appropriate comparison function as the `mayor?`
parameter.

```racket
(define (busca-mayor mayor? lista)
  (foldl __________ (first lista) (rest lista)))
```  


!!! Hint "Hint"
    Notice that, as the base element of `foldl`, we are using the first element
    of the list, and that the fold is performed over the rest of the list.

Write some `check-equal?` expressions to check that `busca-mayor` works, using
different `mayor?` functions.

c) Using the higher-order predicate `for-all?`, implement two versions of the
function `(todos-menores? lista n)`, which receives a list with sublists of
numbers and a number `n`, and checks whether all the numbers in the sublists are
less than `n`.

The first version must be implemented using `for-all?` and the `busca-mayor`
function defined in the previous part, and the second using `for-all?` and the
higher-order function `exists?`.

Example:

```racket
(todos-menores? '((10 30 20) (1 50 30) (30 40 90)) 100) ; ⇒ #t
(todos-menores? '((10 30 20) (1 50 30) (30 40 90)) 90) ; ⇒ #f
(todos-menores? '((10 30 20) (1 50 30) (30 40 90)) 55) ; ⇒ #f
```

### Exercise 6

We are going to improve last week's card game by using the full deck and giving
more freedom to the way cards are dealt into piles, making the guessing of the
chosen card even more implausible.

We use the `(cartas num-cartas)` function from the `lpp.rkt` file and the
`(reparte-tres lista-cartas)` function defined in the previous lab.

!!! Important "Use higher-order functions"
    For the implementation of the following functions, you should use
    higher-order functions instead of recursive functions whenever possible.

a) Define a new version of the `coloca` function using a variable number of
arguments. The new version of the `(coloca ...)` function has only the first
argument as mandatory: the list of n lists. The rest of the arguments are
optional and can range from 0 to n elements.

It is assumed that the list of n lists must have as many lists as elements are
passed as arguments, and if no argument is passed, by convention the list of n
lists is returned unchanged.

Example:

```racket
(coloca '(() () ()) 'a 'b 'c)) ; ⇒ ((a) (b) (c))
(coloca '((a) (a)) 'b 'b)) ; ⇒ ((b a) (b a))
(coloca '((a b c d)) 'e) ; ⇒ ((e a b c d))
(coloca '()) ; ⇒ '()
(coloca '((a) (b c) (d e f) (g h i j)) 'k 'l 'm 'n)) ; ⇒ ((k a) (l b c) (m d e f) (n g h i j))
```

Implement a `reparte-cuatro` function inspired by `reparte-tres` and with an
identical structure.

```racket
(reparte-cuatro '(A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣)) ; ⇒ '((A♣ 5♣ 9♣) (2♣ 6♣ J♣) (3♣ 7♣ Q♣) (4♣ 8♣ K♣))
```

b) Implement the function `(escoge-en-orden lista funcion_ordinal_1
... función_ordinal_n)`, which applies to the first mandatory argument, `lista`,
the series of "ordinal" functions (`first`, `second`, `third` ... `tenth`)
passed after the list as a variable number of arguments, returning the list of
results obtained by applying those functions in the order in which they were
provided.

```racket
(escoge-en-orden '(1 2 3 4 5)) ; ⇒  '()
(escoge-en-orden '(1 2 3 4 5) fourth second) ; ⇒ (4 2)
(escoge-en-orden '(a b c d) third second fourth first) ; ⇒ (c b d a)
(escoge-en-orden '(dos tres un) third first second) ; ⇒ (un dos tres)
```

Using the functions defined above, implement the functions
`(reordena-tres-montones baraja f-ordinal1 f-ordinal2 f-ordinal3)` and
`(reordena-cuatro-montones baraja f-ordinal1 f-ordinal2 f-ordinal3 f-ordinal4)`,
which deal the cards of a supposed deck (a list of cards) into three or four
piles (a list of sublists of cards) and then reorder the piles, or sublists,
according to the order established by the "ordinal" functions passed as
arguments after the deck.

```racket
(reordena-tres-montones  '(A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣) second first third)
; ⇒
; ((2♣ 5♣ 8♣ Q♣) (A♣ 4♣ 7♣ J♣) (3♣ 6♣ 9♣ K♣))
              
(reordena-cuatro-montones  '(A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣) fourth second first third)
; ⇒
; ((4♣ 8♣ K♣) (2♣ 6♣ J♣) (A♣ 5♣ 9♣) (3♣ 7♣ Q♣))
```

c) Implement the function `(junta-montones montones)`, which concatenates the
list of card sublists (piles) into a single list of cards.

```racket
(junta-montones '((4♣ 8♣ K♣) (2♣ 6♣ J♣) (A♣ 5♣ 9♣) (3♣ 7♣ Q♣)))
; ⇒
; (4♣ 8♣ K♣ 2♣ 6♣ J♣ A♣ 5♣ 9♣ 3♣ 7♣ Q♣)
```

d) Once you have implemented the previous functions, all that remains is to copy
the following definition so you can perform the card trick.

The function `(adivina lista-cartas par1 par2 par3)` is the one that does all
the magic and calculates the position of the chosen card from the positions of
the piles in which it has appeared in three deals of the deck.

```racket
(define (adivina baraja par1 par2 par3)
  (list-ref baraja
            (+ (* (- (car par3) 1) (cdr par2) (cdr par1))
               (* (- (car par2) 1) (cdr par1))
               (- (car par1) 1))))
```

Each pair encodes, in its right part, the number of piles into which the deck was
dealt and, in its left part, the pile in which the spectator saw the card. For
example, the pair `(2 . 4)` represents that the deck was dealt into 4 piles and
that the chosen card is in the second pile.

The curious thing about the guessing function is that it works correctly as long
as the deck has been dealt twice into four piles and once into three piles (the
right parts of the three pairs must add up to 11).

Let's see an example of playing the game, as we already did in the previous lab.

The following function, with the constant 90 as an argument, always generates the
random sequence that lets you follow the example. If it is changed to another
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

1. We deal a list of 48 cards into four piles. We ask a spectator to tell us the
   order in which to place the piles, for example, first the first pile, then the
   fourth, then the second, and then the third:

    ```racket
    (define t1 (reordena-cuatro-montones (cartas 48) first fourth second third))
    ```

2. We display the piles and ask the spectator to think of a card without saying
which one. For example, the ace of clubs.

    ```racket
    t1 ; ⇒ ((K♦ 3♦ 6♠ 6♦ 3♥ K♣ 8♦ 5♦ 6♣ 8♥ 5♠ A♣)
       ;   (8♠ 8♣ 9♠ 7♠ 2♣ 7♣ K♥ Q♠ 7♥ Q♣ 9♦ J♥)
       ;   (4♠ 2♥ K♠ Q♥ 7♦ J♣ 9♣ 6♥ 2♠ 9♥ 4♣ A♥)
       ;   (5♣ 2♦ J♦ 4♥ A♠ 5♥ 3♠ J♠ A♦ 3♣ 4♦ Q♦))
    ```

3. We ask the spectator which pile contains the card. We write in the left part
of `p1` the pile where it is (pile 1), and in the right part the number of piles
(4).

    ```racket
    (define p1 '(1 . 4))
    p1
    ```

4. We repeat the operation with `t2`, but now dealing into only three piles. We
can ask another spectator to tell us the order in which the piles are placed.
For example, first the second pile, then the third, and then the first.

    ```racket
    (define t2 (reordena-tres-montones (junta-montones t1) second third first))
    ```

5. We display `t2` and determine the pair according to where the ace of clubs is:

    ```racket
    t2 ; ⇒ ((3♦ 3♥ 5♦ 5♠ 8♣ 2♣ Q♠ 9♦ 2♥ 7♦ 6♥ 4♣ 2♦ A♠ J♠ 4♦)
       ;    (6♠ K♣ 6♣ A♣ 9♠ 7♣ 7♥ J♥ K♠ J♣ 2♠ A♥ J♦ 5♥ A♦ Q♦)
       ;    (K♦ 6♦ 8♦ 8♥ 8♠ 7♠ K♥ Q♣ 4♠ Q♥ 9♣ 9♥ 5♣ 4♥ 3♠ 3♣))
       ;En este caso (2 . 3) (el montón 2 de 3)
    (define p2 '(2 . 3))
    p2
    ```

6. We repeat the dealing and pile-ordering one last time, but with 4 piles. Three
deals must be made, one with 3 piles and the other two with 4, but not
necessarily in the order shown here (4-3-4). The deal into three piles could have
been done first, or left for the end.

    ```racket
    (define t3 (reordena-cuatro-montones (junta-montones t2) fourth second first third))
    ```

7. We display `t3` and define the pair `p3` according to the pile of the ace of
clubs:

    ```racket
    t3 ; ⇒ ((5♠ 9♦ 4♣ 4♦ A♣ J♥ A♥ Q♦ 8♥ Q♣ 9♥ 3♣)
       ;    (5♦ Q♠ 6♥ J♠ 6♣ 7♥ 2♠ A♦ 8♦ K♥ 9♣ 3♠)
       ;    (3♦ 8♣ 2♥ 2♦ 6♠ 9♠ K♠ J♦ K♦ 8♠ 4♠ 5♣)
       ;    (3♥ 2♣ 7♦ A♠ K♣ 7♣ J♣ 5♥ 6♦ 7♠ Q♥ 4♥))
       ;Esta vez es (1 . 4)
    (define p3 '(1 . 4))
    p3
    ```

8. We now have the three magic pairs that let us guess the card:

    ```racket
    (adivina (junta-montones t3) p1 p2 p3) ; ⇒ A♣
    ```

----

Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
