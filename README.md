# python_package

## Features

- **Modern packaging** – PEP 517/518/621 ``pyproject.toml`` using Hatchling.
- **Editable installs** – ``pip install -e .[dev,docs]`` for iterative notebook
  development.
- **Documentation-first** – Sphinx configured with MyST-NB and a notebooks
  gallery ready for Read the Docs or local builds.
- **Testing** – Pytest suite to validate core functionality.

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev,docs]
```

Run the example notebook by launching Jupyter Lab and opening
``docs/notebooks/getting_started.md``.  Build the documentation locally with:

```bash
sphinx-build -b html docs docs/_build/html
```

Execute the tests:

```bash
pytest
```

## License

This project is licensed under the terms of the MIT license.  See
[LICENSE](LICENSE).
# writing_test
