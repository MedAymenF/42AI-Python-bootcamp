#!/bin/sh
mkdir -p ./ai42/logging
mv progressbar.py ai42/
mv log.py ai42/logging
touch ai42/__init__.py
echo "from .progressbar import progressbar" > ai42/__init__.py
touch ai42/logging/__init__.py
echo "from .log import log" > ai42/logging/__init__.py
python setup.py sdist bdist_wheel
