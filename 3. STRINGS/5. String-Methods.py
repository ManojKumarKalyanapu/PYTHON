# 1.capitalize()
txt = "Converts the first character to upper case"
x = txt.capitalize()
print (x)

# 2.casefold()
txt = "This will convert ALL characters to lower case"
x = txt.casefold() 
print(x)

# 3.center()
txt = "This will be centered"
x = txt.center(50, '*') # taking up the space of 50 characters with given string
print(x)

# 4.count()
txt = "Returns the number of times a specified value occurs in a string"
x = txt.count("a")  # counting occurrences of 'a'
print(x)

# 5.encode()
txt = "Returns an encoded version of the string"
x = txt.encode()
print(x)

# 6.endswith()
txt = "Returns true if the string ends with the specified value"
x = txt.endswith("value")
print(x)

# 7.expandtabs()
txt = "Returns\ta\tstring where all tab characters are replaced with one or more spaces"
x = txt.expandtabs(4)  # replacing tabs with 4 spaces   
print(x)

# 8.find()
txt = "Searches the string for a specified value and returns the position of where it was found"
x = txt.find("specified")  # finding the position of 'specified'
print(x)

# 9.format()
txt = "The {} is a {}"
x = txt.format("Python", "programming language")  # formatting the string with values
print(x)

# 10.format_map()
txt = "The {language} is a {type}"
x = txt.format_map({"language": "Python", "type": "programming language"})
print(x)

# 11.index()
txt = "Searches the string for a specified value and returns the position of where it was found"
x = txt.index("specified")  # finding the position of 'specified'
print(x)

# 12.isalnum()
txt = "Returns True if all characters in the string are alphanumeric"
x = txt.isalnum()  # checking if all characters are alphanumeric
print(x)

# 13.isalpha()
txt = "Returns True if all characters in the string are alphabetic"
x = txt.isalpha()  # checking if all characters are alphabetic
print(x)

# 14.isascii()
txt = "Returns True if all characters in the string are ASCII"
x = txt.isascii()  # checking if all characters are ASCII
print(x)

# 15.isdecimal()
txt = "Returns True if all characters in the string are decimal characters"
x = txt.isdecimal()  # checking if all characters are decimal
print(x)

# 16.isdigit()
txt = "Returns True if all characters in the string are digits"
x = txt.isdigit()  # checking if all characters are digits
print(x)

# 17.isidentifier()
txt = "Returns True if the string is a valid identifier"
x = txt.isidentifier()  # checking if the string is a valid identifier
print(x)

# 18.islower()
txt = "Returns True if all characters in the string are lowercase"
x = txt.islower()  # checking if all characters are lowercase
print(x)

# 19.isnumeric()
txt = "Returns True if all characters in the string are numeric"
x = txt.isnumeric()  # checking if all characters are numeric
print(x)

# 20.isprintable()
txt = "Returns True if all characters in the string are printable"
x = txt.isprintable()  # checking if all characters are printable
print(x)

# 21.isspace()
txt = "Returns True if all characters in the string are whitespace"
x = txt.isspace()  # checking if all characters are whitespace
print(x)

# 22.istitle()
txt = "Returns True if the string follows the rules of a title"
x = txt.istitle()  # checking if the string is a title
print(x)

# 23.isupper()
txt = "Returns True if all characters in the string are uppercase"
x = txt.isupper()  # checking if all characters are uppercase
print(x)

# 24.join()
txt = "This will join the elements of a sequence into a single string"
seq = ("Join", "these", "words")
x = txt.join(seq)  # joining the sequence with the string
print(x)

# 25.ljust()
txt = "This will left justify the string"
x = txt.ljust(50, '*')  # left justifying the string to
# a width of 50 characters with given string
print(x)

# 26.lower()
txt = "This will convert all characters to lower case"
x = txt.lower()  # converting to lower case
print(x)

# 27.lstrip()
txt = "This will remove any leading characters (space is the default)"
x = txt.lstrip()  # removing leading spaces
print(x)

# 28.maketrans()
txt = "This will create a translation table"
x = txt.maketrans("aeiou", "12345")  # creating a translation table
print(x)

# 29.partition()
txt = "This will split the string into three parts"
x = txt.partition("split")  # splitting the string at 'split'
print(x)

# 30.replace()
txt = "This will replace a specified phrase with another specified phrase"
x = txt.replace("replace", "substitute")  # replacing 'replace' with 'substitute'
print(x)

# 31.rfind()
txt = "Searches the string for a specified value and returns the last position of where it was found"
x = txt.rfind("casa",5,29) # method returns -1 if the value is not found. 
print(x)

# 32.rindex()
txt = "Searches the string for a specified value and returns the last position of where it was found"
x = txt.rindex("e",5,20)
print(x)

# 33.rjust()
txt = "Returns a right justified version of the string"
x = txt.rjust(20,"r")
print(x)

# 34.rpartition()
txt = "Returns a tuple where the string is parted into three parts"
x = txt.rpartition("the")
print(x)

# 35.rsplit()
txt = "Splits the string at the specified separator, and returns a list"
x = txt.rsplit(", ",1) # value1:Specifies the separator to use when splitting the string # value2:Specifies how many splits to do. Default value is -1, 
print(x)

# 36.rstrip()
txt = "Returns a right trim version of the string              "
x = txt.rstrip()
print(x)
	
# 37.split()	
txt = "Splits the string at the specified separator, and returns a list"
x = txt.split(",") # default separator is any whitespace.
print(x)

# 38.splitlines()	
txt = "Splits the string at line\n breaks and returns a list"
x = txt.splitlines()
print(x)

# 39.startswith()	
txt = "Returns true if the string starts with the specified value"
x = txt.startswith("Re", 0, 20)
print(x)

# 40.strip()	
txt = "Returns a trimmed ....,,,,,,, version of the string"
x = txt.strip(",.")
print(x)

# 41.swapcase()	
txt = "Swaps cases, lower case becomes upper case and vice versa"
x = txt.swapcase()
print(x)

# 42.title()	
txt = "Converts the first character of each word to upper case"
x = txt.title()
print(x)

# 43.translate() Returns a translated string	
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# 44.maketrans()
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print("maketrans:",txt.translate(mytable))

# 45.upper()	
txt = "Converts a string into upper case"
x = txt.upper()
print(x)

# 46.zfill()	
txt = "Fills the string with a specified number of 0 values at the beginning"
x = txt.zfill(100)
print(x)