---
marp: true
theme: lpp-light
title: "LPP: Semana 9"
lang: es
size: 16:9
paginate: true
footer: "LPP · Tema 5: Programación funcional con Swift · Parte 2"
---

<!-- _class: cover institutional-cover -->
<!-- _paginate: false -->
<!-- _footer: "" -->
<div class="system-week">Semana 9</div>

# Opcionales y clausuras<br>en Swift

<div class="system-topics">Funciones de orden superior<br>Genéricos y listas recursivas</div>
<div class="system-author">Cristina Pomares Puig</div>
<div class="institutional-logos">
<img class="university-logo" src="imagenes/logo-ua.svg" alt="Universitat d’Alacant · Universidad de Alicante">
<img class="department-logo" src="imagenes/logo-dccia.jpg" alt="Departamento de Ciencia de la Computación e Inteligencia Artificial">
</div>
<div class="mascot-figure cover-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>

<!-- Fuente: notas-clase/semana09/semana09.md. Diseño: semana 1, tema lpp-light. -->

---

## Veremos hoy

1. Opcionales y ausencia de valor.
2. Ligado y encadenamiento de opcionales.
3. Expresiones de clausura y captura de variables.
4. `map`, `filter` y `reduce`.
5. Funciones y listas genéricas.

<!--
Marcas institucionales: https://imagenycomunicacion.ua.es/es/identidad-visual-corporativa-y-logotipos-ua.html
Logo DCCIA: https://web.ua.es/es/dccia/imagenes/gestadm/logotipos/logodccia.jpg
-->

<!--
Fuente: Veremos hoy. Notas de clase de la semana 9.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 9</div>

# Opcionales

<p class="lead">Expresar en el tipo que un resultado puede no existir.</p>

---

<!-- _class: lesson-code -->

## Un valor o `nil`

```swift
var cadena: String? = "Hola"
cadena = nil
```

`String?` admite una cadena o ausencia de valor. Una variable de tipo `String` no admite `nil`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 53. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Una búsqueda puede no encontrar un valor

```swift
var edades = [
    "Raquel": 30,
    "Pedro": 22,
]
let edad1 = edades["Raquel"]
let edad2 = edades["Ana"] // devuelve nil
```

Los accesos al diccionario devuelven `Int?`. La clave `"Ana"` no existe y produce `nil`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 68. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Desenvoltura de un opcional

```swift
var x: Int? = 10
let y = x + 10 
// error: value of optional type 'Int?' must be unwrapped to a value of type 'Int'
```

<!--
Fuente: Desenvoltura de un opcional. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Desenvoltura de un opcional (continuación)

```swift
var x: Int? = 10
let y = x! + 10 
print(y)
// Imprime "20"
```

El primer fragmento es un error intencionado. `!` extrae el valor, pero exige que exista.

<!--
Fuente: Desenvoltura de un opcional. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Desenvolver `nil` produce un error fatal

```swift
var respuestaEncuesta: String?
print(respuestaEncuesta!)
// Fatal error: Unexpectedly found nil while unwrapping an Optional value
```

Una variable opcional declarada así se inicializa a `nil`. No es seguro aplicar `!` sin conocer su estado.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 115. Notas de clase de la semana 9.
Ejemplo de error intencionado; no ejecutarlo junto con los demás ejemplos.
-->

---

## Ligado opcional

```swift
if let respuesta = leerRespuesta() {
    print ("Respuesta: " + respuesta)
}
```

Si hay una respuesta, el cuerpo dispone de un `String` llamado `respuesta`. Si no hay valor, el cuerpo no se ejecuta.

<!--
Fuente: Ligado opcional. Notas de clase de la semana 9.
leerRespuesta es una función conceptual que debe estar definida para ejecutar el ejemplo.
-->

---

<!-- _class: lesson-code -->

## Suma recursiva con `first` opcional

```swift
func sumaValores(_ valores: [Int]) -> Int {
    if let primero = valores.first {
        let resto = Array(valores.dropFirst())
        return primero + sumaValores(resto)
    } else {
        return 0
    }
}
print(sumaValores([1,2,3,4,5,6,7,8])) 
// Imprime "36"
```

Si `first` tiene valor, procesamos primero y resto. Si el array está vacío, devolvemos `0`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 199. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Ligado de varios valores

