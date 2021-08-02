# Poetry/Pytest Learning

[Poetry](https://python-poetry.org/) is a packaging and dependency management tool for Python. 
[Pytest](https://docs.pytest.org/en/6.2.x/) is a popular python unit-testing framework in the industry.

This repo was initialized with:
```bash
poetry new poetry-learning
```

This repo contains references to work with a `poetry` project, and begin writing unit tests using `pytest`.

## Install Poetry

See here: https://python-poetry.org/docs/master/#installation

for latest instructions to install `poetry` on your machine.

## Useful comands

[Activate virtuanlenv](https://python-poetry.org/docs/cli/#shell):
```bash
poetry shell
```

[Installs deps (from `poetry.lock` if present)](https://python-poetry.org/docs/cli/#install):
```bash
poetry install
```

[Add a dependency](https://python-poetry.org/docs/cli/#add):
```bash
poetry add requests
```

Add a dev dependency
```bash
poetry add pytest-watch --dev
```

[Run tests](https://python-poetry.org/docs/basic-usage/#using-poetry-run)
```bash
poetry run pytest
```

Watch tests:
```bash
poetry run pytest-watch
```

Format code in current directory:
```bash
poetry run black .
```

## Writing tests

`pytest` will pick up all files prefixed with "test_" to run any tests it contains.

Pytest treats any method prefixed with `test*` as a unittest to run. 

By convention, we prefix methods with `test_<method>__<description>` for readability in this repo. For a method
```python
def add(x, y):
    return x + y
```
a unit test would look like:
```python
def test_sub__3_and_2_equals_1():
    # Given
    a = 3
    b = 2

    # When
    actual = sub(a, b)

    # Then
    expected = 1
    assert actual == expected
```

See `tests/test_examples.py` for example unit tests.





