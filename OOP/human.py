# The Program: You are required to create a two basic classes as follows:

# Robot

# This should be the same as the one in the example above. 
# You can test this class by using it to create an object and displaying it using the code below:
# if (__name__ == "__main__"):
#   robot = Robot()
#   robot.display()

# Human

# The class should be named Human.  The class should have the following:

# class attribute:
#   MAX_ENERGY which should be set to 100. Note, that this is uppercase as it is intended to be a constant.

# instance attributes:
#   name, age and energy. 
# initializer:
#   This should set name to "Human", age to 0 and energyto MAX_ENERGY, respectively.
# instance methods:
#   display - This should display name of the human in the form "I am {name}" where {name} should be replaced by the name of the human.

# You can test this class by creating an object and display it using the code below:
# if (__name__ == "__main__"):
#   human = Human()
#   human.display()class Robot:

class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  # repr string, used for debugging
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  # str string for user friendly output
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'

class Human:

  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")

# default invisible name for program
if (__name__ == "__main__"):
  human = Human()
  human.display()
  print()
  robot = Robot()
  print(robot.__str__())