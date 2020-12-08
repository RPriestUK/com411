# The Program: You are required to create a basic class as follows:

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


class Human:

  # A class attribute
  MAX_ENERGY = 100

  # An initialiser (special instance method)
  def __init__(self, name="Human", age=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  # grow by 1 year
  def grow(self):
    self.age += 1
  
  # human can eat to regain energy, but cannot exceed MAX_ENERGY
  def eat(self, amount=0):
    if (self.energy + amount) < Human.MAX_ENERGY:
      self.energy += amount
    else:
      print("I can't eat that, I'm too full!")
  
  # human moves as per distance parameter, but won't move if energy level reduces further than 0
  def move(self, distance=0):
    if (self.energy - distance) > 0:
      self.energy -= distance
    else:
      print("I can't do that, I'm too tired!")

  # repr string, used for debugging
  def __repr__(self):
    return f'human(name={self.name}, age={self.age})'

  # str string for user friendly output
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, and I am a Human.'

# default invisible name for program
if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  print() 
  print(str(human))
  print()
  human.move(20)
  print(human.energy)
  human.eat(30)
  print(human.energy)