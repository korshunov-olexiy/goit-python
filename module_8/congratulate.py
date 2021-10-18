from datetime import datetime, timedelta, date


wks = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
wk_brth = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

users = []
with open('users.txt', 'r', encoding='utf-8') as file_users:
    for line in file_users:  #.read().splitlines():
        name, birth = line.strip().split("\t")
        users.append({'name': name, 'birthday': datetime.strptime(birth, "%d.%m.%Y").date()})

print(users[0])
# .strftime('%d.%m.%Y')
print(date.today().weekday())
