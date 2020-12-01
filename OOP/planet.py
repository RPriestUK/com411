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

class Planet:
  # The class should contain the following instance variables:
  #   humans - a list of human objects (initially an empty # list)
  #   robots - a list of robot objects (initially an empty list)
  def __init__(self):

    self.humans = []
    self.robots = []
  
  # The class should contain the following instance methods:

  #   add_human - adds a human object to the list of humans
  #   remove_human - removes a human object from the list of humans

  #   add_robot - adds a robot object to the list of robots
  #   remove_robot - removes a robot object from the list of robots

  def add_human(self, human):
    self.humans.append(human)
  
  def remove_human(self, human):
    self.humans.remove(human)
  
  def add_robot(self, robot):
    self.robots.append(robot)
  
  def remove_robot(self, robot):
    self.robots.remove(robot)
  
  # The class should contain the following magic methods:

  #   __repr__ - returns a string containing a formal representation of a planet object (includes the list of humans and the list of robots)

  #    __str__ - return a string containing an informal representation of a planet object (includes the list of humans and the list of robots)

  # repr string, used for debugging
  def __repr__(self):
    return f'planet(humans={self.humans}, robots={self.robots})'

  # str string for user friendly output
  def __str__(self):
    return f'The Planet Class contains 2 lists; Humans: {self.humans} and Robots: {self.robots}.'

# You should add suitable code to create and test your class Planet.
if (__name__ == "__main__"):
  planet = Planet()
  print("User friendly (str):")
  print(str(planet))
  print() 
  print("Debug (repr):")
  print(repr(planet))
  print() 
  # add to human list to populate
  planet.add_human("Bob")
  planet.add_human("Dick")
  planet.add_human("Harry")
  # add to robot list to populate
  planet.add_robot("Beep")
  planet.add_robot("Boop")
  planet.add_robot("Wall-e")
  # remove from human list to confirm
  planet.remove_human("Dick")
  # remove from robot list to confirm
  planet.remove_robot("Boop")
  # display user friendly output to show populated lists:
  print(str(planet))
  print() 