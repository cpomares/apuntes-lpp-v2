"""Keep the Material language switcher on translated counterparts when available."""

import re

SITE_URL = "https://cpomares.github.io/apuntes-lpp-v2/"
SPANISH_HOME = "index.html"
ENGLISH_HOME = "en/index.html"

# Only map pages whose English counterpart has real translated content.
SPANISH_TO_ENGLISH = {
    SPANISH_HOME: ENGLISH_HOME,
    "teoria/tema00-descripcion-asignatura/tema00-descripcion-asignatura.html": "en/theory/topic00-course-description/topic00-course-description.html",
    "teoria/tema01-historia-lenguajes-programacion/tema01-historia-lenguajes-programacion.html": "en/theory/topic01-history-programming-languages/topic01-history-programming-languages.html",
    "teoria/tema02-programacion-funcional/tema02-programacion-funcional.html": "en/theory/topic02-functional-programming/topic02-functional-programming.html",
    "teoria/tema03-procedimientos-recursivos/tema03-procedimientos-recursivos.html": "en/theory/topic03-recursive-procedures/topic03-recursive-procedures.html",
    "teoria/tema04-estructuras-recursivas/tema04-estructuras-recursivas.html": "en/theory/topic04-recursive-structures/topic04-recursive-structures.html",
    "teoria/tema05-programacion-funcional-swift/tema05-programacion-funcional-swift.html": "en/theory/topic05-functional-programming-swift/topic05-functional-programming-swift.html",
    "teoria/tema06-programacion-orientada-objetos-swift/tema06-programacion-orientada-objetos-swift.html": "en/theory/topic06-object-oriented-programming-swift/topic06-object-oriented-programming-swift.html",
    "practicas/practica01/practica01.html": "en/labs/lab01-practice/lab01-practice.html",
    "practicas/practica02/practica02.html": "en/labs/lab02-practice/lab02-practice.html",
    "practicas/practica03/practica03.html": "en/labs/lab03-practice/lab03-practice.html",
    "practicas/practica04/practica04.html": "en/labs/lab04-practice/lab04-practice.html",
    "practicas/practica05/practica05.html": "en/labs/lab05-practice/lab05-practice.html",
    "practicas/practica06/practica06.html": "en/labs/lab06-practice/lab06-practice.html",
    "practicas/practica07/practica07.html": "en/labs/lab07-practice/lab07-practice.html",
    "practicas/practica08/practica08.html": "en/labs/lab08-practice/lab08-practice.html",
    "practicas/practica09/practica09.html": "en/labs/lab09-practice/lab09-practice.html",
    "practicas/practica10/practica10.html": "en/labs/lab10-practice/lab10-practice.html",
    "practicas/practica11/practica11.html": "en/labs/lab11-practice/lab11-practice.html",
    "practicas/practica12/practica12.html": "en/labs/lab12-practice/lab12-practice.html",
    "seminarios/seminario1-scheme/seminario1-scheme.html": "en/seminars/seminar01-scheme/seminar01-scheme.html",
    "seminarios/seminario2-swift/seminario2-swift.html": "en/seminars/seminar02-swift/seminar02-swift.html",
}

ENGLISH_TO_SPANISH = {english: spanish for spanish, english in SPANISH_TO_ENGLISH.items()}


def absolute_url(path):
    return f"{SITE_URL}{path}"


def language_targets(page_url):
    normalized_url = page_url or SPANISH_HOME
    is_english_page = normalized_url.startswith("en/")

    if is_english_page:
        spanish_target = ENGLISH_TO_SPANISH.get(normalized_url, SPANISH_HOME)
        english_target = normalized_url
    else:
        spanish_target = normalized_url
        english_target = SPANISH_TO_ENGLISH.get(normalized_url, ENGLISH_HOME)

    return {
        "es": absolute_url(spanish_target),
        "en": absolute_url(english_target),
    }


def on_post_page(output, page, config):
    targets = language_targets(page.url)
    output = re.sub(
        r'href="[^"]*" hreflang="es"',
        f'href="{targets["es"]}" hreflang="es"',
        output,
    )
    output = re.sub(
        r'href="[^"]*" hreflang="en"',
        f'href="{targets["en"]}" hreflang="en"',
        output,
    )
    return output
