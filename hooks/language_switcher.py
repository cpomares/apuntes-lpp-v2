"""Keep the Material language switcher on stable language homepages."""

import re

SPANISH_HOME = "https://cpomares.github.io/apuntes-lpp-v2/index.html"
ENGLISH_HOME = "https://cpomares.github.io/apuntes-lpp-v2/en/index.html"


def on_post_page(output, page, config):
    # The i18n plugin guesses equivalent pages from paths. Our English tree uses
    # translated folder names, so the stable switcher target is each language home.
    output = re.sub(r'href="[^"]*" hreflang="es"', f'href="{SPANISH_HOME}" hreflang="es"', output)
    output = re.sub(r'href="[^"]*" hreflang="en"', f'href="{ENGLISH_HOME}" hreflang="en"', output)
    return output
