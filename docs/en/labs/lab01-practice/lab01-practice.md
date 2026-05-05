# Lab 1: Scheme Seminar

## Completing the Lab ##

1. Install DrRacket on your computer, as explained at the beginning of
   the [Scheme
   seminar](../../seminars/seminar01-scheme/seminar01-scheme.md),
   and create a file called `lab1.rkt`. Include in this file all the code you
   write this week. Use comments (lines that start with `;`) to separate sections
   and add notes.

   This file will be useful for saving your lab work. To submit the assignment,
   you will need to copy the solutions for each exercise into the quiz that will
   be enabled in Moodle.

2. Read the Scheme seminar up to and including section 2.4. (_Simple data
   types_). You can watch **video 1** on the seminar videos page (week 1 in
   Moodle).

    As you read the text or watch the video, try all the examples shown in the
    Racket interpreter. Try them interactively in DrRacket's interactions panel
    and save the definitions in the editing panel of the `lab1.rkt` file.

3. Do the following exercise.

    **Exercise 1**. Launch DrRacket and type each of the following instructions
    in the interpreter, trying to guess the result it will return. They are
    ordered by difficulty from top to bottom and from left to right. Think about
    the results! Try to understand how Scheme interprets what you write.


    |Instruction      | Instruction                                    |
    |---------------- | -----------------------------------------------|
    |`3`              | `(+ (- 4 (* 3 (/ 4 2) 4)) 3)`                  |
    |`(+ 1 2 )`       | `(* (+ (+ 2 3) 4) (* (* 3 3) 2))`              |
    |`(+ 1 2 3 4)`    | `(* (+ 2 3 4 5) 3 (- 5 2 1))`                  |
    |`(+)`            | `(+ (- (+ (- (+ 2 3) 5) 1) 2) 3)`              |
    |`(sqrt 25)`      | `(- (sqrt (* 5 ( + 3 2))) (+ 1 1 1 1))`        |
    |`(* (+ 2 3) 5)`  | `(> (* 3 (+ 2 (+ 3 1)) (+ 1 1)) (+ (* 2 2) 3))`|
    |`+`              | `(= (* 3 2) (+ 1 (+ 2 2) 1))`                  |
    |`#\+`            | `(not (> (+ 3 2) 5))`                          |
    |`"+"`            | `(and (even? 2) (odd? (+ 3 2)))`               |
    |`"hola"`         | `(remainder (+ 6 2) (+ 1 1))`                  |


4. Read section 2.5. (_Compound data types_) of the Scheme seminar, which
   explains how to work with strings, pairs, and lists in Racket. You can watch
   **video 2** on the seminar videos page in Moodle.

    Try all the examples from the seminar in the Racket interpreter.

5. Do the following exercises.

    **Exercise 2** on pairs. Predict what Scheme will do when you write the
    following expressions. They are ordered by difficulty from top to bottom and
    from left to right. Then try them and check whether your prediction was
    correct. If it was not, try to understand why.

    | Instruction                           | Instruction                       |
    |---------------------------------------|-----------------------------------|
    | `(cons 1 2)`                          | `(car (car (cons (cons 1 2) 3)))` |
    | `(car (cons 1 2))`                    | `(car (cons (cons 3 4) 2))`       |
    | `(cdr (cons 1 2))`                    | `(cdr (cons (cons 3 4) 2))`       |
    | `(cons (* 2 3) (/ 4 2))`              | `(cdr (cons 1 (cons 2 3)))`       |
    | `(cons (+ 2 1) (if (> 2 3) "2" "3"))` | `(cdr (car (cons (cons 1 2) 3)))` |


    **Exercise 3** on lists. Predict what Scheme will do when you write the
    following expressions. Then try them and check whether your prediction was
    correct. If it was not, try to understand why.

    | Instruction                                    | Instruction                              |
    |------------------------------------------------|------------------------------------------|
    | `(list 1 2 3 4)`                               | `(cons 3 '(1 2 3))`                      |
    | `(rest (list 1 2 3 4))`                         | `(rest (cons #t (cons "Hola" (list 1))))` |
    | `(first '(1 2 3 4))`                             | `(first (list (list 1 2) 1 2 3 4))`        |
    | `(first (list #t 1 "Hola"))`                     | `(first (rest '((1 2) 1 2)))`               |
    | `(first (rest (list 1 2 3 4)))`                   | `(cons '(1 2 3) '(4 5 6))`               |
    | `(rest (rest '(1 2 3 4)))`                       | `(first (rest (list 1 2 3 4)))`             |
    | `(first (rest (rest (list 1 2 3 4))))`             | `(rest (rest (list 1 2 3 4)))`             |
    | `(list (* 2 2) (+ 1 2) (/ 4 2))`               | `(first (rest (rest (rest '(1 2 3 4)))))`     |
    | `(list (+ 2 3) (- 3 4) (string-ref "hola" 3))` |                                          |


    **Exercise 4** on lists. Try to complete the following items without using
    the Scheme interpreter. Then check whether you were right.

    a) Given the following list, indicate the correct expression so that Scheme
    returns 3:

    ```racket
    (list 1 2 3 4 5)
    ```

    b) Given the following list, indicate the correct expression so that Scheme
    returns (5).

    ```racket
    (list 1 2 3 4 5)
    ```

    c) Given the following list, indicate the correct expression so that Scheme
    returns 5.

    ```racket
    (list 1 2 3 4 5)
    ```

    d) Given the following expression, what does Scheme return?

    ```racket
    (first (rest (rest (list 1 (list 2 3) (list 4 5) 6))))
    ```

    e) Given the following expression, what does Scheme return?

    ```racket
    (rest (rest '(1 (2 3) 4 5)))
    ```

