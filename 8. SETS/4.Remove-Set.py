# Remove Item
thisset = {"apple", "banana", "cherry"}
# Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)


# Discard Item
# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# pop
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)