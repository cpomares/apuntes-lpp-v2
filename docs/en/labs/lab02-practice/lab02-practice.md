# Lab 2: Functional Programming in Scheme


## Before the Lab Session ##

- Before starting this lab, it is important that you review the solution to
  lab 1. You can ask your lab instructor any questions you may have.

- The following exercises are based on the theory concepts covered last week.
Before the lab session, you should review all the concepts and **try in
DrRacket** all the examples from topic 2 [_Functional
Programming_](../../theory/topic02-functional-programming/topic02-functional-programming.md)
up to and including section 2.6 _Lists_.


## Exercises

Open DrRacket and create a file called `lab2.rkt`, where you should write all
the examples and exercise solutions you complete. Write your first and last name
in comments. Also use comments to separate sections and add notes. Include in
the file all the code, examples, and exercise solutions you work on this week.

You must also add test cases to the code of all the functions you implement, as
we saw at the end of the Scheme seminar. You can use some of the examples from
the statements, but you should also build some new cases with examples created
by you.

!!! Note "You must always include test cases"
    Test cases are an important component of the code, because they allow you to
    keep in the code itself a demonstration that it works correctly, as well as
    examples of how to call the defined functions.

### Exercise 1

a) Implement the function `(binario-a-decimal b3 b2 b1 b0)`, which receives
4 bits representing a binary number and returns the equivalent decimal number.

```racket
(binario-a-decimal 1 1 1 1) ; ⇒ 15
(binario-a-decimal 0 1 1 0) ; ⇒ 6
(binario-a-decimal 0 0 1 0) ; ⇒ 2
```

**Note**: remember that to perform this conversion, the following formula is
used:

```text
n = b3 * 2ˆ3 + b2 * 2ˆ2 + b1 * 2ˆ1 + b0 * 2ˆ0
```

For the implementation of the expression, you must use the `expt` function.


b) Implement the function `(binario-a-hexadecimal b3 b2 b1 b0)`, which receives
4 bits of a number represented in binary and returns the character corresponding
to its hexadecimal representation.

```racket
(binario-a-hexadecimal 1 1 1 1) ; ⇒ #\F
(binario-a-hexadecimal 0 1 1 0) ; ⇒ #\6
(binario-a-hexadecimal 1 0 1 0) ; ⇒ #\A
```

**Note**: to perform this conversion, as an intermediate step you must first
convert the binary number to its decimal representation (using the function
defined in the previous part) and then to its corresponding hexadecimal
representation.

Remember that the hexadecimal representation of decimal numbers from 0 to 9 is
the character corresponding to that number, and that decimal number 10 is
represented by the character A, 11 by B, and so on up to 15, which is F in
hexadecimal.

To implement this helper function that converts from decimal to hexadecimal, you
must use the `integer->char` and `char->integer` functions. In the
`char->integer` function, consecutive characters are associated with consecutive
numbers. For example, the integer corresponding to the character `#\A` is one
less than the integer corresponding to the character `#\B`. Digit characters and
letter characters are not consecutive.


### Exercise 2

The Caesar cipher is a substitution cipher technique in which each letter of the
text is encoded as the corresponding letter shifted by a certain number of
places. For example, if we use a shift of 5, the character `#\c` would be
encoded as the character `#\h` (the character 5 positions after `#\c` in the
alphabet).

We are going to encrypt and decrypt lowercase and uppercase letters of the
English alphabet (26 characters: from `#\a or #\A` to `#\z or #\Z`). We will
work with a variable shift, positive or negative, depending on the direction in
which we rotate the alphabet.

Define the functions `(cifra-caracter char desplazamiento)` and
`(descifra-caracter char desplazamiento)` that implement the cipher described
above.

To implement the previous functions, you must define and use the following
helper functions:

- `(encuentra-indice char)`
- `(encuentra-caracter indice)`
- `(entre-az? char)`
- `(rota-indice indice desplazamiento)`

The function `(rota-indice indice desplazamiento)` receives the index of the
original character and calculates the index of the encrypted character.

**Tip**: you can use the `modulo` function [see documentation](https://docs.racket-lang.org/reference/generic-numbers.html#(def._((quote._~23~25kernel)._modulo))).

Analyze the following examples to better understand how the helper functions and
the main functions work:

```racket
(encuentra-indice #\a) ; ⇒ 0
(encuentra-indice #\b) ; ⇒ 1
(encuentra-indice #\m) ; ⇒ 12
(encuentra-indice #\z) ; ⇒ 25

(encuentra-caracter 0) ; ⇒ #\a
(encuentra-caracter 1) ; ⇒ #\b
(encuentra-caracter 12) ; ⇒ #\m
(encuentra-caracter 25) ; ⇒ #\z

(entre-az? #\a) ; ⇒ #t
(entre-az? #\m) ; ⇒ #t
(entre-az? #\z) ; ⇒ #t
(entre-az? #\`) ; ⇒ #f
(entre-az? #\{) ; ⇒ #f

(rota-indice 4 12) ; ⇒ 16)
(rota-indice 4 24) ; ⇒ 2)
(rota-indice 4 -5) ; ⇒ 25)

(cifra-caracter #\c 5) ; ⇒ #\h)
(cifra-caracter #\z -1) ; ⇒ #\y)
(cifra-caracter #\j 40) ; ⇒ #\x)
(cifra-caracter #\D 3) ; ⇒ #\G)
(cifra-caracter #\ñ 3) ; ⇒ #\ñ)

(descifra-caracter #\d 3) ; ⇒ #\a)
(descifra-caracter #\y -1) ; ⇒ #\z)
(descifra-caracter #\x 40) ; ⇒ #\j)
(descifra-caracter #\G 3) ; ⇒ #\D)
(descifra-caracter #\tab 3) ; ⇒ #\tab)
```


### Exercise 3

Implement the function `(menor-de-tres n1 n2 n3)`, which receives three numbers
as arguments and returns the smallest of the three, trying to keep the number of
conditions as small as possible.

You must not use the `min` function.

Implement two versions of the function:

- version 1: using the `if` special form
- version 2 (call it `menor-de-tres-v2`): without using the `if` special form;
  instead, define a helper function `(menor x y)` that returns the smaller of
  two numbers (in this helper you should use `if`) and build the
  `menor-de-tres-v2` function as a composition of calls to this helper function.

```racket
(menor-de-tres 2 8 1) ;; ⇒ 1
(menor-de-tres-v2 3 0 3) ;; ⇒ 0
```

### Exercise 4

a) Suppose we have the definitions