```swift
var x1: Int? = pedirNumUsuario()
var x2: Int? = pedirNumUsuario()
var x3: Int? = pedirNumUsuario()
if let dato1 = x1, let dato2 = x2, let dato3 = x3 {
   let suma = dato1+dato2+dato3
   print("Ningún nil y la suma de todos los datos es: \(suma)")
} else {
   print("Algún dato del usuario es nil")
}
```

El cuerpo principal solo se ejecuta cuando todos los opcionales tienen valor.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 220. Notas de clase de la semana 9.
pedirNumUsuario es una función de apoyo que debe implementarse en el entorno.
-->

---

<!-- _class: lesson-code -->

## Comparaciones de opcionales

```swift
var x: Int? = 10
x == 10 // devuelve true
x != nil // devuelve true
x == 0 // devuelve false
// Asignamos nil a x
x = nil
x == nil // devuelve true
x == 10 // devuelve false
```

`==` y `!=` permiten comprobar igualdad y ausencia sin usar desenvoltura forzosa.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 239. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Un valor por defecto con `??`

```swift
let a: Int? = nil
let b: Int? = 10
let x = a ?? -1
let y = b ?? -1
print("Resultado: \(x), \(y)")
// Imprime Resultado: -1, 10
```

El operador de coalescencia nula devuelve el valor contenido o, si hay `nil`, el valor alternativo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 258. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Encadenamiento de opcionales

```swift
let nombre1: String? = "Pedro"
let nombre2: String? = nil
// Error: let str1 = nombre1.lowercased()
// No podemos llamar al método lowercased() del String
// porque nombre es opcional y puede tener nil
let str1 = nombre1?.lowercased()
let str2 = nombre2?.lowercased()
// str1: String? = "pedro"
// str2: String? = nil
```

`?.` llama al método cuando existe el valor. El resultado sigue siendo opcional.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 276. Notas de clase de la semana 9.

-->

---

## Una lista cuyo resto es opcional

<div class="columns equal">
<div>

```swift
indirect enum Lista{
  case nodo(Int, Lista?)
}
```

</div>
<div>

El caso `nodo` contiene un entero y un resto de tipo `Lista?`.

El resto `nil` termina la lista.

Podemos usar `Lista?` también para representar una lista vacía.

</div>
</div>



<!--
Fuente: Una lista cuyo resto es opcional. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Recorrer la lista opcional

```
func suma(lista: Lista?) -> Int {
    switch lista {
        case nil:
            return 0
        case let .nodo(first, rest):
            return first + suma(lista: rest)
    }
}
let z: Lista = .nodo(20, .nodo(10, nil))
print(suma(lista: z))
/// Devuelve 30
```

El `switch` distingue ausencia y nodo. La recursión continúa con el resto opcional.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 306. Notas de clase de la semana 9.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 9</div>

# Expresiones de clausura

<p class="lead">Crear una función anónima en el punto donde se necesita.</p>

---

<!-- _class: lesson-code -->

## Un criterio para `sorted(by:)`

```swift
func primeroMayor(s1: String, s2: String) -> Bool {
    return s1 > s2
}
let estudiantes = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
let alreves = estudiantes.sorted(by: primeroMayor)
print(alreves)
// Imprime ["Peter", "Kweku", "Kofi", "Akosua", "Abena"]
```

La función devuelve `true` cuando el primer elemento debe aparecer antes que el segundo. Usar `>` produce orden descendente.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 360. Notas de clase de la semana 9.

-->

---

## Sintaxis de una expresión de clausura

```text
{ ( <parametros>) -> <tipo devuelto> in
   <sentencias>
}
```

`in` separa los parámetros y el tipo devuelto del cuerpo. Las expresiones de clausura cumplen el papel de las expresiones lambda en Scheme.

<!--
Fuente: Sintaxis de una expresión de clausura. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## El criterio como expresión de clausura

```swift
let alreves = estudiantes.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```

La función de comparación queda escrita en la llamada que la utiliza.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 389. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Inferir los tipos y omitir `return`

```swift
let alreves = estudiantes.sorted(by: { s1, s2 in return s1 > s2 } )
```

<!--
Fuente: Inferir los tipos y omitir `return`. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Inferir los tipos y omitir `return` (continuación)

