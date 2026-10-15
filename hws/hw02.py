import random

from share import parse_value


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generate a lottery ticket: unique random numbers from the range [min, max].
    :param min: smallest possible number, at least 1
    :param max: largest possible number, at most 1000
    :param quantity: how many numbers to pick; at least 1 and no more than the range holds
    :return: sorted list of unique numbers;
             empty list if any parameter breaks the limits (the error is printed)
    """
    res = list()
    try:
        min = parse_value(min, int, 'min')
        max = parse_value(max, int, 'max')
        quantity = parse_value(quantity, int, 'quantity')
        if quantity < 1:
            raise Exception(f'{quantity} have not valid format')
        if min < 1:
            raise Exception(f'{min} must be 1 or more')
        if max > 1000:
            raise Exception(f'{max} > 1000')
        if min > max:
            raise Exception(f'{min} > {max}')
        if not min < quantity < max:
            raise Exception(f'quantity must be between min and max - {min} < {quantity} < {max}')
        if quantity - 1 > (max - min):
            raise Exception(f'{quantity} > {(max - min)} - not enough variants')

        while len(res) < quantity:
            value = random.randint(min, max)
            if value not in res:
                res.append(value)
        res.sort()
    except Exception as e:
        print(f'Error get_numbers_ticket: {e}')
        return res
    return res
