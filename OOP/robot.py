# The Program: You are required to create a basic class as follows:

# Robot

# This should be the same as the one in the example above. 
# You can test this class by using it to create an object and displaying it using the code below:
# if (__name__ == "__main__"):
#   robot = Robot()
#   robot.display()

# import super class 'Inhabitant'
from inhabitant import Inhabitant

class Robot(Inhabitant):

  # class attributes
  laws = "Protect, Obey and Survive" 

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):
    # An instance attribute
    self.name = name
    self.age = age
    self.energy = self.MAX_ENERGY
  
    # A class method
  def the_laws():
    print(Robot.laws)

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  # repr string, used for debugging
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  # str string for user friendly output
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, have {self.energy} energy and I am a Robot.'

# default invisible name for program
if (__name__ == "__main__"):
  robot = Robot()
  # print(repr(robot))
  print() 
  print(str(robot))
  print()
  # robot.move(20)
  # print(robot.energy)
  # robot.eat(30)
  # print(robot.energy)