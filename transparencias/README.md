# Transparencias de LPP

## Versión en castellano

Las semanas 1 a 11 están rehechas en castellano a partir de las notas de
clase de cada semana, con el diseño de la semana 1.

- [Índice de presentaciones y fuentes editables](es/indice.md)
- [Correcciones y precisiones de la revisión](es/revision.md)
- Tema de Marp: `es/tema-lpp-claro.css`

Los archivos definitivos se llaman `semanaXX.md` y `semanaXX.html`, sin el sufijo
`design`. Cada semana incluye una guía docente. Los ejemplos conservan los
nombres y la terminología de los apuntes en castellano. La versión inglesa
queda pendiente de adaptación a esta revisión.

## Semana 1: muestra de diseño en inglés

- Fuente editable: `en/week01/week01-design.md`
- Presentación en el navegador: `en/week01/week01-design.html`
- Tema de Marp: `en/theme-lpp-light.css` (nombre: `lpp-light`)
- Marca de la asignatura: λ y LPP en HTML/CSS, arriba a la derecha
- Función pura: `en/week01/images/pure-function-mustard-v2.png`
- Referencias a un objeto compartido: `en/week01/images/shared-object-mustard-v1.png`
- Evaluación de las ramas de `if`: `en/week01/images/if-branches-mustard-v1.png`

La muestra revisada tiene 38 diapositivas y está organizada para ensayar una
sesión de unas dos horas. La guía `en/week01/week01-teaching-guide.md` relaciona
los apartados con las notas originales, propone tiempos y recoge preguntas,
respuestas y apoyos para pizarra y editor.

Se han agrupado la introducción y las explicaciones repetidas, manteniendo
los ejemplos de código existentes. Se han ampliado la transparencia
referencial, la composición, las reglas de las formas especiales y la
diferencia entre listas como elementos y concatenación. La tipografía de
lectura es Avenir Next, con monoespaciada para el código.

La portada utiliza mostaza y grafito. Los separadores de tema llevan una
banda mostaza inferior. La marca λ LPP permanece arriba a la derecha.
Las fechas de exámenes no se han trasladado de cursos anteriores; la
planificación y la evaluación deben contrastarse con el curso nuevo.

Desde la raíz del repositorio, con Marp CLI instalado:

```bash
marp transparencias/en/week01/week01-design.md \
  --theme transparencias/en/theme-lpp-light.css \
  --html \
  --output transparencias/en/week01/week01-design.html
```

El HTML necesita conservar la ruta relativa al dibujo. La marca λ LPP es
tipografía editable y no depende de una imagen externa.
El tema `lpp` y los archivos `week01.md` / `week01.html` originales se mantienen
para comparar. Las demás semanas todavía utilizan el diseño anterior.

Los tres esquemas se generaron con la herramienta integrada de OpenAI en
grafito y mostaza sobre marfil. El de función pura muestra dos llamadas
idénticas a `square`, con entrada `4`, cuerpo `(* x x)` y salida `16`. El de
aliasing representa dos referencias a un único objeto. El de `if` distingue
la rama seleccionada de la rama que no se evalúa. Las descripciones de
generación se conservan en comentarios junto a cada imagen.

Referencia visual para el tratamiento editorial del contenido:
https://plusai.com/templates/editorial
El diseño y la implementación en Marp son propios.
