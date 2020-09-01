"""An `mdfind` wrapper"""
import subprocess as sp
from typing import List, Optional

__all__ = ["query", "count", "name"]

NUL = "\x00"


def _mdfind(*args: str) -> sp.CompletedProcess:
    return sp.run(["mdfind", *args], capture_output=True, text=True, check=True)


def query(query: str, onlyin: Optional[str] = None) -> List[str]:
    """Get a list of files that match the given metadata query."""
    output = _mdfind("-0", query, *iter(["-onlyin", onlyin] if onlyin else []))
    return output.stdout.split(NUL)


def count(query: str, onlyin: Optional[str] = None) -> int:
    """Get the total number of matches."""
    output = _mdfind("-count", query, *iter(["-onlyin", onlyin] if onlyin else []))
    return int(output.stdout)


def name(query: str, onlyin: Optional[str] = None) -> List[str]:
    """Get a list of files that match the given name."""
    output = _mdfind("-0", "-name", query, *iter(["-onlyin", onlyin] if onlyin else []))
    return output.stdout.split(NUL)
