def number_increment(current_numbers):

    def increase(current_numb=list):
        new_list = [ch + 1 for ch in current_numbers]
        return new_list

    return increase()


print(number_increment([1, 2, 3]))