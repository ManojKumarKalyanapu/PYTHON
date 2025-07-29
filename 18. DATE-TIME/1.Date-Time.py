# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()
print(x)

# Date Output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

from datetime import datetime

now = datetime.now()

print("Current DateTime:", now)
print("Weekday, short version (%a):", now.strftime("%a"))
print("Weekday, full version (%A):", now.strftime("%A"))
print("Weekday as a number 0-6, Sunday=0 (%w):", now.strftime("%w"))
print("Day of month 01-31 (%d):", now.strftime("%d"))
print("Month name, short version (%b):", now.strftime("%b"))
print("Month name, full version (%B):", now.strftime("%B"))
print("Month as a number 01-12 (%m):", now.strftime("%m"))
print("Year, short version, no century (%y):", now.strftime("%y"))
print("Year, full version (%Y):", now.strftime("%Y"))
print("Hour 00-23 (%H):", now.strftime("%H"))
print("Hour 00-12 (%I):", now.strftime("%I"))
print("AM/PM (%p):", now.strftime("%p"))
print("Minute 00-59 (%M):", now.strftime("%M"))
print("Second 00-59 (%S):", now.strftime("%S"))
print("Microsecond 000000-999999 (%f):", now.strftime("%f"))
print("UTC offset (%z):", now.strftime("%z"))   # Usually empty unless aware datetime
print("Timezone (%Z):", now.strftime("%Z"))     # Usually empty unless aware datetime
print("Day number of year 001-366 (%j):", now.strftime("%j"))
print("Week number of year, Sunday first day, 00-53 (%U):", now.strftime("%U"))
print("Week number of year, Monday first day, 00-53 (%W):", now.strftime("%W"))
print("Local version of date and time (%c):", now.strftime("%c"))
print("Century (%C):", now.strftime("%C"))
print("Local version of date (%x):", now.strftime("%x"))
print("Local version of time (%X):", now.strftime("%X"))
print("A % character (%%):", now.strftime("%%"))
print("ISO 8601 year (%G):", now.strftime("%G"))
print("ISO 8601 weekday (1-7) (%u):", now.strftime("%u"))
print("ISO 8601 week number (01-53) (%V):", now.strftime("%V"))
