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
# The function should then read in the user's response.
# Finally, the function should return the direction corresponding to user's response.
# The third function should be named run and should have no parameters.
# The function should create an empty list named route.
# The function should start be displaying the message "Working out escape route...".
# The function should then use a loop to do the following 5 times:
#    Call the function menu and append the returned direction to the list route.
# Finally, the function should display the message "Escape route: {route}" where {route} is the content of the list route.


def directions():
  # Initialise directions list and populate
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  get_directions = directions()
  # Display Menu List
  for i in range(0, len(get_directions), 1):
    print("{}: {}.".format(i, get_directions[i]))
  # User menu item selection
  menu_item = get_directions[int(input())]
  return menu_item

def run():
  # initialise route list
  route = []
  print("\nWorking out escape route...")
  # Cycle through menu and selection 5 times, and add to route list
  for i in range(5):
    route.append(menu())
  # Display escape route chosen 
  print("\nEscape route: {}".format(route))

run()