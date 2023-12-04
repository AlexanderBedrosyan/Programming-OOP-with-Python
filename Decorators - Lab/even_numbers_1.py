import functools


def even_numbers(function):
    @functools.wraps(function)
    def wrapper(numbers):
        result = []
        for ch in numbers:
            if ch % 2 == 0:
                result.append(ch)
        return result
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))

