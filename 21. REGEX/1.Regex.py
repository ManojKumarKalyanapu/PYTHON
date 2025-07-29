# The findall() Function
import re

# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
# If no matches are found, the value None is returned:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# The split() Function
# The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt, 1)
print(x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", txt, 2)
print(x)


# The Match object has properties and methods used to retrieve information about the search, and the result:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # .span() returns a tuple containing the start-, and end positions of the match.
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # returns the string passed into the function
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # The regular expression looks for any words that starts with an upper case "S":
print(x.group())