# We wish to create a variation of our previous program to help Beep and Bop escape the cave.

# The program should consist of the following three functions:

# The first function should be named directions and should have no parameters.
# The function should create a list named directions.
# The function should populate the list with the following items: "Move Forward", "Move Backward", "Turn Left" and "Turn Right". 
# Finally, the function should return the list directions.

# The second function should be named menu and should have no parameters.
# The function should start by displaying the message "Please select a direction:".
# The function should then call the first function and store the returned list in a local variable
# The function should then use a loop to display each direction in the list with an index number.  This should be displayed in the format "{index}: {direction}" where {index} is the index number of the list and {direction} is the direction from the list.

# The third function should be named run and should have no parameters.
# The function should simply call the function menu.

def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")

  get_directions = directions()
  
  # initialise vars
  menu_items = []

  for i in range(0, len(get_directions), 1):
    print("{}: {}.".format(i, get_directions[i]))
  return menu_items

def run():
  menu()

run()     