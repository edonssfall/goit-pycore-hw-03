import datetime
import random
import re


def get_days_from_today(date):
    return (datetime.datetime.today() - datetime.datetime.strptime(date, '%Y-%m-%d')).days


def get_numbers_ticket(min, max, quantity):
    res = [random.randint(min, max) for _ in range(quantity)]
    res.sort()
    return res


def normalize_phone(number):
    number = re.sub(r'[^0-9+]', '', number)
    l_number = len(number)
    if number.startswith('0') and l_number == 10:
        number = '+380' + number
    elif number.startswith('380') and l_number == 12:
        number = '+' + number
    return number

def get_upcoming_birthdays(users):
    return [{
        'name': user['name'],
        'congratulation_date': user['birthday']
         } for user in users
        if datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').replace(year=2000) > datetime.datetime.today().replace(year=2000)]



if __name__ == '__main__':
    print(get_days_from_today('2020-10-09'))

    print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))

    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
