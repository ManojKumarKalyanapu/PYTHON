# Python Strings
print("Hello")

a = "Hello"
print(a)

# muiltiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays
x = "Hello World"
print(x[0])  # H

# Looping through a String
for x in "banana":
    print(x)
    
# String Length
x = "Hello World"
print(len(x))  # 11

# Check String
txt = "The best things in life are free!"
print("free" in txt)  # True

# use if in statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check NOT in String
txt = "The best things in life are free!"
print("expensive" not in txt)  # True

# use if NOT in statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")