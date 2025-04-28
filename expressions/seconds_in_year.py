"""Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute"""

days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_each_minute = 60

def main():

    print("There are " + str(days_per_year * hours_per_day * minutes_per_hour * seconds_each_minute) + " in a day")

if __name__ == '__main__':
    main()