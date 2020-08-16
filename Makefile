register:
	python setup.py register -r pypi

publish:
	python -m twine upload  dist/*

build:
	python setup.py sdist bdist_wheel
