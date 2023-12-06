from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        start = timer()
        func(*args)
        end = timer()
        return (start - end)
    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
         
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
