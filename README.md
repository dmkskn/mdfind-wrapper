# `mdfind`

A python library that wraps the **mdfind**.

- No dependencies except ones that in the python standart library
- Mypy checked ✨
- Fully tested

## Installation

```bash
$ pip install mdfind-wrapper
```

## Usage

```python
import mdfind # not mdfind-wrapper


QUERY = "kind:image"

images = mdfind.query(QUERY)
n_imgs = mdfind.count(QUERY)
```