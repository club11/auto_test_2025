"""task 10"""


def decorator_func(*args, **kwargs):
    """
    decorator
    """
    def wrapper(a_func):
        def wrapped_func(*func_args, **func_kwargs):
            return (args, kwargs), a_func(*func_args, **func_kwargs)
        return wrapped_func
    return wrapper


@decorator_func(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(num):
    """
    return a num
    """
    return num


print(identity(42))
