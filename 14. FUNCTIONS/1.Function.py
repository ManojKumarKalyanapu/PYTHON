# function
def my_function(fname): # fname is arguments
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# arbitrary arguments
def my_function(*kids):
  print(kids)
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# pass Statement
def myfunction():
  pass

# Positional-only arguments
def calculate(x, y, /, z):
    return (x + y) * z

print(calculate(2, 3, 4))       # ✅ valid
print(calculate(2, 3, z=4))     # ✅ valid
# print(calculate(x=2, y=3, z=4))  # ❌ TypeError

'''
| Position   | Symbol | Argument Type         |
| ---------- | ------ | --------------------- |
| Before `/` | `/`    | Positional-only       |
| After `/`  |        | Positional or keyword |
| After `*`  | `*`    | Keyword-only          |

'''

# Keyword-Only Arguments
def display_info(name, age, *, city, country):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")

# Valid usage
display_info("Alice", 30, city="New York", country="USA")

# Invalid: city and country must be keywords
# display_info("Alice", 30, "New York", "USA")  # ❌ TypeError


# Combine Positional-Only and Keyword-Only
def my_function(a, b, /, e, f, g, *, c, d):
    print(a + b + c + d, e, f, g)
my_function(5, 6, 1, f=2, g=3, c=7, d=8)

'''
| Parameter | Value | How it's passed |
| --------- | ----- | --------------- |
| `a`       | 5     | Positional only |
| `b`       | 6     | Positional only |
| `e`       | 1     | Positional      |
| `f`       | 2     | Keyword         |
| `g`       | 3     | Keyword         |
| `c`       | 7     | Keyword-only    |
| `d`       | 8     | Keyword-only    |

'''

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)