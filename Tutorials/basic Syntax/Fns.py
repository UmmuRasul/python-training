#number of the dats month . first value placeholder
month_days =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # doc string expl what suppose to be done
    """:return True for leap yaers and false for non-leap"""
    #here if the year is divisible by 4 ! by 100 and divided by 400
    #calculating a leap yr
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year,month):
    """:return number of days in that month year:"""

#check if month is 1-12
    if not 1 <= month <= 12:
        return  "Invalid Month"
    if month == 2 and is_leap(year):
        return 29 #if is 2month and aleap yr if both are true return 29

#return no. of month here
    return month_days[month]

print(is_leap(2019))


print(days_in_month(2019, 5))