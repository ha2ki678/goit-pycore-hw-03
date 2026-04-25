import datetime

def get_days_from_today(date_string):
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    except:
        return 0

    current_date = datetime.date.today()

    difference = current_date - parsed_date
    return difference.days