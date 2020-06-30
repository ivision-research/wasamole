init:
	pip install -r requirements.txt

format:
	black wasamole tests bin/wasm-objdump

typecheck:
	mypy --strict wasamole/ bin/wasm-objdump

test:
	py.test tests

dist:
	python setup.py sdist bdist_wheel

.PHONY: init test
