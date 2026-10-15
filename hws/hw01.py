import re
from datetime import datetime, date as d

from share import parse_value


def get_days_from_today(date: str) -> int | None:
    """
    Calculate the number of days from the given date to today (time of day is ignored).
    :param date: date string in format 'YYYY-MM-DD', e.g. '2020-10-09'
    :return: days from date to today: positive for a past date, negative for a future one;
             None if the date has an invalid format (the error is printed)
    """
    try:
        date = parse_value(date, str, 'date')
        if not re.fullmatch('^\\d{4}-\\d{2}-\\d{2}', date):
            raise Exception(f'{date} have not valid format')
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except Exception:
            raise Exception(f'{date} have not valid format')
        return (d.today() - date.date()).days
    except Exception as e:
        print(f'Error get_days_from_today: {e}')
