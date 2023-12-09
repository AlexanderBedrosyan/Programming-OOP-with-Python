def type_check(current_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if type(*args) is current_type:
                return function(*args)
            else:
                return "Bad Type"

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
