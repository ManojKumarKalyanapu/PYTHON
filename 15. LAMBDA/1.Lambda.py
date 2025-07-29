# Lambda
# A lambda function is a small anonymous function.
# Syntax
# lambda arguments : expression

x = lambda a, b : a * b
print(x(5, 6))


# Why Use Lambda Functions?
# lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))