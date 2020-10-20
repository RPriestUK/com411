# We wish to create a variation of our previous program to help Beep and Bop escape the cave.

# The program should consist of the following two functions:
# The first function should be named movements and should have no parameters.
# The function should create a list named path.
# The function should populate the list with the following values: "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1
# Finally, the function should return the list named path.
# The second function should be named run and should have no parameters.
# The function should start by displaying the message "Moving...".
# The function should then call the first function and store the return list in a local variable
# The function should then display the values in the list in the following format: "{direction} for {steps} steps" where {direction} is the direction of movement and {steps} is the number of steps to move.

def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  get_movements = movements()
  print("{} for {} steps".format(get_movements[0],get_movements[1]))
  print("{} for {} steps".format(get_movements[2],get_movements[3]))
  print("{} for {} steps".format(get_movements[4],get_movements[5]))
  print("{} for {} steps".format(get_movements[6],get_movements[7]))

run()