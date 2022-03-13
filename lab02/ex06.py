import datetime

today = datetime.datetime.today()
endOftheYearDate = datetime.datetime(today.year + 1, 1, 1)
endOfTheYearTime = datetime.datetime(today.year + 1, 1, 1, 0, 0, 0)
print("Days till end of the year: ", (endOftheYearDate - today).days)
print("Till end of the year: ", endOfTheYearTime - today)
