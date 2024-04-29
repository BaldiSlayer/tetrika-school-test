import pytest
from strict import strict
from mismatched_error import ParameterMismatchError


@strict
def add(a: int, b: int) -> int:
    return a + b


@strict
def concat(a: str, b: str) -> str:
    return a + b


@strict
def equal(a: bool, b: bool) -> bool:
    return a == b


@strict
def add_float(a: float, b: float) -> float:
    return a + b


@strict
def variadic(*args: int):
    return sum(args)


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


def test_equal_with_correct_types_args():
    assert equal(True, True)


def test_equal_with_incorrect_types_args():
    with pytest.raises(TypeError) as exc_info:
        equal(1, True)
    assert str(exc_info.value) == "Argument a must be of type <class 'bool'>"


def test_add_float_with_correct_types():
    assert add_float(3.0, 5.0) == 8.0


def test_add_float_with_incorrect_types_int():
    with pytest.raises(TypeError) as exc_info:
        add_float(3, '5')
    assert str(exc_info.value) == "Argument a must be of type <class 'float'>"


def test_add_float_with_incorrect_types_str():
    with pytest.raises(TypeError) as exc_info:
        add_float(3.0, '5')
    assert str(exc_info.value) == "Argument b must be of type <class 'float'>"


def test_non_existent_kwarg():
    with pytest.raises(TypeError) as exc_info:
        add_float(a=3.0, e='5')
    assert str(exc_info.value) == "Argument e it is not parameter of a add_float function"


def test_variadic():
    with pytest.raises(ParameterMismatchError) as exc_info:
        variadic(1, 2, 3)
    assert str(exc_info.value) == "The number of parameters does not match"


def test_none_type_return():
    variadic(1)
