from datetime import datetime, timedelta


WEEKDAYS_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def congratulate(file_name):
    """Displays a list of birthday people who need to be congratulated this week.

    Args:
        file_name ([str]): The name of the file where names and birthdays are stored.
    """
    global WEEKDAYS_NAMES
    weekdays_data = [[], [], [], [], [], [], []]
    # current date
    current_date = datetime.today()
    # monday of the current week
    base_date = current_date - timedelta(days=current_date.weekday())
    weekdays_list = [(base_date + timedelta(days=x)).strftime("%d.%m") for x in range(-2, 7)]
    days_list = [weekdays_list[:3]]+weekdays_list[3:]
    with open(file_name, 'r', encoding='utf-8') as file_users:
        for line in file_users:
            # Get the birthdayman name and date
            name, birth = line.strip().split("\t")
            birth = datetime.strptime(birth[:5], "%d.%m").strftime("%d.%m")
            for idx in range(len(days_list)):
                if birth in days_list[idx]:
                    weekdays_data[idx].append(name)
    for idx in range(len(weekdays_data)):
        print(f"{WEEKDAYS_NAMES[idx]:<9}: {', '.join(weekdays_data[idx])}")


if __name__ == "__main__":
    congratulate('users.txt')
