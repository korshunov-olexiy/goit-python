from datetime import datetime


def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    cur_date = datetime.now().date()
    delta = cur_date-date
    return delta.days


print(get_days_from_today('2021-10-09'))
