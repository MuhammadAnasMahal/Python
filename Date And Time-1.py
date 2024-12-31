from datetime import date, time,datetime

today = datetime.today()
now = datetime.now()
print("The today's date is", today)
print("The current time is", now)
print("The date components", today.year,today.month,today.day)