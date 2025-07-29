# Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

# Continue Statement
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# range() function
for x in range(6): # starting from 0 by default, and increments by 1
  print('range: ',x) # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
  
# range form and to
for x in range(2, 6):
  print('range from to: ',x)
  
# range from and to and increment number
for x in range(2, 30, 3):
  print(x)
  
# Else in For Loop
# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  print('else: ',x)
else:
  print("Finally finished!")
  
# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
for x in [0, 1, 2]:
  pass