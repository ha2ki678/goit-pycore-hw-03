from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    birthdays_list = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_date = birthday.replace(year=today.year)

        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_left = (birthday_date - today).days

        if 0 <= days_left <= 7:
            if birthday_date.weekday() == 5:
                birthday_date = birthday_date + timedelta(days=2)
            elif birthday_date.weekday() == 6:
                birthday_date = birthday_date + timedelta(days=1)

            birthdays_list.append({
                "name": user["name"],
                "congratulation_date": birthday_date.strftime("%Y.%m.%d")
            })

    return birthdays_list

users = [
    {"name": "Mykola Varenyk", "birthday": "1984.04.29"},
    {"name": "Ivan Bondarenko", "birthday": "1991.01.26"},
    {"name": "Maria Melnyk", "birthday": "1994.01.18"},
    {"name": "Stepan Kylish", "birthday": "1989.04.30"}
]

result = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", result)