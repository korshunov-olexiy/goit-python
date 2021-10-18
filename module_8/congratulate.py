from datetime import datetime, timedelta, date


WEEKDAYS = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

# print(users[0])
# .strftime('%d.%m.%Y')
# print(date.today().weekday())

def congratulate(file_name):
    """Displays a list of birthday people who need to be congratulated this week.

    Args:
        file_name ([str]): The name of the file where names and birthdays are stored.
    """
    # current date without year.
    cur_date = datetime.today().strftime('%d.%m.')
    # List of days of the week from current date to Sunday (weekday = 6)
    week_dates = range(datetime.today().weekday, 7)
    # list with users dict
    users = []
    with open(file_name, 'r', encoding='utf-8') as file_users:
        for line in file_users:
            name, birth = line.strip().split("\t")
            users.append({'name': name, 'birthday': datetime.strptime(birth, "%d.%m.%Y").date()})

wk_brth = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

# congratulate('users.txt')
