import functools


def multiply(times):
    @functools.wraps(times)
    def decorator(function):
        def wrapper(number):
            return times * function(number)
        return wrapper

    return decorator

@multiply(3)
def add_ten(number):
    return number + 10
print(add_ten(3))
