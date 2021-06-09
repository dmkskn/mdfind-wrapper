"""An `mdfind` wrapper"""
import subprocess as sp
from typing import List, Optional, Union, Iterator

__all__ = ["query", "count", "name"]

NUL = "\x00"

_Kwarg = Optional[Union[str, bool]]


def _mdfind(*args: str) -> sp.CompletedProcess:
    return sp.run(["mdfind", *args], capture_output=True, text=True, check=True)


def _iter_args(*args: str, **kwargs: _Kwarg) -> Iterator[str]:
    """Returns args and kwargs as a flat list of strings. Filters a kwarg
    if its value is None. Fliters a kwarg if its value is False. Adds
    a hyphen to the kwarg key (if it doesn't have one)."""
    yield from args
    for key, value in kwargs.items():
        if value is None or value is False:
            continue
        yield key if key.startswith("-") else f"-{key}"
        if isinstance(value, str):
            yield value


def query(query: str, onlyin: Optional[str] = None, **kwargs: _Kwarg) -> List[str]:
    """Get a list of files that match the given metadata query."""
    output = _mdfind(*_iter_args("-0", query, onlyin=onlyin, **kwargs))
    return output.stdout.strip(NUL).split(NUL)


def count(query: str, onlyin: Optional[str] = None, **kwargs: _Kwarg) -> int:
    """Get the total number of matches."""
    output = _mdfind(*_iter_args("-count", query, onlyin=onlyin, **kwargs))
    return int(output.stdout)


def name(query: str, onlyin: Optional[str] = None, **kwargs: _Kwarg) -> List[str]:
    """Get a list of files that match the given name."""
    output = _mdfind(*_iter_args("-0", "-name", query, onlyin=onlyin, **kwargs))
    return output.stdout.strip(NUL).split(NUL)
