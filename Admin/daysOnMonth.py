def daysOfMonth(month, year):
    days = 0
    if month == 1:
        days = 31
    elif month == 2:
        if year%2 == 0:
            days = 29
        else:
            days = 28
    elif month == 3:
        days = 31
    elif month == 4:
        days = 30
    elif month == 5:
        days = 31
    elif month == 6:
        days = 30
    elif month == 7:
        days = 31
    elif month == 8:
        days = 31
    elif month == 9:
        days = 30
    elif month == 10:
        days = 31
    elif month == 11:
        days = 30
    elif month == 12:
        days = 31

    return days