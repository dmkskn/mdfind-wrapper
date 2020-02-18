"""An `mdfind` wrapper"""
import subprocess
from typing import List, Optional

__all__ = ["query", "count", "name"]


def query(query: str, onlyin: Optional[str] = None) -> List[str]:
    """Get a list of files that match the given metadata query."""
    cmd = ["mdfind", query, *[_ for _ in ["-onlyin", onlyin] if onlyin]]
    output = subprocess.run(cmd, capture_output=True, text=True)
    if output.returncode == 0:
        return output.stdout.splitlines()
    else:
        raise ValueError(output.stdout)


def count(query: str, onlyin: Optional[str] = None) -> int:
    """Get the total number of matches."""
    cmd = ["mdfind", "-count", query, *[_ for _ in ["-onlyin", onlyin] if onlyin]]
    output = subprocess.run(cmd, capture_output=True, text=True)
    if output.returncode == 0:
        return int(output.stdout)
    else:
        raise ValueError(output.stdout)


def name(query: str, onlyin: Optional[str] = None) -> List[str]:
    """Get a list of files that match the given name."""
    cmd = ["mdfind", "-name", query, *[_ for _ in ["-onlyin", onlyin] if onlyin]]
    output = subprocess.run(cmd, capture_output=True, text=True)
    if output.returncode == 0:
        return output.stdout.splitlines()
    else:
        raise ValueError(output.stdout)
