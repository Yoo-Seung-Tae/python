import datetime

today=datetime.date.today()

print('지금까지 며칠이 지났는가')
first_day=datetime.date(2024,11,25)
passed_time=today-first_day
print(passed_time)