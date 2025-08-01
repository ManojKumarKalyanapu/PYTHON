
# INT
x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# setting specific data type
x = int(20)


# FLOAT
x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# setting specific data type
x = float(20.5)

# COMPLEX
x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# setting specific data type
x = complex(1j)


# Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random

print(random.randrange(1, 10))
