# We wish to create a program to help Bop climb the bridge ladder.

# The program should consist of the following two functions:

# The first function should be named display_ladder and should have one parameter steps representing the number of steps on the ladder.  This function should display an ASCII ladder with the same number of steps as the value of the parameter steps.

# The second function should be named create_ladder and should have no parameters.  This function should ask the user for the number of steps and then use the value in a call to the first function.

# Finally, the program should contain a call to the second function.

def display_ladder(steps):
  
  # initialise iteration and 
  i = 0 
  print("    | |")

  while (i < steps): 
    # display a new rung on the ladder
    print("""    ***
    | |""")
    i = i + 1


def create_ladder():
  # Ask user for number of steps
  print("Please enter the number of steps remaining on the ladder")
  s = int(input())

  # call other function with parameter from user
  display_ladder(s)

# call create ladder function
create_ladder()