# You should create a program that does the following:
# The program should consist of the following two functions:

# The first function should be named animate and should have 1 parameter that represents the current frame number
# The function should set the x limit for the axes to a minimum of 0 and a maximum of 720.
# The function should then set the y limit for the axes to a minimum of -1 and a maximum of 1.
# The function should then create a NumPy array named x with a range from 0 to the current frame number.
# The function should then calculate the y values by multiplying the x values by PI/180
# Finally, the function should plot the points given be x and y.

# The second function should be named run and should have no parameters. 
# The function should create an animation with 720 frames and an interval of 100.
# Finally, the function should show the plot.

# What interesting observations can be made?
# Code your solution (visual/animations/sine.py) and be sure to include appropriate comments in your code.

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  pi = np.pi
  # declare max sizes to fix figure size from start, y requires to be a minus value if x is positive/0
  ax.set_xlim(0,100)
  ax.set_ylim(-10,10)
  
  # create x and y values for sine wave (x * 180 divided by Pi)
  x_values = np.arange(0, 100)
  y_values = np.sin(x_values * (180/pi))

  # plot each frame's x & y, with solid black line 
  ax.plot(x_values, y_values, linestyle='solid', color='black') 

def run():
  # figure to draw to, function to call for animation, number of frames (range, i.e. upto i), interval between frames, repetition - needs to be assigned to a variable
  sine_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 1000, repeat = False) 

  plt.show()

run()