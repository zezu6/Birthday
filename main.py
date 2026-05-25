from datetime import date, datetime
from secrets import token_urlsafe


def isleap(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


today = date.today()
while True:
    response = input("Enter your birthday (dd/mm/yyyy): ")
    try:
        birthday = datetime.strptime(response, "%d/%m/%Y").date()
        break
    except ValueError:
        print("try again")

next_bd = birthday.replace(year=today.year)
delta = (next_bd - today).days


print(f"Your birthday is in {delta} days. You'll be {next_bd.year - birthday.year} years old.")
