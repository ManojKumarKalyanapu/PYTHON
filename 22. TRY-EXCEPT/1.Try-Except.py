'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
# Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
# Finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# You can define what kind of error to raise, and the text to print to the user.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")