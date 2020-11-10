# We wish to create a program to display the path Beep and Bop are taking through Robo City.

# The program should consist of the following three functions:

# The first function should be named small and should have no parameters.
# The function should display a small square using a line plot.
# The line should be a red dotted line with circle markers.
# The second function should be named medium and should have no parameters. 
# The function should display a medium square around the small square using a line plot.
# The line should be a green dashed line with square markers.
# The third function should be named large and should have no parameters.
# The function should display a large square around the medium square using a line  plot.
# The line should be a blue solid line with pentagon markers.

# import library
import matplotlib.pyplot as plt

# -- = dashed line 
# - = solid line 
# o = circle 
# s = square 
# p = pentagon

def small():
  # The function should display a small square using a line plot.
  # The line should be a red dotted line with circle markers.
  xval = [3, 3, 4, 4, 3]
  yval = [4, 3, 3, 4, 4]
  plt.plot(xval, yval, "r--o")


def medium():
  # The function should display a medium square around the small square using a line plot.
  # The line should be a green dashed line with square markers.
  xval = [2, 2, 5, 5, 2]
  yval = [5, 2, 2, 5, 5]
  plt.plot(xval, yval, "g--s")


def large():
  # The function should display a large square around the medium square using a line  plot.
  # The line should be a blue solid line with pentagon markers.
  xval = [1, 1, 6, 6, 1]
  yval = [6, 1, 1, 6, 6]
  plt.plot(xval, yval, "b-p")


small()
medium()
large()
plt.show()