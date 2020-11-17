# We wish to create a program to display the path Beep and Bop are taking through Robo City.

# The program should consist of the following three functions:

# The first function should be named data and should have no parameters.
# The function should start by creating an empty dictionary named paths.
# The function should then ask the user what type of line they would like (dotted, dashed or solid) and read in the user's response.
# The function should then ask the user what colour they would like (red, green, blue) and read in the user's response.
# The function should then ask the user what style of marker they would like (circle, square or triangle) and read in the user's response.
# The function should then store the line style, colour, marker style in the dictionary as key-value pairs
# Finally, the function should return the dictionary.

# The second function should be named generate and should have no parameters. 
# The function should start by displaying the message "How many lines would you like to display?" and then read in the user's response.
# The function should then create a loop that iterates as many times as the number of lines specified by user and does the following:
#     Call the first function and store the result in a variable named data.
#     Display a line graph using the values stored in data.

# The third function should be named run and should have no parameters.
# The function start by displaying the message "Running....".
# The function should then call the second function.
# Finally, the function should display the message "Done!".

# When executed, the program should display the line plots as specified by the user.

# import library
import matplotlib.pyplot as plt
import random as random

def datas():
  # The function should start by creating an empty dictionary named paths.
  paths = {}

  # The function should then ask the user what type of line they would like (dotted, dashed or solid) and read in the user's response.
  print("Please choose a line style:")
  print("[1] Dotted ...")
  print("[2] Dashed ---")
  print("[3] Solid -")
  choice = int(input())
  if (choice == 1):
    ls = ":"
  elif (choice == 2):
    ls = "--"
  elif (choice == 3):
    ls = "-"
  # The function should then ask the user what colour they would like (red, green, blue) and read in the user's response.
  print("Please enter a colour for the line:")
  print("[1] Red")
  print("[2] Green")
  print("[3] Blue")
  choice = int(input())
  if (choice == 1):
    lc = "r"
  elif (choice == 2):
    lc = "g"
  elif (choice == 3):
    lc = "b"
  # The function should then ask the user what style of marker they would like (circle, square or triangle) and read in the user's response.
  print("Please choose the marker style:")
  print("[1] Circle")
  print("[2] Square")
  print("[3] Triangle")
  choice = int(input())
  if (choice == 1):
    ms = "o"
  elif (choice == 2):
    ms = "s"
  elif (choice == 3):
    ms = "^"
  # The function should then store the line style, colour, marker style in the dictionary as key-value pairs
  paths = {"LineStyle":ls, "LineColour":lc, "MarkerStyle":ms}
  # Finally, the function should return the dictionary.
  return paths

def generate():
  # The function should start by displaying the message "How many lines would you like to display?" and then read in the user's response.
  print("How many lines would you like to display?")
  nol = int(input())
  # The function should then create a loop that iterates as many times as the number of lines specified by user and does the following:
  for count in range(0, nol, 1):
    #     Call the first function and store the result in a variable named data.
    #     Display a line graph using the values stored in data.
    data = datas()
    style = ""
    # retrieve style variables for line
    for key, value in data.items():
      style = style + value
    # retrieve coordinates
    coord = coordinates()
    x = coord[0]
    y = coord[1]
    # plot coordinates in the style requested by user
    plt.plot(x, y, style)
  plt.show()

def coordinates():
  # create random plot start and end coordinates for each line
  x = []
  y = []
  # count 2 for start & end
  for count in range(2):
    x.append(random.randint(1, 20))
    y.append(random.randint(1, 20))
  return (x, y)

def run():
  # The function start by displaying the message "Running....".
  print("Running...")
  # The function should then call the second function.
  generate()
  # Finally, the function should display the message "Done!".
  print("Done!")


run()

