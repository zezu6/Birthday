from datetime import datetime


def isleap(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


today = datetime.now().date()
while True:
    response = input("Enter your birthday (dd.mm.yyyy): ")
    try:
        birthday = datetime.strptime(response, "%d.%m.%Y")
        break
    except ValueError:
        print("dumbass")

td_days = today.timetuple().tm_yday
bd_days = birthday.timetuple().tm_yday
days_left = bd_days - td_days

if days_left < 0:
    birthday.replace(year=birthday.year + 1)
    bd_days = birthday.timetuple().tm_yday

    days_left = 365 - td_days + bd_days
    if isleap(today.year):
        days_left = 366 - td_days + bd_days

print(days_left)
