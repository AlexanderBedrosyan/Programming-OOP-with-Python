class Calculator:

    @staticmethod
    def add(*args):
        sum = 0
        for ch in args:
            sum += ch
        return sum

    @staticmethod
    def multiply(*args):
        sum = 1
        for ch in args:
            sum *= ch
        return sum

    @staticmethod
    def divide(*args):
        sum = args[0]
        for ch in args[1:]:
            if ch != 0:
                sum /= ch
        return sum

    @staticmethod
    def subtract(*args):
        sum = args[0]
        for ch in args[1:]:
            sum -= ch
        return sum
