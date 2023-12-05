import functools


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        result = function()
        vowels = ["a", "e", "o", "u", "i", "y"]
        new_list = []
        for ch in result:
            if ch.lower() in vowels:
                new_list.append(ch)
        return new_list
        pass

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