```swift
let alreves = estudiantes.sorted(by: { s1, s2 in s1 > s2 } )
```

El contexto conoce los tipos. En una clausura de una sola expresión, la devolución puede ser implícita.

<!--
Fuente: Inferir los tipos y omitir `return`. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Argumentos abreviados y función operadora

```swift
let alreves = estudiantes.sorted(by: { $0 > $1 } )
```

<!--
Fuente: Argumentos abreviados y función operadora. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Argumentos abreviados y función operadora (continuación)

```swift
let alreves = estudiantes.sorted(by: >)
```

`$0` y `$1` designan los argumentos. El propio operador `>` también tiene el perfil requerido.

<!--
Fuente: Argumentos abreviados y función operadora. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Clausuras al final

```swift
let alreves = estudiantes.sorted() { $0 > $1 }
```

<!--
Fuente: Clausuras al final. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Clausuras al final (continuación)

```swift
let alreves = estudiantes.sorted { $0 > $1 }
```

Si la clausura es el último argumento, se puede escribir después de los paréntesis. Si es el único, los paréntesis pueden omitirse.

<!--
Fuente: Clausuras al final. Notas de clase de la semana 9.

-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 9</div>

# Captura de variables

<p class="lead">Una clausura conserva acceso al ámbito en el que se creó.</p>

---

<!-- _class: lesson-code -->

## Un incrementador con estado

```swift
func construyeIncrementador(incremento cantidad: Int) -> () -> Int {
    var totalAcumulado = 0
    func incrementador() -> Int {
        totalAcumulado += cantidad
        return totalAcumulado
    }
    return incrementador
}
```

La clausura captura `cantidad` y `totalAcumulado`. Cada llamada cambia el total: esta función no es pura.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 518. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Llamadas a la misma clausura

```swift
let incrementaDiez = construyeIncrementador(incremento: 10)
incrementaDiez()
// devuelve 10
incrementaDiez()
// devuelve 20
incrementaDiez()
// devuelve 30
```

El estado capturado permanece entre llamadas. Los resultados son `10`, `20` y `30`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 558. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Dos clausuras, dos estados

```swift
let incrementaSiete = construyeIncrementador(incremento: 7)
incrementaSiete()
// devuelve 7
```

<!--
Fuente: Dos clausuras, dos estados. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Dos clausuras, dos estados (continuación)

```swift
incrementaDiez()
// devuelve 40
```

La segunda construcción crea su propio acumulador. No cambia el estado de `incrementaDiez`.

<!--
Fuente: Dos clausuras, dos estados. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Dos nombres para la misma clausura

```swift
let tambienIncrementaDiez = incrementaDiez
tambienIncrementaDiez()
// devuelve 50
```

Asignar la clausura a otra constante comparte la misma captura. Siguiendo la secuencia anterior, el total pasa de `40` a `50`.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 707. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Devolver una expresión de clausura

```swift
func construyeSumador10() -> (Int) -> Int {
    return {$0 + 10}
}
let f = construyeSumador10()
print(f(20))
// Imprime "30"
```

No necesitamos una función local con nombre si una expresión de clausura expresa el mismo cálculo.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 608. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Incrementador con una expresión de clausura

```swift
func construyeIncrementador(incremento cantidad: Int) -> () -> Int {
    var totalAcumulado = 0
    return {totalAcumulado += cantidad
            return totalAcumulado}
}
let incrementaDiez = construyeIncrementador(incremento: 10)
print(incrementaDiez())
// Imprime "10"
print(incrementaDiez())
// Imprime "20"
```

La sintaxis cambia, pero el acumulador capturado sigue siendo mutable.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 633. Notas de clase de la semana 9.
Es una definición alternativa del incrementador. Ejecutarla como ejemplo independiente para no duplicar definiciones.
-->

---

<!-- _class: lesson-code -->

## Ámbito de definición y de invocación

```swift
func construyeFunc() -> () -> Int {
   var x = 0
   return {
      x = x + 1
      return x
   }
}
let f = construyeFunc()
print(f()) // -> ?
print(f()) // -> ?
```

Las dos primeras llamadas devuelven `1` y `2`.

<!--
Fuente: Variables capturadas y ámbito de invocación. Notas de clase de la semana 9.
La x capturada pertenece a la invocación de construyeFunc.
-->

