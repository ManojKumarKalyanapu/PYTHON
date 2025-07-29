# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.


import myModule
# import myModule as mx ; Re-naming a Module
myModule.greeting('Manoj')


# Variables in Module
a = myModule.person1['age']
print(a)


# Build in Module
# There are several built-in modules in Python,
import platform

x = platform.system()
print(x)


# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)