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

# import built-in classes
import random as random
import matplotlib.pyplot as plt

# import parent (Super) classes
from robot import Robot
from human import Human
from planet import Planet


# Universe class
class Universe:
  # initialise instance variables
  def __init__(self):
    # create list of planets
    self.planets = []
  
  def generate(self):
    # - creates a new planet object
    # - adds a random number of humans and robots to the    planet object
    planet = Planet()

    # create a set number in a range or 
    # random number of planets
    num_of_planets = range(0, 1, 1) 
    # range(0, random.randint(1, 20), 1)

    for planets in num_of_planets:
      # - adds the planet object to the list of planets

      # creates random number of humans & robots
      num_of_humans = range(0, random.randint(1, 20), 1)
      num_of_robots = range(0, random.randint(1, 20), 1)
      
      # adds random humans and robots to planet
      for index in num_of_humans:
        newhuman = Human(f'Human{index}')
        planet.add_human(newhuman)
        index += 1
      
      for index in num_of_robots:
        newrobot = Robot(f'Robot{index}')
        planet.add_robot(newrobot)
        index += 1
          
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

  # display populations per planet in matplotlib
  def show_populations(self):
      num_subplots = len(self.planets)
      
      fig, axs = plt.subplots(1, num_subplots)
      
      for index in range(num_subplots):
        planet = self.planets[index]
        num_humans = len(planet.inhabitants['humans'])
        num_robots = len(planet.inhabitants['robots'])

        if (num_subplots == 1):
          axs.bar([1, 2], [num_humans, num_robots])
        else:
          axs[index].bar([1, 2], [num_humans, num_robots])

      plt.tight_layout()  
      plt.show()

# run following code when default code block is __main__.
if (__name__ == "__main__"):
  universe = Universe()
  print() 
  # generate multiple planets using universe
  universe.generate()
  universe.generate()
  universe.show_populations()
  universe.display()


