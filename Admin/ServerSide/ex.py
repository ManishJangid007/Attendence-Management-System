from datetime import date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(date.today().year-1, 6, 1)
end_date = date.today()
for single_date in daterange(start_date, end_date):
    day = single_date.strftime("%Y-%m-%d")
    print(day)