6. Read section 3 (_Control structures_) of the Scheme seminar. You can watch
   **video 3** up to minute 7:00 on the seminar videos page in Moodle.

7. Do the following exercise.

    **Exercise 5**. Predict what Scheme will return when you write the following
    expressions. They are ordered by difficulty from top to bottom and from left
    to right. Then try them and check whether your prediction was correct. If it
    was not, try to understand why.

    | Instruction                                    | Instruction                                                               |
    |------------------------------------------------|---------------------------------------------------------------------------|
    | `(equal? "hola" "hola")`                       | `(+ (char->integer(integer->char 1200)) (char->integer #\A))`             |
    | `(string-ref "pepe" 1)`                        | `(string-length (make-string 7 #\E))`                                     |
    | `(substring "buenos dias" 1 4)`                | `(define a 3)` <br/> `(define b (+ a 1))`                                 |
    | `(= "hola" "hola")`                            | `(+ a b (* a b))`                                                         |
    | `(string-ref (substring "buenos dias" 2 5) 1)` | `(= a b)`                                                                 |
    | `(define pi 3.14159)`                          | `(if (and (> a b) (< b (* a b))) b a)`                                    |
    | `pi`                                           | `(cond ((= a 4) 6)`<br/>`((= b 4) (+ 6 7 a))`<br/>`(else 25))`            |
    | `"pi"`                                         | `(+ 2 (if (> b a) b a))`                                                  |
    | `(+ pi (+ pi pi))`                             | `(* (cond ((> a b) a)` <br/>`((< a b) b)`<br/>`(else -1))`<br/>`(+ a 1))` |
    | `(+ (* pi pi) (- 2 pi pi pi pi))`              | `((if (< a b) + -) a b)`                                                  |

8. Read the rest of the seminar, from section 4 to the end. You can watch
   **video 3** from minute 7:00 to the end on the seminar videos page in Moodle.

    - Try the `ecuacion` and `convertir-temperatura` functions and reflect on
      how they are implemented.

    - Try the unit tests for the `ecuacion` function. Change the function
      definition to introduce an error and cause the unit tests to fail. Fix the
      function definition so that it works again.

9. Do the following exercise.

    **Exercise 6**

    a) Define the function `(distancia p1 p2)` that calculates the distance
    between two points, represented by pairs of integer numbers. Add the
    following tests to check that it works correctly:


    | Input                 | Output   |
    |-----------------------|----------|
    | `p1:(0, 0) p2:(0, 10)`  | `10`     |
    | `p1:(0, 0) p2:(10, 0)`  | `10`     |
    | `p1:(0, 0) p2:(10, 10)` | `14.142135623730951`     |


    b) Using the `distancia` function defined above, implement the function
    `isosceles?`, which receives the three coordinates of the vertices of a
    triangle and must return whether the figure is an isosceles triangle. To do
    so, you must check that the three sides are not all equal (that would be
    equilateral) and that one of the following three conditions holds: either the
    first side is equal to the second, the first side is equal to the third, or
    the second side is equal to the third.

    Notice that the Boolean functions `and`, `or`, and `not` already return a
    Boolean value, and that functional programming uses function composition.

    You must implement the function using a single expression in which you do
    not use `if`, but rather a composition of Boolean expressions.

    !!! Hint "Hint"
        Remember from the seminar that the `=` function can have more than two
        arguments.

    Add the corresponding tests for the following examples:

    ```racket
    ; Ejemplos de triángulos isósceles:
    
    ; p1: (0, 0) p2: (3, 3) p3: (6, 0)
    ; p1: (2, 2) p2: (4, 0) p3: (0, 0)

    ; No isósceles:

    ; p1: (0, 0) p2: (0, 0) p3: (0, 0) (igual la distancia entre los tres puntos)
    ; p1: (0, 0) p2: (1, 1) p3: (3, 2) (ningún lado igual)
    
    (isosceles? '(0 . 0) '(3 . 0) '(6 . 0)) ; ⇒ #t
    (isosceles? '(2 . 2) '(4 . 0) '(0 . 0)) ; ⇒ #t
    (isosceles? '(0 . 0) '(0 . 0) '(0 . 0)) ; ⇒ #f
    (isosceles? '(0 . 0) '(1 . 1) '(3 . 2)) ; ⇒ #f
    ```


## Lab Submission

Copy the lab exercises into the _Lab 1 submission_ quiz. The deadline is next
Sunday at 21:00. Once the submission deadline has passed, you will be able to
review the quiz and view the solution. In this case, the only exercise with a
solution is exercise 6.

Once the solution is available, compare it with yours. You can ask your lab
instructor any questions during next week's lab session.

----
Programming Languages and Paradigms, academic year 2025-26  
© Department of Computer Science and Artificial Intelligence, University of Alicante  
Domingo Gallardo, Cristina Pomares, Antonio Botía, Francisco Martínez
