from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        difference = today - given_date
        return difference.days

    except ValueError:
        return "Неправильний формат дати. Використовуйте формат РРРР-ММ-ДД."

user_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")
result = get_days_from_today(user_date)
print(result)