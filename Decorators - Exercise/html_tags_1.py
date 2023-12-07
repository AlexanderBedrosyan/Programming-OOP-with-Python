def tags(symbol):
    def decorator(func):
        def wrapper(*args):
            return f"<{symbol}>{func(*args)}</{symbol}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
