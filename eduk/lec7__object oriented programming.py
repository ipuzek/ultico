# object oriented programming #
# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-8-object-oriented-programming/ #

# everything in python is an object
# function is also an object

# 1. create an object
# 2. modify / manipulate an object (mutate) -- interact with it
# 3. delete an object / "forget" about it

#  objects are a data abstraction
# that captures…

# (1) an internal representation
# • through data attributes

# (2) an interface for interacting with object
# • through methods (aka procedures/functions)
# • defines behaviors but hides implementation

# in class quests:

# 1. Class Definition

# Which of the following is a good and valid definition for a class representing a car?

# def class Car(object): (just weird)
# class Car(object):
# def Car(object): (function definition)
# class A(object) (ok def, but not a Car object)

# 2. Class Instance

# Using the class definition below, which line creates a new Car object with 4 wheels and 2 doors?

# class Car(object):
#  def __init__(self, w, d):
#   self.wheels = w
#   self.doors = d
#   self.color = ""

# Car(mycar, 4, 2)              # mycar wtf?
# mycar = Car(4, 2, "white")    # color why?
# mycar = Car(4, 2)             # good
# mycar = Car(2, 4)             # just no

# 3. Methods

# Which of the following methods changes the color of the car, based on the definition below?

# class Car(object):
#  def __init__(self, w, d):
#   self.wheels = w
#   self.doors = d
#   self.color = ""

# def paint(c): color = c           # self needs to be the first parameter
# def paint(self, c): color = c     # just a variable, not a particular instance (self denotes instance)
# def paint(c): self.c = c          # self needs to be the first parameter
# def paint(self, c): self.color = c 

# 4. Method Call

# You create a car with mycar = Car(4, 2). Which is a line of code to change the color of mycar to “red”?

# class Car(object):
#  def __init__(self, w, d):
#   self.wheels = w
#   self.doors = d
#   self.color = ""
#   def paint(self, c):
#    self.color = c

#  Car.paint("red")         # needs to be mycar, missing object
#  mycar.paint(red)         # should be a string
#  mycar.paint("red") 
#  mycar.paint(Car, "red")  # no need for Car, just weird

# 5. Special Methods

# With the code below, what does the line print(mycar == yourcar) print?

# class Car(object):
#  def __init__(self, w, d):
#   self.wheels = w
#   self.doors = d
#   self.color = ""
#  def paint(self, c):
#   self.color = c
#  def __eq__(self, other):
#   if self.wheels == other.wheels and \
#   self.color == other.color and \
#   self.doors == other.doors:
#    return True
#   else:
#    return False

# mycar = Car(4, 2)
# mycar.paint("red")
# yourcar = Car(4,2)
# print(mycar == yourcar)

#  True     # difference in color
#  False
#  An error # no error because we defined the method



