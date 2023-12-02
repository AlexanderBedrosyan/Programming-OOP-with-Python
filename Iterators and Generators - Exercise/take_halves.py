from sys import maxsize


def solution():

    def integers():
        for i in range(1, maxsize):
            yield i

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]


    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
