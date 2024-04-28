import pytest

from typing import Any, Callable
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


# def test_strict_decorator_with_no_annotations():
#    @strict
#    def no_annotations(a: Any, b: Any) -> Any:
#        return a + b

#    assert no_annotations(3, 5) == 8
#    assert no_annotations('Hello, ', 'world!') == 'Hello, world!'
