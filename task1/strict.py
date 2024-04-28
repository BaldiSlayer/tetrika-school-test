import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        signature_arguments = inspect.signature(func).parameters.values()
        for arg_name, arg_value in zip(signature_arguments, args):
            if not isinstance(arg_value, arg_name.annotation):
                raise TypeError(f'Argument {arg_name.name} must be of type {arg_name.annotation}')

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1.0, 2.4))  # >>> TypeError
