import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame):    
  # declare max sizes to fix figure size from start, or omit to resize figure's axis to the data as it is populated
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  # plot each frame's x & y, with red O markers
  ax.plot(frame, frame, 'ro') 
     
def run():
  global fig  
  # your code here
  basic_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000, repeat = False)   

  plt.show() # Display

run()  