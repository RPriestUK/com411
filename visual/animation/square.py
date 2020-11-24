# We now wish to create a program that shows some animated squares - a small square, followed by a medium square, followed by a large square.


# he Program: You should create a program that does the following:
# The program should consist of the following three functions:
# The first function should be named init and should have 0 parameters.
# The function should populate a global list of dictionaries that contains 3 dictionaries where each dictionary contains the coordinates for a square (small, medium and large).

# The second function should be named animate and should have 1 parameter that represents the current frame number
# The function should render each box in the list of dictionaries of the first function.  You should use % (mod) operator to work out which box to display.
# The third function should be named run and should have no parameters. 
# The function should create an animation that displays the boxes.
# Finally, the function should show the plot.

# Code your solution (visual/animations/squares.py) and be sure to include appropriate comments in your code.

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

fig, ax = plt.subplots()
squares = []

def init():
  # The function should populate a global list of dictionaries that contains 3 dictionaries where each dictionary contains the coordinates for a square (small, medium and large).
  squares.append(squareCoords('small'))
  squares.append(squareCoords('medium'))
  squares.append(squareCoords('large'))
  # squares.append({'x':[1, 1, 6, 6, 1], 'y':[6, 1, 1, 6, 6]})

def squareCoords(size):
  # The function creates a dictionary of a square's x and y values using size parameter
  square = {}
  if (size == 'large'):
    square['x'] = [1, 1, 6, 6, 1]
    square['y'] = [6, 1, 1, 6, 6]
  elif (size == 'medium'):
    square['x'] = [2, 2, 5, 5, 2]
    square['y'] = [5, 2, 2, 5, 5]
  elif (size == 'small'):
    square['x'] = [3, 3, 4, 4, 3]
    square['y'] = [4, 3, 3, 4, 4]
  return (square)

def animate(frame):
  # The function should render each box in the list of dictionaries of the first function.  You should use % (mod) operator to work out which box to display.
  global ax

  # create index of squares
  index = frame % len(squares)

  # clears previous lines to prevent overlap of frames
  ax.cla()

  # declare max sizes to fix figure size from start, y requires to be a minus value if x is positive or 0
  ax.set_xlim(0,7)
  ax.set_ylim(0,7)

  # plot each frame's x & y, with solid black line 
  ax.plot(squares[index]['x'], squares[index]['y']) 

def run():
  # figure to draw to, function to call for animation, number of frames (range, i.e. upto i), interval between frames, repetition, initialising function)
  sine_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 1000, init_func=init()) 

  plt.show()

run()