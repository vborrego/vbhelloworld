#!/bin/sh
rm dist/*
ls dist/
python3 setup.py sdist bdist_wheel
ls dist/
#twine upload --repository-url https://pypi.python.org/legacy/ dist/*
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
