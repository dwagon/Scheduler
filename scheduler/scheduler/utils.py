import datetime


###############################################################################
def thisMonth(year=None, month=None):
    today = datetime.date.today()
    if year is None:
        year = today.year
    else:
        year = int(year)
    if month is None:
        month = today.month
    else:
        month = int(month)
    return year, month


###############################################################################
def nextMonth(year, month):
    month += 1
    if month == 13:
        month = 1
        year += 1
    return year, month


###############################################################################
def prevMonth(year, month):
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    return year, month

# EOF
