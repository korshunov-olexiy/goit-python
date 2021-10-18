from datetime import datetime, timedelta, date


WEEKDAYS_NAMES = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

def congratulate(file_name):
    """Displays a list of birthday people who need to be congratulated this week.

    Args:
        file_name ([str]): The name of the file where names and birthdays are stored.
    """
    weekdays_data = [[], [], [], [], [], [], []]
    weekdays = []
    global WEEKDAYS_NAMES
    # current date.
    cur_date = datetime.today()
    # List of days of the week from current date to Sunday (weekday = 6)
    week_days = range(datetime.today().weekday(), 7)
    for day in week_days:
        # Get and write the dates for this week, starting from the current date.
        week_date = cur_date + timedelta(days=day)
        week_date = week_date.strftime("%d.%m")
        weekdays.append(week_date)
    print(weekdays)
    with open(file_name, 'r', encoding='utf-8') as file_users:
        for line in file_users:
            # Get the name and date.
            name, birth = line.strip().split("\t")
            birth = datetime.strptime(birth[:5], "%d.%m")
            birth_weekday = birth.weekday()
            if birth.strftime("%d.%m") in weekdays:
                weekdays_data[birth_weekday].append(name)
    return weekdays_data


congratulate('users.txt')
