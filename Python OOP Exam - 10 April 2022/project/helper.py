# ValueError if empty string
def value_error_if_value_is_empty_string(value, message):
    if value == '':
        raise ValueError(message)


# ValueError if less than zero/negative number
def value_error_if_value_is_negative_number(value, message):
    if value < 0:
        raise ValueError(message)


# ValueError if number is less than other number
def value_error_if_number_is_less_than_other_number(value, number_checker, message):
    if value < number_checker:
        raise ValueError(message)


# ValueError if number is bigger than other number
def value_error_if_number_is_bigger_than_other_number(value, number_checker, message):
    if value > number_checker:
        raise ValueError(message)
