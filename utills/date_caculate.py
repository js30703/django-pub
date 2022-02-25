from datetime import datetime


def get_previous_month_first(date):
    year = date.year
    month = date.month
    if month == 1:
        return datetime(year=year-1, month=12, day=1)
    else:
        return datetime(year=year, month=month-1, day=1)


def get_this_month_first(date):
    year = date.year
    month = date.month
    return datetime(year=year, month=month, day=1)