```racket
(define (f x)
    (cons x 2))

(define (g x y)
    (cons x y))
```

Perform the step-by-step evaluation of the following expression

```racket
(g (f (+ 2 1)) (+ 1 1))
```

using the **substitution model**, with both **applicative order** and **normal
order**.

Write the solution inside comments in the lab's own `.rkt` file.

b) Suppose we have the definitions

```racket
(define (func-1 x)
    (/ x 0))
    
(define (func-2 x y)
    (if (= x 0)
        0
        y))
```

As in the previous part, perform the step-by-step evaluation of the following
expression

```racket
(func-2 0 (func-1 10))
```

using the **substitution model**, with both **applicative order** and **normal
order**. Write the solution inside comments in the lab's own `.rkt` file.


### Exercise 5

Implement the function `(cadenas-mayores lista1 lista2)`, which receives 2 lists
with 3 strings and returns another list with the 3 longer strings, comparing the
strings at each position of the list. When the strings have the same length, the
string from the first list is returned.

!!! Note "Hint"
    You can use the `second` and `third` functions, which return the second and
    third element of a list.

```racket
(cadenas-mayores '("hola" "que" "tal") '("meme" "y" "adios")) ; ⇒ ("hola" "que" "adios")
(cadenas-mayores '("esto" "es" "lpp") '("hoy" "hay" "clase")) ; ⇒ ("esto" "hay" "clase")
```


### Exercise 6

a) Suppose we want to program a card game that uses the French deck. The first
thing we need to do is define a way to represent cards and functions that work
with that representation. In this exercise we will implement those functions.

We will represent a card with a two-letter symbol: the first one indicates its
number or face, and the second one indicates the card suit, represented with the
corresponding UTF symbol.

!!! Note "UTF symbols for the suits of the French deck"
    You can copy the following UTF symbols and paste them into the lab source
    code: ♠, ♣, ♥ and ♦ (spades, clubs, hearts, and diamonds).

For example:

```racket
(define tres-de-picas '3♠)
(define as-de-corazones 'A♥)
(define jota-de-diamantes 'J♦)
```

We must define the function `carta`, which returns a pair with the value
corresponding to its order in the French deck (a number) and the name of the
card suit (as a symbol, not as a string).

```racket
(carta tres-de-picas) ; ⇒ (3 . Picas)
(carta as-de-corazones) ; ⇒ (1 . Corazones)
(carta 'K♣) ; ⇒ (12 . Tréboles)
```

The card values in the French deck are:

```text
A (As) ⇒ 1
J (Jota) ⇒ 10
Q (Reina) ⇒ 11
K (Rey) ⇒ 12
```

To complete the exercise, you must first define the functions `(obten-palo char)`
and `(obten-valor char)`, which return the suit and value, given a character.
Then you must implement the `carta` function using these two functions.

```racket
(obten-palo #\♠) ; ⇒ Picas
(obten-palo #\♥) ; ⇒ Corazones
(obten-valor #\3) ; ⇒ 3
(obten-valor #\J) ; ⇒ 10
```

!!! Note "Hint"
    You can use the functions `(symbol->string simbolo)`, which converts a
    symbol into a string, and `(string-ref cadena pos)`, which returns the
    character of a string located at a given position.

b) Implement the function `(jugada-mano carta1 carta2 carta3)`, which receives 3
cards from the French deck and returns a string indicating whether the
three-card hand contains a **pair** (two cards with the same value), a **three of
a kind** (all three cards have the same value), or **nothing** (all three cards
are different), and also the value of the pair or three of a kind.

To obtain the values of the cards, you must implement the function
`(valor-carta carta)`.

Examples:

```racket
(jugada-mano '3♥ '3♣ '3♥) ; ⇒ "trío de 3"
(jugada-mano 'K♦ '7♠ 'K♥) ; ⇒ "pareja de 12"
(jugada-mano '5♣ '4♣ '6♣) ; ⇒ "nada"
```

!!! Note "Numbers to strings"
    You can obtain a string corresponding to a number using the `number->string`
    function. You should only use this function in this exercise.


----
Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
