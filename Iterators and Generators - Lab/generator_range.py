def genrange(start_number, end_number):

    while start_number <= end_number:
        yield start_number
        start_number += 1


print(list(genrange(1, 10)))