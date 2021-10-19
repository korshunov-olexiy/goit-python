from datetime import datetime, timedelta


cur_date = datetime.now()
# begin of week
start = cur_date - timedelta(days=cur_date.weekday())
# end of week
end = cur_date + timedelta(days=6)

# for dt in range(start, end):
#     print(dt)

base = datetime.today().date()
date_list = [base + timedelta(days=x) for x in range(7)]
print(date_list)
