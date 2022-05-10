import datetime


def date(month, day, year):
    weekday = datetime.datetime(year, month, day)
    return weekday.strftime("%A")


print(date(int(input("month: ")), int(input("day: ")), int(input("year: "))))

