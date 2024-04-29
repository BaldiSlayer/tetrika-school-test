import inspect
from functools import wraps
from mismatched_error import ParameterMismatchError


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # getting parameters from the function signature
        signature_arguments = inspect.signature(func).parameters

        if len(args) + len(kwargs) != len(signature_arguments):
            raise ParameterMismatchError('The number of parameters does not match')

        # checking args types matching
        for arg_name, arg_value in zip(signature_arguments.values(), args):
            if not isinstance(arg_value, arg_name.annotation):
                raise TypeError(f'Argument {arg_name.name} must be of type {arg_name.annotation}')

        # checking kwargs types matching
        for arg_name, arg_value in kwargs.items():
            if arg_name not in signature_arguments:
                raise TypeError(f'Argument {arg_name} it is not parameter of a {func.__name__} function')
            if not isinstance(arg_value, signature_arguments[arg_name].annotation):
                raise TypeError(f'Argument {arg_name} must be of type {signature_arguments[arg_name].annotation}')

        result = func(*args, **kwargs)

        # checking the type of the returned value
        return_type = func.__annotations__.get('return')
        if return_type and not isinstance(result, return_type):
            raise TypeError(f'Type of result is {type(result)} and not {return_type}')

        return result

    return wrapper
