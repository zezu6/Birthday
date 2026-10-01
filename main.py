from datetime import date, datetime


def birthday_in_year(birthday: date, year: int) -> date:
    try:
        return birthday.replace(year=year)
    except ValueError: # 29/02 in a non-leap year
        return date(year, 3, 1)


def ask_birthday(today: date) -> date:
    while True:
        response = input("Enter your birthday (dd/mm/yyyy): ").strip()
        try:
            birthday = datetime.strptime(response, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date, use the format dd/mm/yyyy")
            continue
        if birthday > today:
            print("Are you a person from the future?")
            continue
        return birthday
    raise AssertionError("unreachable") # unreachable; keeps type checker silent


def main() -> None:
    now = date.today()
    bd = ask_birthday(now)

    next_bd = birthday_in_year(bd, now.year)
    if next_bd < now:
        next_bd = birthday_in_year(bd, now.year + 1)

    delta = (next_bd - now).days
    if delta == 0:
        print("Happy birthday!")
    else:
        print(f"Your birthday is in {delta} day{'s' if delta != 1 else ''}.\n"
              f"You'll be {next_bd.year - bd.year} years old.")


if __name__ == "__main__":
    main()
