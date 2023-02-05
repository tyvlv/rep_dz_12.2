import pytest
from utils import arrs


@pytest.fixture
def list_example():
    return [1, 2, 3]


def test_get(list_example):
    assert arrs.get(list_example, 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(list_example):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(list_example, 1) == [2, 3]
    assert arrs.my_slice([],) == []
    assert arrs.my_slice(list_example, -1) == [3]
    assert arrs.my_slice(list_example, -4) == [1, 2, 3]
