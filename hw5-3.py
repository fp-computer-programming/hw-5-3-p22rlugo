# Ryan Lugo: RJL 11/2/21

import calendar as cal

# Question 1
cal.TextCalendar().pryear(2020)

# Question 2
cal.setfirstweekday(cal.SUNDAY)
cal.prmonth(2020,1)

# Question 3
cal.TextCalendar().prmonth(2020,themonth=2)

# Question 4
print(cal.isleap(2022))
# It expects a year as an argument, it returns bool values if it is true or false of it being a leap year.