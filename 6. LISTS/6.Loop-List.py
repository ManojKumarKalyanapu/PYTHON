# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# The Syntax
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)