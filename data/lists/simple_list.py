# We wish to create a program to help Beep and Bop find their way through the maze.

# The program should consist of the following two functions:

# The first function should be named directions and should have no parameters.
# The function should create a list named directions.
# The function should populate the list with the following items: "Move Forward", "Move Backward", "Turn Left" and "Turn Right". 
# Finally, the function should return the list directions.
# The second function should be named run and should have no parameters. 
# The function should call the first function and display the list returned by the call.

def directions():
  # Initialise list and populate with values
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
  
def run():
  print(directions())

run()