from unittest.mock import Mock, call, patch

import pytest

import mdfind


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="one\ntwo"))
def test_query(run):
    result = mdfind.query("kind:image")
    cmd = ["mdfind", "kind:image"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == ["one", "two"]


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="one\ntwo"))
def test_query_onlyin(run):
    result = mdfind.query("kind:image", onlyin="/Users")
    cmd = ["mdfind", "kind:image", "-onlyin", "/Users"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == ["one", "two"]


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="0"))
def test_count(run):
    result = mdfind.count("kind:image")
    cmd = ["mdfind", "-count", "kind:image"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == 0


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="0"))
def test_count_onlyin(run):
    result = mdfind.count("kind:image", onlyin="/Users")
    cmd = ["mdfind", "-count", "kind:image", "-onlyin", "/Users"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == 0


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="one\ntwo"))
def test_name(run):
    result = mdfind.name("foo")
    cmd = ["mdfind", "-name", "foo"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == ["one", "two"]


@patch("subprocess.run", return_value=Mock(returncode=0, stdout="one\ntwo"))
def test_name_onlyin(run):
    result = mdfind.name("foo", onlyin="/Users")
    cmd = ["mdfind", "-name", "foo", "-onlyin", "/Users"]
    assert run.call_args == call(cmd, capture_output=True, text=True)
    assert result == ["one", "two"]


@patch("subprocess.run", return_value=Mock(returncode=1, stderr="Failed"))
def test_query_raises_an_error(run):
    with pytest.raises(ValueError) as excinfo:
        mdfind.query("foo")
        assert excinfo.value == "Failed"


@patch("subprocess.run", return_value=Mock(returncode=1, stderr="Failed"))
def test_count_raises_an_error(run):
    with pytest.raises(ValueError) as excinfo:
        mdfind.count("foor")
        assert excinfo.value == "Failed"


@patch("subprocess.run", return_value=Mock(returncode=1, stderr="Failed"))
def test_name_raises_an_error(run):
    with pytest.raises(ValueError) as excinfo:
        mdfind.name("foo")
        assert excinfo.value == "Failed"
