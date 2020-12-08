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
  # generate empty list of inhabitants
  inhabitants = []

  # instance variables:
  def __init__(self):
    pass
    
  def add_inhabitant(self, inhabitant):
    # adds entered inhabitant to list
    self.inhabitants.append(inhabitant)
  
  def remove_inhabitant(self, inhabitant):
    # checks the inhabitant is in the list and removes them, otherwise displays error
    if (inhabitant in self.inhabitants):
      self.inhabitants.remove(inhabitant)
    else:
      print("The inhabitant '{}' is not in the 'Inhabitants' list".format(inhabitant))
      print() 
    
  # The class should contain the following magic methods:

  #   __repr__ - returns a string containing a formal representation of a planet object (includes the list of humans and the list of robots)

  #    __str__ - return a string containing an informal representation of a planet object (includes the list of humans and the list of robots)

  # repr string, used for debugging
  def __repr__(self):
    return f'planet(inhabitants={self.inhabitants})'

  # str string for user friendly output
  def __str__(self):
    return f"The Planet contains a list of inhabitants; Humans & Robots: {self.inhabitants}."

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
  planet.add_inhabitant(bob)
  planet.add_inhabitant(dick)
  planet.add_inhabitant(harry)
  # add to robot list to populate
  beep = Robot("Beep")
  boop = Robot("Boop", 6)
  walle = Robot("Wall-e", 3)
  planet.add_inhabitant(beep)
  planet.add_inhabitant(boop)
  planet.add_inhabitant(walle)
  # remove from list to confirm
  planet.remove_inhabitant(dick)
  planet.remove_inhabitant(dick)
  # remove from list to confirm
  planet.remove_inhabitant(boop)
  # display user friendly output to show populated lists:
  print(str(planet))
  print() 