from datetime import datetime, timedelta, date as d

from share import parse_value


def get_upcoming_birthdays(users: list[dict[str, str]], days: int = 7) -> list[dict[str, str]]:
    """
    Find users whose birthday falls within the next `days` days, today included.
    A birthday on Saturday or Sunday is congratulated on the following Monday.
    A 29 February birthday is treated as 1 March in non-leap years.
    Users without name or birthday are skipped; a user with a bad date is reported and skipped.
    :param users: [{"name": <name>, "birthday": <YYYY.MM.DD>}, ...]
    :param days: window length in days, today included (default 7)
    :return: [{"name": <name>, "congratulation_date": <YYYY.MM.DD>}, ...]
    """
    res = list()

    for user in users:
        try:
            if user.get('birthday') and user.get('name'):

                birthday = datetime.strptime(
                    parse_value(user['birthday'], str, 'birthday'),
                    '%Y.%m.%d').date()
                today = d.today()
                for year in (today.year - 1, today.year, today.year + 1):
                    try:
                        birthday_year = birthday.replace(year=year)
                    except Exception:
                        birthday_year = birthday.replace(year=year, month=3, day=1)

                    if birthday_year >= today and 0 <= (birthday_year - today).days < days:
                        bday = birthday_year + timedelta(
                            days=7 - birthday_year.weekday()) if birthday_year.weekday() >= 5 else birthday_year
                        res.append({
                            'name': parse_value(user['name'], str, 'name'),
                            'congratulation_date': bday.strftime('%Y.%m.%d'),
                        })
        except Exception as e:
            print(f'Error get_upcoming_birthdays: {e}')
    return res
