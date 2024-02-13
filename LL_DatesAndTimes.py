# Linkedin Learning Challenge Dates and Times
# You're given a month and year, along with a day of the week (Monday through Sunday).
# Return the number of instances of that day in the given month

import calendar

def count_days(year, month, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(year, month)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

run = True
while run:
    try:
        print("Which day of the week would you like to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or exit to quit")

        theday = input("? ")
        if theday.lower() == "exit" or theday.lower() == "":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter a year: ")
        year = int(yearstr)

        monthstr = input("Enter a month: ")
        month = int(monthstr)

        result = count_days(year, month, day)

        print("There are " + str(result) + " instances of that day in the specified month and year")
        print("---------\n")
    except Exception as e:
        print(e)
        print("Sorry, that's an invalid entry.")
