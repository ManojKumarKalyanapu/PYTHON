# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# example
list1 = [1, 2, 3, 4, 5]
list2 = list1  # list2 is just a reference to list1

# Modify list1
list1[0] = 100

print("list1:", list1)
print("list2:", list2)

# Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)