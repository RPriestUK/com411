# The Program: You are now required to add an extra class to the program.

# Universe:

# This class should be named Universe.
# This class should contain an instance variable that represents a list of planets.
# The class should contain an instance method called generate which does the following:
# - creates a new planet object
# - adds a random number of humans and robots to the planet object
# - adds the planet object to the list of planets
# Note: you can use a loop and math.random to generate the humans and robots.

# You should add suitable code to test your code.

import random as random

# Planet Class 
class Planet:
  # initialise instance variables
  def __init__(self):

    self.inhabitants = {
      'humans': [],
      'robots': []
    }

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

  # repr string, used for debugging
  def __repr__(self):
    return f'planet(inhabitants={self.inhabitants})'

  # str string for user friendly output
  def __str__(self):
    return f"The Planet contains 1 dictionary of 2 lists; Humans: {self.inhabitants['humans']} & Robots:{self.inhabitants['robots']}."

# Universe class
class Universe:
  # initialise instance variables
  def __init__(self):
    # create list of planets
    self.planets = []
  
  def generate(self):
    # - creates a new planet object
    # - adds a random number of humans and robots to the    planet object

    # create random number of planets
    num_of_planets = range(0, random.randint(1, 20), 1)

    for planets in num_of_planets:
      # - adds the planet object to the list of planets
      planet = Planet()

      # creates random number of humans & robots
      num_of_humans = range(0, random.randint(1, 20), 1)
      num_of_robots = range(0, random.randint(1, 20), 1)
      
      for human in num_of_humans:
        humanname = f'Human{human}'
        planet.add_human(humanname)
        human += 1
      
      for robot in num_of_robots:
        robotname = f'Robot{robot}'
        planet.add_robot(robotname)
        robot += 1
          
      self.planets.append(planet)
      planets += 1       

  def display(self):
    universe = self.planets
    for i in range(0, len(universe), 1):
      print("Planet {}: {}".format(i, universe[i]))
      i += 1
      
  # repr string, used for debugging
  def __repr__(self):
    return f'universe(planets={self.planets})'

  # str string for user friendly output
  def __str__(self):
    return f'The Universe Class contains a list of {len(self.planets)} Planets, each with a dictionary of two lists of inhabitant types (humans & robots); {self.planets}.'

# run following code when default code block is __main__.
if (__name__ == "__main__"):
  universe = Universe()
  print() 
  #print("User friendly (str):")
  #print(str(universe))
  #print() 
  universe.generate()
  #print(str(universe))
  #print()
  universe.display()


