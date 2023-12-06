import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        condition = True
        for ch in args:
            if isinstance(ch, float) or isinstance(ch, int):
                if ch % 2 != 0:
                    condition = False
            else:
                condition = False
        if condition:
            return func(*args)
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))