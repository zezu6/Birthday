from datetime import date, datetime


def isleap(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


today = date.today()
while True:
    response = input("Enter your birthday (dd/mm/yyyy): ")
    try:
        birthday = datetime.strptime(response, "%d/%m/%Y").date()
        if birthday > today:
            print("Are you a person from the future?")
            continue
        break
    except ValueError:
        print("try again")

try: # exception happens when a person is born on 29/02
    next_bd = birthday.replace(year=today.year)
except ValueError:
    next_bd = birthday.replace(day=1, month=3, year=today.year)

if (next_bd - today).days < 0: # birthday is next year
    next_bd = next_bd.replace(year=today.year + 1)

    # person born on 29/02 AND next year is a leap year
    if birthday.day == 29 and birthday.month == 2 and isleap(today.year + 1):
        next_bd = next_bd.replace(day=29, month=2)
delta = (next_bd - today).days

if delta == 0:
    print("Happy birthday!")
else:
    print(f"Your birthday is in {delta} days. You'll be {next_bd.year - birthday.year} years old.")
