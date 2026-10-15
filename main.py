from datetime import date, timedelta

from hws import get_days_from_today, get_numbers_ticket, normalize_phone, get_upcoming_birthdays

if __name__ == '__main__':
    # HW-01
    print(get_days_from_today('2026-10-15'))
    print(get_days_from_today('2026-10-20'))
    print(get_days_from_today('2020-13-45'))
    print(get_days_from_today('2026-02-30'))

    # HW-02
    text = 'Ваші лотерейні числа: %s'
    print(text % get_numbers_ticket(5, 5, 1))
    print(text % get_numbers_ticket(1, 10, 10))
    print(text % get_numbers_ticket(1, 49, 6))
    print(text % get_numbers_ticket(1, 10, 20))
    print(text % get_numbers_ticket(1, 49, 0))
    print(text % get_numbers_ticket(1, 49, -3))

    # HW-03
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
        "38012^+"
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print('Нормалізовані номери телефонів для SMS-розсилки:', sanitized_numbers)

    # HW-04
    users = [
        {"name": "fas", "birthday": date.today().strftime('%Y.%m.%d')},
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    bdays = get_upcoming_birthdays(users)
    print('Список привітань на цьому тижні: %s' % bdays if bdays else 'No birthdays this week')

    # HW-04
    today = date.today()
    relative_users = []
    for k in range(-1, 9):
        day = today + timedelta(days=k)
        relative_users.append({
            "name": f"{k:+d} {day.strftime('%a')}",
            "birthday": day.replace(year=1992).strftime('%Y.%m.%d'),
        })
    print(f'Сьогодні {today} ({today.strftime("%a")})')
    for item in get_upcoming_birthdays(relative_users):
        print(f'  {item["name"]:8} -> {item["congratulation_date"]}')

