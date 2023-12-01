def read_next(*args):
    for item in args:
        for i in item:
            yield i


