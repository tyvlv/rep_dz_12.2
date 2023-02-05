import pytest
from utils import dicts


@pytest.fixture
def dictionary():
    return {"vcs": "mercurial"}


def test_get_val(dictionary):
    assert dicts.get_val(dictionary, "vcs",) == "mercurial"
    assert dicts.get_val(dictionary, "vcc",) == "git"
    assert dicts.get_val(dictionary, "vcc", "bazaar") == "bazaar"
