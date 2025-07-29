# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

class Student(Person): # inherit parent class
  def __init__(self, fname, lname): # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
      Person.__init__(self, fname, lname)
      super().__init__(fname, lname) # super() function that will make the child class inherit all the methods and properties from its parent:
      self.graduationyear = 2019 # adding property
  def welcome(self):
      print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
parent = Person("John", "Doe") # calling the parent class
parent.printname()
print('parent method: ',parent.printname) # prints memory location

child = Student("Mike", "Olsen") # calling child class
child.printname()
print('child property: ',child.graduationyear)
child.welcome()