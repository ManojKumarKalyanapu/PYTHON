# A Class is like an object constructor, or a "blueprint" for creating objects.
class Person:
  def __init__(self, name, age): # __init__() function to assign values to object properties,
    self.name = name # this is properties of object
    self.age = age # self is used to access variables and it can be named has self or anything
    
  def myfunc(self): # functions are called has methods in class
    print("Hello my name is " + self.name)

  def __str__(self): # function controls what should be returned when the class object is represented as a string.
    return f"{self.name},{self.age}"

p1 = Person("John", 36)
p1.age = 40 # mofiying object properties
# del p1.age # delete object properties
p1.myfunc() # calling the object method
print(p1)


# class definitions cannot be empty, put in the pass statement to avoid getting an error.
class PersonPass:
    pass