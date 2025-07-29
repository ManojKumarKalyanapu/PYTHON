# Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print('min: ',x)
print('max: ',y)


# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print('abs: ',x)

# The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3)
print('power: ',x)


# The Math Module
import math
x = math.sqrt(64) # math.sqrt() method for example, returns the square root of a number:
print('sqrt: ',x)


x = math.ceil(1.4) # method rounds a number upwards to its nearest integer,
y = math.floor(1.4) # method rounds a number downwards to its nearest integer,

print('ceil: ',x) # returns 2
print('floor: ',y) # returns 1


# The math.pi constant, returns the value of PI (3.14...):
x = math.pi

print(x)