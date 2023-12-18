def value_error_if_value_is_empty_string(value, message):
    """
    :param value: the parameter which we have to check if it's an empty string
    :param message: ValueError message which will raise if the value is empty string
    :return: None or ValueError
    """
    if value == '':
        raise ValueError(message)


def value_error_if_value_is_negative_number(value, message):
    """
    :param value: the parameter which we have to check if it's less than 0
    :param message: ValueError message which will raise if the value is less than zero
    :return: None or ValueError
    """
    if value < 0:
        raise ValueError(message)


def value_error_if_number_is_less_than_other_number(value, number_checker, message):
    """
    :param value: the parameter which we have to check if it's less than number_checker
    :param number_checker: range number which we use for checking
    :param message: ValueError message which will raise if the value is less than number_checker
    :return: None or ValueError
    """
    if value < number_checker:
        raise ValueError(message)


def value_error_if_number_is_bigger_than_other_number(value, number_checker, message):
    """
    :param value: the parameter which we have to check if it's bigger than number_checker
    :param number_checker: range number which we use for checking
    :param message: ValueError message which will raise if the value is bigger than number_checker
    :return: None or ValueError
    """
    if value > number_checker:
        raise ValueError(message)


def value_error_if_number_is_equal_to_other_number(value, number_checker, message):
    """
    :param value: the parameter which we have to check if it's equal to number_checker
    :param number_checker: range number which we use for checking
    :param message: ValueError message which will raise if the value is equal to number_checker
    :return: None or ValueError
    """
    if value == number_checker:
        raise ValueError(message)


def value_error_if_value_contains_only_white_spaces(value, message):
    """
    :param value: The parameter which we have to check if it's only white spaces
    :param message: ValueError message which will raise if the value is only with white spaces
    :return: None or ValueError
    """
    if value.isspace():
        raise ValueError(message)


def value_error_if_string_is_not_only_with_letters_and_digits(value, message):
    """
    :param value: The parameter which we have to check if it's not only letters and digits
    :param message: ValueError message which will raise if the value is not only letters and digits
    :return: None or ValueError
    """
    if not value.isalnum():
        raise ValueError(message)


def find_object(item: str or int, attribute: str, collection: list):
    """
    :param item: parameter that we are looking for
    :param attribute: parameter name in the object (self.model - attribute is 'model')
    :param collection: list of objects
    :return: None or obj
    """
    for obj in collection:
        if getattr(obj, attribute) == item:
            return obj