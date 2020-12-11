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
    # - adds a random number of inhabitants to a planet object
    # - adds planet object to the universe object
    planet = Planet()

    # create a set number in a range or 
    # random number of planets
    num_of_planets = range(0, 1, 1) 
    # num_of_planets = range(0, random.randint(1, 20), 1)

    for index in num_of_planets:
      # creates random number of inhabitants
      num_of_inhabitants = range(0, random.randint(1, 50), 1)

      # adds random inhabitants to planet
      for inhabitant in num_of_inhabitants:
        # randomly selects inhabitant type (Human, Robot, Alien)
        # and assigns to relevant group
        num_of_pop_types = range(0, random.randint(1, 2), 1)
        for pop_type in num_of_pop_types:
          if pop_type == 0: # Human
            newinhabitant = Human(f'Human{inhabitant}')
          elif pop_type == 1: # Robot
            newinhabitant = Robot(f'Robot{inhabitant}')
          elif pop_type == 2: # Alien
            print("new alien")
            #newinhabitant = Alien(f'Alien{inhabitant}')
          planet.add_inhabitant(newinhabitant)

      # adds the planet object to the list of planets
      self.planets.append(planet)

  # Displays list of planets and populations in the universe
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
    return f'The Universe Class contains a list of {len(self.planets)} Planets, each with a list of inhabitants (types: humans, robots); {self.planets}.'

  # display populations per planet in matplotlib
  def show_populations(self):
    # initialise plot and figure values for visualisations
    num_subplots = len(self.planets)

    # plt.subplots(rows, cols, params)
    fig, axs = plt.subplots(1, num_subplots, sharey=True) 
    fig.suptitle('Population per Planet')

    # loop through planets to retrieve population data
    # and assign to associated subplot on visualisation
    for index in range(num_subplots):
      planet = self.planets[index]
      # initialise population values for each type
      num_humans = 0
      num_robots = 0
      # num_aliens = 0

      for inhabitant in planet.inhabitants:
        if isinstance(inhabitant, Human):
          num_humans += 1
        elif isinstance(inhabitant, Robot):
          num_robots += 1    
        # elif isinstance(inhabitant, Alien):
        #  num_aliens += 1      

      # create graph with labels for number of population
      # per planet. 
      if (num_subplots == 1):
        axs.bar(["Human", "Robot"], [num_humans, num_robots])
      else:
        axs[index].bar(["Human", "Robot"], [num_humans, num_robots])
        axs[index].set_xlabel('Population Type')
        axs[index].set_ylabel('Total')
        axs[index].set_title(f"Planet: {index}")

    plt.tight_layout()  
    plt.show()
    
# run following code when default code block is __main__.
if (__name__ == "__main__"):
  universe = Universe()
  print() 
  # generate multiple planets using universe
  universe.generate()
  universe.generate()
  universe.generate()
  universe.generate()
  universe.generate()
  universe.show_populations()
  #universe.display()


