from datetime import datetime, timedelta

from share import parse_value


def get_upcoming_birthdays(users: list[dict[str, str]], today = datetime.today().date(), days: int = 7) -> list[dict[str, str]]:
    """
    Birthdays in the next `days` days; weekend ones move to Monday,
    on Monday the past weekend ones are congratulated too.
    :param users: [{"name": <name>, "birthday": <YYYY.MM.DD>}, ...]
    :param today: date to count from (default: date of import)
    :param days: window length, today included
    :return: [{"name": <name>, "congratulation_date": <YYYY.MM.DD>}, ...]
    """
    res = list()

    for user in users:
        try:
            if user.get('birthday') and user.get('name'):

                birthday = datetime.strptime(
                    parse_value(user['birthday'], str, 'birthday'),
                    '%Y.%m.%d').date()

                for year in (today.year - 1, today.year, today.year + 1):
                    try:
                        birthday_year = birthday.replace(year=year)
                    except Exception:
                        birthday_year = birthday.replace(year=year, month=3, day=1)

                    in_window = birthday_year >= today and 0 <= (birthday_year - today).days < days

                    past_weekend = today.weekday() == 0 and -2 <= (birthday_year - today).days < 0

                    if in_window or past_weekend:
                        bday = birthday_year + timedelta(
                            days=7 - birthday_year.weekday()) if birthday_year.weekday() >= 5 else birthday_year
                        res.append({
                            'name': parse_value(user['name'], str, 'name'),
                            'congratulation_date': bday.strftime('%Y.%m.%d'),
                        })
        except Exception as e:
            print(f'Error get_upcoming_birthdays: {e}')
    return res
