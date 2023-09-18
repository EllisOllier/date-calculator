import datetime

# Functions 

def dateEntry():
    firstDateEntry = input("Enter a date in the format YYYY-MM-DD: ")
    year,month,day = map(int, firstDateEntry.split('-'))
    firstDate = datetime.date(year, month, day)

    secondDateEntry = input("Enter another date in the format YYYY-MM-DD: ")
    year,month,day = map(int, secondDateEntry.split('-'))
    secondDate = datetime.date(year, month, day)

    timeBetweenDates(firstDate, secondDate)

def timeBetweenDates(date1, date2):
    if date1 > date2:
        timeBetween = date1 - date2
    else:
        timeBetween = date2 - date1
    print(timeBetween)
    

# Startup functions

dateEntry()