from utils import dicts


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs",) == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcc",) == "git"
    assert dicts.get_val({"vcs": "mercurial"}, "vcc", "bazaar") == "bazaar"
