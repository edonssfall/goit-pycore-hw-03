from datetime import date, timedelta, datetime

from hws import get_days_from_today, get_numbers_ticket, normalize_phone, get_upcoming_birthdays

if __name__ == '__main__':
    # HW-01
    print(get_days_from_today('2026-10-15'))
    print(get_days_from_today('2026-10-20'))
    print(get_days_from_today('2020-13-45'))
    print(get_days_from_today('2026-02-30'))

    # HW-02
    text = 'Ваші лотерейні числа: %s'
    print(text % get_numbers_ticket(1, 10, 10))
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

    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    print(get_upcoming_birthdays(users, today=datetime.strptime('2024.01.22', '%Y.%m.%d').date()))

    # HW-04: перевірки (сьогодні, ДР, очікувана дата привітання або None)
    checks = [
        # приклад з ТЗ
        (date(2024, 1, 22), "1985.01.23", "2024.01.23"),  # пн, ДР у вт
        (date(2024, 1, 22), "1990.01.27", "2024.01.29"),  # пн, ДР у сб -> пн
        (date(2024, 1, 22), "1991.01.29", None),  # пн, ДР рівно через тиждень — поза вікном
        # субота в кінці вікна, коли сьогодні неділя
        (date(2024, 1, 7), "1990.01.13", "2024.01.15"),
        # перехід між роками вперед
        (date(2025, 12, 29), "1990.01.03", "2026.01.05"),  # пн, ДР у сб нового року
        (date(2022, 12, 27), "1990.12.31", "2023.01.02"),  # вт, ДР у сб старого року -> пн нового
        # минулі вихідні -> сьогодні понеділок
        (date(2024, 1, 15), "1990.01.13", "2024.01.15"),  # пн, ДР був у сб
        (date(2024, 1, 15), "1990.01.14", "2024.01.15"),  # пн, ДР був у нд
        (date(2024, 1, 16), "1990.01.14", None),  # вт, ДР був у нд — понеділок уже минув
        # минулі вихідні через Новий рік
        (date(2024, 1, 1), "1990.12.31", "2024.01.01"),  # пн, ДР був у нд 31.12
        (date(2024, 1, 1), "1990.12.30", "2024.01.01"),  # пн, ДР був у сб 30.12
    ]
    for day, birthday, expected in checks:
        res = get_upcoming_birthdays([{"name": "x", "birthday": birthday}], today=day)
        got = res[0]["congratulation_date"] if res else None
        mark = '✅' if got == expected else '❌'
        print(f'{mark} сьогодні {day} ({day.strftime("%a")}), ДР {birthday[5:]}: {got} (очікується {expected})')