---

<!-- _class: lesson-code -->

## La variable local del llamador

```swift
func usaFunc(_ f: () -> Int) -> Int {
     var x = 10
     return f()
}
print(usaFunc(f)) // -> ?
```

La llamada devuelve `3`, no `11`: la clausura usa su propia `x` capturada.

<!--
Fuente: Variables capturadas y ámbito de invocación. Notas de clase de la semana 9.
No busca x en el ámbito de usaFunc.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 9</div>

# Operaciones sobre colecciones

<p class="lead">Transformar, seleccionar y plegar mediante funciones de orden superior.</p>

---

<!-- _class: lesson-code -->

## Transformación con `map`

```swift
let numeros = [Int](0...5)
numeros.map {$0 * $0}
// devuelve [0, 1, 4, 9, 16, 25]
```

Cada elemento se transforma en un nuevo resultado. La clausura puede devolver otro tipo de dato.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 749. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Sumar los componentes de cada pareja

```swift
func suma(parejas: [(Int, Int)]) -> [Int] {
   return parejas.map({(pareja: (Int, Int)) -> Int in
                        return pareja.0 + pareja.1})
}
suma(parejas:[(1, 1), (2, 2), (3, 3), (4, 4)])
// devuelve [2, 4, 6, 8]
```

Cada tupla se transforma en un entero. El resultado es un array de enteros.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 760. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Transformación con una variable capturada

```swift
func incrementa(valores: [Int], con: Int) -> [Int] {
   return valores.map {$0 + con}
}
incrementa(valores: [10, 20, 30], con: 5)
// devuelve [15, 25, 35]
```

La clausura utiliza el parámetro `con` al transformar cada valor.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 784. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Selección con `filter`

```swift
let numeros = [Int](0...10)
numeros.filter {$0 % 2 == 0}
// devuelve [0, 2, 4, 6, 8, 10]
```

Conserva los elementos para los que la clausura devuelve `true`, sin transformarlos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 808. Notas de clase de la semana 9.

-->

---

## Plegado con `reduce`

```swift
func reduce<Result>(_ initialResult: Result, 
                    _ nextPartialResult: (Result, Element) -> Result) -> Result
```

En Swift, la función de combinación recibe primero el **resultado acumulado** y después el **elemento**.

Este orden de argumentos difiere del `foldl` de Racket utilizado en clase.

<!--
Fuente: Plegado con `reduce`. Notas de clase de la semana 9.
Destacar el orden al pasar de Scheme a Swift; las operaciones no conmutativas lo hacen visible.
-->

---

<!-- _class: lesson-code -->

## Sumar con `reduce`

```swift
let numeros = [Int](0...10)
numeros.reduce(0, +)
```

