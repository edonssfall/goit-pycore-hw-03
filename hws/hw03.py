import re

from share import parse_value


def normalize_phone(number: str, country_code: str = '+38') -> str:
    """
    Normalize a phone number for SMS sending: keep only digits and a leading '+',
    add the international code if it is missing.
    :param number: phone number in any format, e.g. '(050) 123-45-67'
    :param country_code: code added to numbers without one (default '+38', Ukraine)
    :return: normalized number, e.g. '+380501234567'
    """
    try:
        number = parse_value(number, str, 'number')
        country_code = parse_value(country_code, str, 'country_code')

        number = re.sub(r'(?!^\+)[^0-9]', '', number)
        if number.startswith('+'):
            number = number
        elif number.startswith('0'):
            number = f'{country_code}{number}'
        elif number.startswith(f'{country_code[1:]}0'):
            number = f'+{number}'

        return number

    except Exception as e:
        print(f'Error normalize_phone: {e}')
