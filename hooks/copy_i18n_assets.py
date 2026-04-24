from pathlib import Path
from shutil import copytree


def on_post_build(config, **kwargs):
    """Mirror shared MkDocs assets into the English site subtree.

    With use_directory_urls disabled, mkdocs-static-i18n generates English
    pages under site/en, and Material's relative asset links point to
    site/en/assets. The shared assets are emitted at site/assets, so we mirror
    them after each build.
    """
    site_dir = Path(config["site_dir"])
    english_dir = site_dir / "en"

    for folder_name in ("assets", "imagenes"):
        source = site_dir / folder_name
        target = english_dir / folder_name
        if source.exists():
            copytree(source, target, dirs_exist_ok=True)
