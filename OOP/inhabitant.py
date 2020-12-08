# combines duplicated attributes and methods
# shared between the different types of planet
# inhabitants

class Inhabitant:

  # class attribute
  MAX_ENERGY = 100

  # 'pass' indicates an abstract which requires
  # sub classes to provide functionality
  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    pass

  # grow by 1 year
  def grow(self):
    self.age += 1
  
  # human can eat to regain energy, but cannot exceed MAX_ENERGY
  def eat(self, amount=0):
    if (self.energy + amount) < self.MAX_ENERGY:
      self.energy += amount
    else:
      print("I can't eat that, I'm too full!")
  
  # human moves as per distance parameter, but won't move if energy level reduces further than 0
  def move(self, distance=0):
    if (self.energy - distance) > 0:
      self.energy -= distance
    else:
      print("I can't do that, I'm too tired!")
