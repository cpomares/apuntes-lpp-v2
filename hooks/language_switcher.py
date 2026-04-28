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
