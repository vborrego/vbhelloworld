#!/bin/sh
rm dist/*
ls dist/
python3 setup.py sdist bdist_wheel
ls dist/
twine upload --repository-url https://test.pypi.org/legacy/ dist/*