def reverse_text(word):
    index = 1

    while index <= len(word):
        yield word[-index]
        index += 1


for char in reverse_text("step"):
    print(char, end='')
