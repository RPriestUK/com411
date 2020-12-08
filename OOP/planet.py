# The Program: You are now required to create a new class as follows:
# Planet:

# The class should be named Planet.
# The class should contain the following instance variables:
#   humans - a list of human objects (initially an empty # list)
#   robots - a list of robot objects (initially an empty list)

# The class should contain the following instance methods:

#   add_human - adds a human object to the list of humans
#   remove_human - removes a human object from the list of humans

#   add_robot - adds a robot object to the list of robots
#   remove_robot - removes a robot object from the list of robots

# The class should contain the following magic methods:

#   __repr__ - returns a string containing a formal representation of a planet object (includes the list of humans and the list of robots)

#    __str__ - return a string containing an informal representation of a planet object (includes the list of humans and the list of robots)

# You should add suitable code to create and test your class Planet.

from robot import Robot
from human import Human

class Planet:
  # The class should contain the following instance variables:
  #   humans - a list of human objects (initially an empty # list)
  #   robots - a list of robot objects (initially an empty list)
  def __init__(self):

    self.inhabitants = {
      'humans': [],
      'robots': []
    }
  
  # The class should contain the following instance methods:

  #   add_human - adds a human object to the list of humans
  #   remove_human - removes a human object from the list of humans

  #   add_robot - adds a robot object to the list of robots
  #   remove_robot - removes a robot object from the list of robots

  def add_human(self, human):
    # adds entered inhabitant to humans list
    self.inhabitants['humans'].append(human)
  
  def remove_human(self, human):
    # checks the inhabitant is in the list and removes them, otherwise displays error
    if (self.inhabitants['humans'].count(human) <= 0):
      print("The inhabitant '{}' is not in the 'Humans' list".format(human))
      print() 
    else:
      self.inhabitants['humans'].remove(human)
  
  def add_robot(self, robot):
    # adds entered inhabitant to robots list
    self.inhabitants['robots'].append(robot)
  
  def remove_robot(self, robot):
    # checks the inhabitant is in the list and removes them, otherwise displays error
    if (self.inhabitants['robots'].count(robot) <= 0):
      print("The inhabitant '{}' is not in the 'Robots' list".format(robot))
      print() 
    else:
      self.inhabitants['robots'].remove(robot)
  
  # The class should contain the following magic methods:

  #   __repr__ - returns a string containing a formal representation of a planet object (includes the list of humans and the list of robots)

  #    __str__ - return a string containing an informal representation of a planet object (includes the list of humans and the list of robots)

  # repr string, used for debugging
  def __repr__(self):
    return f'planet(inhabitants={self.inhabitants})'

  # str string for user friendly output
  def __str__(self):
    return f"The Planet contains 1 dictionary of 2 lists; Humans: {self.inhabitants['humans']} & Robots:{self.inhabitants['robots']}."

# You should add suitable code to create and test your class Planet.
if (__name__ == "__main__"):
  planet = Planet()
  print() 
  print("User friendly (str):")
  print(str(planet))
  print() 
  print("Debug (repr):")
  print(repr(planet))
  print() 
  # add to human list to populate
  bob = Human("Bob", 5)
  dick = Human("Dick", 15)
  harry = Human("Harry", 98)  
  planet.add_human(bob)
  planet.add_human(dick)
  planet.add_human(harry)
  # add to robot list to populate
  beep = Robot("Beep")
  boop = Robot("Boop", 6)
  walle = Robot("Wall-e", 3)
  planet.add_robot(beep)
  planet.add_robot(boop)
  planet.add_robot(walle)
  # remove from human list to confirm
  planet.remove_human("Dick")
  planet.remove_human("Dick")
  # remove from robot list to confirm
  planet.remove_robot("Boop")
  # display user friendly output to show populated lists:
  print(str(planet))
  print() 