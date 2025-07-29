
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Global Keyword
def myfuncGlobal():
  global a
  a = "fantastic"

myfuncGlobal()

print("Python Global Key " + a)