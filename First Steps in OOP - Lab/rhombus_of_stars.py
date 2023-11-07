def construct_the_figure(num):
    for i in range(0, num):
        result = ['*' for _ in range(i + 1)]
        print(' ' * (num - 1 - i) + ' '.join(result) + ' ' * (num - 1 - i))

    for i in range(num - 1, - 1, - 1):
        result = ['*' for _ in range(i)]
        print(' ' * (num - i) + ' '.join(result) + ' ' * (num - i))


num = int(input())
construct_the_figure(num)