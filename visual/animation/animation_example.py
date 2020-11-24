import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

fig, ax = plt.subplots()

def animate(frame):
  # clear axs (in this case - before each frame is drawn)
  ax.cla()
  # declare max sizes to fix figure size from start, or omit to resize figure's axis to the data as it is populated
  ax.set_xlim(0,100)
  ax.set_ylim(0,100)
  # plot each frame's x & y, with red O markers
  ax.plot(frame, frame, 'ro') 

def run():
  # figure to draw to, function to call for animation, number of frames (range, i.e. upto i), interval between frames, repetition - needs to be assigned to a variable
  basic_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 100, repeat = False) 

  plt.show()

run()
