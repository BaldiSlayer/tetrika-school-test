import inspect


def strict(func):
    def wrapper(*args, **kwargs):
        signature_arguments = inspect.signature(func).parameters
        for arg_name, arg_value in zip(signature_arguments.values(), args):
            if not isinstance(arg_value, arg_name.annotation):
                raise TypeError(f'Argument {arg_name.name} must be of type {arg_name.annotation}')

        for arg_name, arg_value in kwargs.items():
            if not isinstance(arg_value, signature_arguments[arg_name].annotation):
                raise TypeError(f'Argument {arg_name} must be of type {signature_arguments[arg_name].annotation}')

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

