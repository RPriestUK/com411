# We wish to create a program to display the path Beep and Bop are taking through Robo City.

# The program should consist of the following two functions:

# The first function should be named display and should take 2 parameters.
# The first parameter is a list of x values.
# The second parameter is a list of y values.
# The function should display a line plot using the arguments supplied for the parameters.
# The second function should be named run and should take 0 parameters.
# The function should create an empty list named x_values containing the following values: 1, 2, 3, 4, 5
# The function should then create an empty list named y_values containing the following values: 1, 4, 9, 16, 25
# The function should then call the first  function passing x_values and y_values as arguments.

# import library
import matplotlib.pyplot as plt

def display(xval, yval):
  # display line plot using x & y vals
  plt.plot(xval, yval)
  plt.show()

def run():
  # populate x, y value lists
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  # run function to display chart
  display(x_values, y_values)

run()