El resultado inicial es `0`. Cada paso combina el resultado parcial con el elemento siguiente.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 834. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Acumular la longitud de las cadenas

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]
cadenas.reduce(0, {(i: Int, c: String) -> Int in c.count + i })
// devuelve 18
```

<!--
Fuente: Acumular la longitud de las cadenas. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Acumular la longitud de las cadenas (continuación)

```swift
cadenas.reduce(0) {$1.count + $0}
```

`$0` es el total parcial. `$1` es la cadena actual. El resultado es `18`.

<!--
Fuente: Acumular la longitud de las cadenas. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## El orden del plegado

```swift
let cadenas = ["Patatas", "Arroz", "Huevos"]
cadenas.reduce("", +)
// devuelve "PatatasArrozHuevos"
```

La combinación recorre los elementos de izquierda a derecha y conserva ese orden al concatenarlos.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 861. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Componer filtrado y transformación

```swift
let numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.filter{$0 % 2 == 0}.map{$0*$0}
// Devuelve el array [4,16,36,64,100]
```

Primero conservamos los pares. Después elevamos cada uno al cuadrado.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 879. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Componer filtrado y plegado

```swift
let numeros = [103, 2, 330, 42, 532, 6, 125]
numeros.filter{$0 >= 100}.reduce(0,+)
// Devuelve 1090
```

La condición selecciona valores mayores o iguales que `100`. El plegado suma los seleccionados.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 887. Notas de clase de la semana 9.
La prosa de las notas dice mayores de 100, pero el código incluye el 100. Se describe el código exacto.
-->

---

<!-- _class: section topic-opening -->

<div class="mascot-figure section-mascot wizard"><img src="imagenes/mascota-lpp-creando.png" alt="Personaje LPP con una varita y una lambda."></div>
<div class="eyebrow">Semana 9</div>

# Genéricos

<p class="lead">Generalizar el tipo de dato sin duplicar el algoritmo.</p>

---

<!-- _class: lesson-code -->

## La misma operación con tipos distintos

```swift
func intercambia(_ tupla: (Int, String)) -> (String, Int) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}
let tupla = (10, "Hola")
intercambia(tupla)
// devuelve ("Hola", 10)
```

<!--
Fuente: La misma operación con tipos distintos. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## La misma operación con tipos distintos (continuación)

```swift
func intercambia(_ tupla: (Int, Int)) -> (Int, Int) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}
let tupla2 = (10, 20)
intercambia(tupla2)
// devuelve (20, 10)
```

El cuerpo intercambia los componentes. Solo cambian los tipos de entrada y salida.

<!--
Fuente: La misma operación con tipos distintos. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Función genérica `intercambia`

```swift
func intercambia<A,B>(_ tupla: (A, B)) -> (B, A) {
   let tuplaNueva = (tupla.1, tupla.0)
   return tuplaNueva
}
```

`A` y `B` son parámetros de tipo. El compilador los determina a partir de cada llamada.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 940. Notas de clase de la semana 9.

-->

---

<!-- _class: lesson-code -->

## Inferencia de los parámetros de tipo

```swift
let tupla = (10, "Hola")
intercambia(tupla)
// devuelve ("Hola", 10)
let tupla2 = (10, 20)
intercambia(tupla2)
// devuelve (20, 10)
let tupla3 = (true, 10.5)
intercambia(tupla3)
// devuelve (10.5, true)
```

Cada llamada concreta los tipos sin cambiar la definición de la función.

<!--
Fuente: ejemplo del bloque de código que comienza en la línea 955. Notas de clase de la semana 9.
Se corrige el resultado de intercambia((10,20)): (20,10).
-->

---

<!-- _class: lesson-code -->

## Una lista recursiva genérica

```swift
indirect enum Lista<T> {
     case vacia
     case nodo(T, Lista<T>)
}
```

`T` es el tipo de los elementos. El resto mantiene el mismo tipo `Lista<T>`.

<!--
Fuente: Lista genérica. Notas de clase de la semana 9.
Ejemplo final: lista genérica.
-->

---

<!-- _class: lesson-code -->

## Selector `first`

```swift
func first<T>(_ lista: Lista<T>) -> T? {
   switch lista {
      case let .nodo(primero, _):
         return primero
      case .vacia:
         return nil
   }
}
```

El resultado es opcional porque la lista vacía no tiene primer elemento.

<!--
Fuente: Lista genérica: first. Notas de clase de la semana 9.
No usar desenvoltura forzosa sin garantizar que la lista es no vacía.
-->

---

<!-- _class: lesson-code -->

## Selector `rest`

```swift
func rest<T>(_ lista: Lista<T>) -> Lista<T>? {
   switch lista {
      case let .nodo(_, resto):
         return resto
      case .vacia:
         return nil
   }
}
```

Una lista no vacía tiene un resto, que puede ser la lista vacía.

<!--
Fuente: Lista genérica: rest. Notas de clase de la semana 9.
Distinguir nil de una Lista.vacia devuelta como valor del opcional.
-->

---

<!-- _class: lesson-code -->

## Predicado y ejemplos

```swift
func vacia<T>(_ lista: Lista<T>) -> Bool {
   switch lista {
      case .vacia:
         return true
      default:
         return false
   }
}
let lista : Lista = .nodo(20, .nodo(30, .nodo(40, .vacia)))
let lista2 : Lista = .nodo("A", .nodo("B", .nodo("C", .vacia)))
print(first(rest(lista)!)!) // Imprime 30
print(first(rest(lista2)!)!) // Imprime "B"
```

<!--
Fuente: Lista genérica: vacia y ejemplos. Notas de clase de la semana 9.
Relacionar los elementos enteros y las cadenas con la inferencia de T. Las desenvolturas del ejemplo son válidas para estas listas no vacías.
-->
