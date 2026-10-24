"""Rebuild the GitHub Pages /docs directory after editing data or assets."""
from pathlib import Path
import shutil
import build

build.build()
root = Path(__file__).resolve().parent
shutil.copytree(root / 'dist', root / 'docs', dirs_exist_ok=True)
print('Updated docs/. Commit and push to publish with GitHub Pages.')
