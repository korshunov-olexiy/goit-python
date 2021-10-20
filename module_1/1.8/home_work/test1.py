#import datetime
from datetime import date, timedelta, datetime

print(datetime.strptime("2021-10-01", "%Y-%m-%d").date())


def next_week(dt, idx=0):
    '''Get a list of the days of the next week.

    Key arguments:
    dt - Start date, data type: datetime.date
    '''
    fmt = "%d.%m.%Y"
    days_ahead = idx - dt.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    print(timedelta(days_ahead).days)
    nx_wkday = dt + timedelta(days_ahead)
    # We get a list of dates from Mon to Sun.
    if idx < 6:
        return [nx_wkday.strftime(fmt)] + next_week(dt, idx+1)
    else:
        return [nx_wkday.strftime(fmt)]


d = date(2021, 10, 13)
print(next_week(d))

wks = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
            3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
wk_brth = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
print(wks[d.weekday()])

#users = [{"name": "Бобриєвич Микола Сергійович", "birthday": datetime.strptime("01.03.1975","%d.%m.%Y").date()},

#print(type(users[0]['birthday']))
print([r for r in range(d.weekday(),7)])
print(date.today().strftime('%d.%m.%Y').weekday())

users = []
with open('users.txt', 'r', encoding='utf-8') as file_users:
    for line in file_users:
        name, birth = line.strip().split("\t")
        users.append({'name': name, 'birthday': datetime.strptime(birth, "%d.%m.%Y").date()})

print(users[0])
