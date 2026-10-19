# Transparencias de LPP en castellano

Las semanas 1 a 11 se han rehecho tomando como fuente principal las notas de
clase de cada semana en `notas-clase/semanaXX/semanaXX.md`. Se utiliza el diseño
de la semana 1: fondo claro, mostaza y grafito, Avenir Next y personaje LPP.
El nombre de la autora aparece en pequeño solo en la portada de cada semana.
Las portadas incluyen las marcas oficiales de la UA y del DCCIA y el
personaje LPP. Los separadores interiores utilizan también el personaje,
sin la antigua marca λ en un cuadrado grafito.

[Vista previa de la portada](vistas-previas/portada-semana01.png) ·
[Vista previa del separador](vistas-previas/separador-semana01.png).

| Semana | Contenido | Diapositivas | Presentación | Markdown |
| --- | --- | --- | --- | --- |
| 1 | Presentación y fundamentos de programación funcional | 39 | [Abrir](semana01/semana01.html) | [Editar](semana01/semana01.md) |
| 2 | Recursión, parejas y listas | 39 | [Abrir](semana02/semana02.html) | [Editar](semana02/semana02.md) |
| 3 | Construcción de listas, lambda y apply | 39 | [Abrir](semana03/semana03.html) | [Editar](semana03/semana03.md) |
| 4 | Clausuras y funciones de orden superior | 46 | [Abrir](semana04/semana04.html) | [Editar](semana04/semana04.md) |
| 5 | Procesos recursivos e iterativos y figuras recursivas | 48 | [Abrir](semana05/semana05.html) | [Editar](semana05/semana05.md) |
| 6 | Listas estructuradas | 36 | [Abrir](semana06/semana06.html) | [Editar](semana06/semana06.md) |
| 7 | Árboles y árboles binarios | 39 | [Abrir](semana07/semana07.html) | [Editar](semana07/semana07.md) |
| 8 | Programación funcional con Swift y datos recursivos | 59 | [Abrir](semana08/semana08.html) | [Editar](semana08/semana08.md) |
| 9 | Opcionales, clausuras y genéricos | 57 | [Abrir](semana09/semana09.html) | [Editar](semana09/semana09.md) |
| 10 | Clases, estructuras, propiedades y herencia | 66 | [Abrir](semana10/semana10.html) | [Editar](semana10/semana10.md) |
| 11 | Protocolos, casting, genéricos y extensiones | 69 | [Abrir](semana11/semana11.html) | [Editar](semana11/semana11.md) |

El personaje conserva las letras, las proporciones y los colores. Sus brazos,
postura y mirada varían según el mensaje: varita y lambda en portadas y al explicar la creación de funciones, señalamiento
en aclaraciones, reflexión en conceptos y un signo de interrogación al
plantear preguntas. Las semanas 1 a 3 ya alternan estas variantes.

Los pies de página indican el tema y la parte correspondiente. La numeración
de temas sigue los apuntes publicados: Swift funcional es el tema 5 y
orientación a objetos con Swift es el tema 6.

Las presentaciones no incluyen transparencias de repaso final.

Cada carpeta contiene también una guía docente con la correspondencia entre
las diapositivas y las notas de clase. Las preguntas, respuestas y apoyos de
explicación están en los comentarios de la fuente Marp.

Las [correcciones y precisiones de la revisión](revision.md) recogen las
erratas detectadas al preparar los ejemplos. Los originales españoles y la
versión inglesa se conservan. Las notas disponibles terminan en la semana 11.

## Generación del HTML

Con Marp CLI instalado, desde la raíz del repositorio:

```bash
marp transparencias/es/semana02/semana02.md \
  --theme transparencias/es/tema-lpp-claro.css \
  --html \
  --output transparencias/es/semana02/semana02.html
```

Las carpetas se llaman `semana01` a `semana11`, y sus archivos principales
son `semanaXX.md` y `semanaXX.html`. El HTML debe conservar su carpeta `imagenes` al
copiarlo o compartirlo. Estas presentaciones son archivos independientes de
MkDocs y no se han publicado.
