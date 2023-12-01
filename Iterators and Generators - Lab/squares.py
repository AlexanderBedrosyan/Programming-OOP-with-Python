def squares(n):
    number = 1

    while number <= n:
        yield number ** 2
        number += 1


print(list(squares(5)))