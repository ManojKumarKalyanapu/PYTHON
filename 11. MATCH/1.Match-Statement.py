# The Python Match Statement
month = 5
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4 | 10 |12 if month == 5: # combine values
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _: # default value
    print("Looking forward to the Weekend")