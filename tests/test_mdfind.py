from unittest.mock import Mock, call, patch

import mdfind

NUL = "\x00"
PATHS_STDOUT = f"/foo{NUL}/bar"
COUNT_STDOUT = "0"

MDFIND_MOCK_WITH_PATHS = Mock(returncode=0, stdout=PATHS_STDOUT)
MDFIND_MOCK_WITH_COUNT = Mock(returncode=0, stdout=COUNT_STDOUT)


@patch("subprocess.run")
def test_mdfind(run):
    cmd = ["mdfind", "kind:image", "-onlyin", "~"]
    mdfind._api._mdfind(*cmd[1:])
    assert run.call_args == call(cmd, capture_output=True, text=True, check=True)


@patch("mdfind._api._mdfind")
def test_query_calls_mdfind_correct(_mdfind):
    mdfind.query("kind:image", onlyin="~")
    assert _mdfind.call_args == call("kind:image", "-onlyin", "~")
    mdfind.query("kind:image")
    assert _mdfind.call_args == call("kind:image")


@patch("mdfind._api._mdfind", return_value=MDFIND_MOCK_WITH_PATHS)
def test_query_return_splitted_list(_mdfind):
    result = mdfind.query("kind:image", onlyin="~")
    assert result == PATHS_STDOUT.split(NUL)


@patch("mdfind._api._mdfind")
def test_count_calls_mdfind_correct(_mdfind):
    mdfind.count("kind:image", onlyin="~")
    assert _mdfind.call_args == call("-count", "kind:image", "-onlyin", "~")
    mdfind.count("kind:image")
    assert _mdfind.call_args == call("-count", "kind:image")


@patch("mdfind._api._mdfind", return_value=MDFIND_MOCK_WITH_COUNT)
def test_query_return_splitted_list(_mdfind):
    result = mdfind.count("kind:image", onlyin="~")
    assert result == int(COUNT_STDOUT)


@patch("mdfind._api._mdfind")
def test_name_calls_mdfind_correct(_mdfind):
    mdfind.name("foo")
    assert _mdfind.call_args == call("-name", "foo",)
    mdfind.name("foo", onlyin="~")
    assert _mdfind.call_args == call("-name", "foo", "-onlyin", "~")


@patch("mdfind._api._mdfind", return_value=MDFIND_MOCK_WITH_PATHS)
def test_name_return_splitted_list(_mdfind):
    result = mdfind.name("foo", onlyin="~")
    assert result == PATHS_STDOUT.split(NUL)
