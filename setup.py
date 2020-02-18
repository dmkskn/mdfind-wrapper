from pathlib import Path

from setuptools import setup

BASE = Path(__file__).parent


def get_long_description() -> str:
    with open(BASE / "README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="mdfind-wrapper",
    license="Unlicense",
    version="0.1.3",
    url="https://github.com/dmkskn/mdfind-wrapper",
    author="Dima Koskin",
    author_email="dmksknn@gmail.com",
    description="A python library that wraps the mdfind.",
    keywords=["macos", "mdfind", "spotlight"],
    python_requires=">=3.6",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=["mdfind"],
    package_data={"mdfind": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: MacOS",
    ],
)
