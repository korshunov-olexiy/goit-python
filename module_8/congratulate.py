from datetime import datetime, timedelta


def congratulate(file_name):
    """Displays a list of birthday people who need to be congratulated this week.

    Args:
        file_name ([str]): The name of the file where names and birthdays are stored.
    """
    WEEKDAYS_NAMES = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    weekdays_data = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    # current date
    cur_date = datetime.today()
    # monday of the current week
    base_date = cur_date - timedelta(days=cur_date.weekday())
    weekdays_list = [(base_date + timedelta(days=x)).strftime("%d.%m") for x in range(-2, 7)]
    weekdays_list = [weekdays_list[:3]]+weekdays_list[3:]
    with open(file_name, 'r', encoding='utf-8') as file_users:
        for line in file_users:
            # Get the birthdayman name and date
            name, birth = line.strip().split("\t")
            birth = datetime.strptime(birth[:5], "%d.%m").strftime("%d.%m")
            for idx, days in enumerate(weekdays_list):
                if birth in days:
                    weekdays_data[idx].append(name)
    for idx, day in weekdays_data.items():
        print(f"{WEEKDAYS_NAMES[idx]:<9}: {', '.join(day)}")


if __name__ == "__main__":
    congratulate('users.txt')
