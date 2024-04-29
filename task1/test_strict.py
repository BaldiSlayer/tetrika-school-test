import pytest
from strict import strict


@strict
def add(a: int, b: int) -> int:
    return a + b


@strict
def concat(a: str, b: str) -> str:
    return a + b


def test_add_with_correct_types():
    assert add(3, 5) == 8


def test_add_with_incorrect_types():
    with pytest.raises(TypeError) as exc_info:
        add(3, '5')
    assert str(exc_info.value) == "Argument b must be of type <class 'int'>"


def test_concat_with_correct_types():
    assert concat('Hello, ', 'world!') == 'Hello, world!'


def test_concat_with_incorrect_types():
    with pytest.raises(TypeError) as exc_info:
        concat('Hello, ', 5)
    assert str(exc_info.value) == "Argument b must be of type <class 'str'>"


def test_add_with_correct_types_kwargs():
    assert add(a=3, b=5) == 8


def test_add_with_incorrect_types_kwargs():
    with pytest.raises(TypeError) as exc_info:
        add(b=3, a='5')
    assert str(exc_info.value) == "Argument a must be of type <class 'int'>"
