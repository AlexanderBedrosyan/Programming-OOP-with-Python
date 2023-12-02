def get_primes(current_list):
    def check_if_number_is_prime(num):

        if num <= 1:
            return False
        if num == 2:
            return True

        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for el in current_list:
        if check_if_number_is_prime(el):
            yield el


