# You should create a program that does the following:
# The program should consist of the following two functions:

# The first function should be named animate and should have 1 parameter that represents the current frame number
# The function should display a sine wave that shifts each time a new frame is rendered.
# The second function should be named run and should have no parameters. 
# The function should create an animation with 720 frames and an interval of 100.
# Finally, the function should show the plot.

# Code your solution (visual/animations/shift_sine.py) and be sure to include appropriate comments in your code.

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  # retrieve value of pi for creating y value
  pi = np.pi

  # clears previous lines to prevent overlap of frames
  ax.cla()

  # declare max sizes to fix figure size from start, y requires to be a minus value if x is positive or 0
  ax.set_xlim(0,pi)
  ax.set_ylim(-1.5,1.5)
  
  # create x and y values for sine wave (x * pi divided 180)
  x = np.arange(0, 2*pi, 0.01)
  y = np.sin(x + frame / 50)

  # plot each frame's x & y, with solid black line 
  ax.plot(x, y, 'b-o', linewidth=1, markersize=1) 

def run():
  # figure to draw to, function to call for animation, number of frames (range, i.e. upto i), interval between frames, repetition - needs to be assigned to a variable
  sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100) 

  plt.show()

run()

