# The Program: You are required to create a basic class as follows:

# Robot

# This should be the same as the one in the example above. 
# You can test this class by using it to create an object and displaying it using the code below:
# if (__name__ == "__main__"):
#   robot = Robot()
#   robot.display()

class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive" 
  MAX_ENERGY = 100

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  # grows by 1 year
  def grow(self):
    self.age += 1
  
  # robot can eat to regain energy, but cannot exceed MAX_ENERGY
  def eat(self, amount=0):
    if (self.energy + amount) < Robot.MAX_ENERGY:
      self.energy += amount
    else:
      print("I can't eat that, I'm too full!")
        
  # robot moves as per distance parameter, but won't move if energy level reduces further than 0
  def move(self, distance=0):
    if (self.energy - distance) > 0:
      self.energy -= distance
    else:
      print("I can't do that, I'm too tired!")

  # repr string, used for debugging
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  # str string for user friendly output
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, and I am a Robot.'

# default invisible name for program
if (__name__ == "__main__"):
  robot = Robot()
  print(repr(robot))
  print() 
  print(str(robot))
  print()
  robot.move(20)
  print(robot.energy)
  robot.eat(30)
  print(robot.energy)