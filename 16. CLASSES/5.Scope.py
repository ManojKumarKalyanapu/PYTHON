# Scope refers to the region in a program where a variable is recognized and accessible.
# Python uses the LEGB Rule to define variable scope:
# Local → Enclosing → Global → Built-in


# 1. Local Scope
# Variables defined inside a function.
# Only accessible within that function.
def my_func():
    x = 10  # Local scope
    print(x)

my_func()
# print(x)  # Error: x is not defined

# 2. Enclosing Scope (Nonlocal Scope)
# Variables defined in a nested function's outer function.
# Accessible in inner/nested functions via nonlocal.
def outer():
    y = 20  # Enclosing scope

    def inner():
        nonlocal y
        y += 5
        print("Inner:", y)

    inner()
    print("Outer:", y)

outer()

# 3.Global Scope
# Defined outside of functions.
# Accessible anywhere in the module, unless shadowed by local variables.
z = 30  # Global variable

def show():
    print("Global z:", z)

show()
print("Outside:", z)


count = 0

# To modify a global variable inside a function, use global:
def increment():
    global count
    count += 1

increment()
print(count)


# 4. Built-in Scope
# Predefined names like len, sum, print, etc.
# Available everywhere in Python.
print(len("scope"))  # len is from built-in scope


'''
| **Scope Type** | **Defined Where?**           | **Accessible Where?**       |
| -------------- | ---------------------------- | --------------------------- |
| Local          | Inside a function            | Only inside that function   |
| Enclosing      | Outer function of nested one | Inside inner functions      |
| Global         | At the top level of a module | Anywhere within the module  |
| Built-in       | Python predefined names      | Anywhere in Python programs |

'''