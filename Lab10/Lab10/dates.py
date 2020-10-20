"""
Date Handling
"""
import datetime
import sys
from typing import Tuple

def name_of_weekday(date: datetime.date) -> str:
    """What is the name of the weekday?

    No work needed.  But, notice that:
    1. date.weekday() returns an index 0 through 6.
    2. we use that index to get a name.
    """
    weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return weekday_names[date.weekday()]

#--------------------------------------------------------------
# IMPLEMENT THE FUNCTIONS BELOW THIS LINE

def text_to_ymd(text: str) -> Tuple[int,int,int]:
    """
    Convert text into a year, month, day
      ISO: YYYY-MM-DD
      USA: MM/DD/YY
    """
    # 1. if the text contains "-":
    # 2.   split the text on "-":
    #        s_year, s_month, s_day = text.split("-")
    # 3. if the text contains "/":
    # 4.   split it on "/"
    #        s_month, s_day, s_year = text.split("/")
    # 5. Convert all three values into ints
    # 6. Return the three values: year, month, day
    if "-" in text:
        year,month,day = text.split("-")
    elif "/" in text:
        month,day,year = text.split("/")
    return (int(year),int(month),int(day))

def new_years_day(year: int) -> datetime.date :
    """
    What day of the week was the given year's January 1st?
    """

    # 1. Get today's date:
    #      today = datetime.date.today()
    # 2. get the year: today.year
    # 3. Make and return new date object:
    #      return datetime.date(y, m, d) (pick y, m, d appropriately)
    today = datetime.date.today()
    currentYear = today.year
    return datetime.date(currentYear,1,1)

def n_weeks_after_newyears(year: int, n_weeks: int) -> datetime.date:
    """What day was n_weeks weeks after new year's day?
    """

    # 1. Call new_years_day() to get the first date of the year.
    # 2. Call datetime.timedelta( X ), which is an interval.
    #    X is the number of days. (remember 7 days per week).
    # 3. Add that to the first date, and return
    newYearsDay = new_years_day(year)
    dt = datetime.timedelta(7*n_weeks)
    return newYearsDay + dt

def first_thursday(year: int, month: int) -> datetime.date:
    """What was the first Thursday of the given month of the year?
    """

    # 1. make a date = datetime.date(year, month, 1) for first day of month.
    # 2. Loop:
    #      while True:
    # 3. inside loop, check if date.weekday() == 3
    #      if so, it's Thursday.  break.
    # 4. otherwise, add one day:
    #      date += datetime.timedelta(1)
    # when done, return date

    date = datetime.date(year,month,1)
    while True:
        if date.weekday() == 3:
            break
        else:
            date += datetime.timedelta(1)
    return date

def thanksgiving_thursday(year: int) -> datetime.date:
    """What day is the third Friday of November, of the year?
    """
    # 1. Get first Thursday of November (call first_thursday(11))
    # 2. add 14 days to it, and return

    firstThursNov = first_thursday(year,11)
    thanksgiving = firstThursNov + datetime.timedelta(14)
    return thanksgiving

def days_until_thanksgiving(today: datetime.date, year: int) -> int:
    """How many days from today until thanksgiving?
    """
    # 1. Call thanksgiving_thursday
    # 2. Subtract today's date:
    #  delta = thanksgiving_thursday() - today
    # 3. return delta.days
    thanksgiving = thanksgiving_thursday(year)
    dt = thanksgiving - today
    return dt.days

def election_day(year: int) -> datetime.date:
    """When is election day, on the given year?
    It's the first Tuesday AFTER the first Monday of November.
    """
    electionDay = datetime.date(year,11,1)
    while True:
        if electionDay.weekday() == 0:   # is monday
            break
        else:
            electionDay += datetime.timedelta(1)
    electionDay += datetime.timedelta(1)    # add one more day (tues)
    return electionDay 
    
def is_leap_year(year: int) -> bool:
    """Is the given year a leap year?
    """

    """
    Rules (proleptic Gregorian calendar):
    1. If the year is not divisible by 4, it's NOT a leap year.
       return False
    2. if the year IS divisible by 400, it's NOT a leap year.
    3. otherwise, it's a leap year.
    """
    if year % 4 != 0:      
        return False
    elif year % 400 == 0:
        return False
    else:
        return True


# IMPLEMENT THE FUNCTIONS ABOVE THIS LINE
#-------------------------------------------------------------

def main():
    the_year: int = 2020
    today: datetime.date = datetime.date(the_year, 1, 31)
    if len(sys.argv) == 2:
        the_year, month, day = text_to_ymd(sys.argv[1])
        today = datetime.date(the_year, month, day)

    for text_date in ["2008-09-01", "2015-08-23", "09/01/2008", "8/23/2015"]:
        year, month, day = text_to_ymd(text_date)
        date = datetime.date(year, month, day)
        print("{:<22} : {}".format(text_date, date))
    print("New Year's Day          ", new_years_day(the_year))
    print("New Year's was a        ", name_of_weekday(new_years_day(the_year)))
    print("10 weeks later is a     ",
          name_of_weekday(n_weeks_after_newyears(the_year, 10)))
    print("First Thursday of Sept: ", first_thursday(the_year, 9))
    print("Thanksgiving:           ", thanksgiving_thursday(the_year))
    print("Days until thanksgiving:", days_until_thanksgiving(today, the_year))
    election = election_day(2016)
    print("Election day 2016:      ", election)
    print("Election day was a      ", name_of_weekday(election))

    for decade in range(1980, 2020, 10):
        for year in range(decade, decade + 10):
            print("{:>4} ".format(year), end = "")
        print()
        for year in range(decade, decade + 10):
            if is_leap_year(year):
                print("{:>4} ".format("Leap"), end = "")
            else:
                print("{:>4} ".format(""), end = "")
        print()

if __name__ == '__main__':
    main()

