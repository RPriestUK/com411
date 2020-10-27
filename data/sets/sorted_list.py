# We wish to create a variation of our previous program to help Beep and Bop record their observations.

# The program should consist of the following three functions:

# The first function should be named observed and should have no parameters.
# The function should create a list named observations.
# The function should populate the list with 5 values read in from the user.  There should be some duplicate values.
# Finally, the function should return the list named observations.
# The second function should be named remove_observations and should take 1 parameter.
# The parameter should represent the list of observations.
# The function should ask the user if they wish to remove observations.
#While the user wishes to remove observations, the function should
#    Prompt the user to enter a string representing the observation (e.g. "Skyscraper") to be removed
   # The observation should then be removed from the list
# The third function should be named run and should have no parameters.
# The function should call the first function and store the returned list in a local variable.
# The function should then call the second function with the previously retrieved list.
# Finally, the function should display a sorted set of the observations and how many times each observation has been made.

def observed():
  # define empty list
  observations = []
  # loop for 5 input requests
  for count in range(5):
    # Ask user for objects they have observed and add to list
    print("Please enter an observation:")
    observations.append(input())
  return observations

def remove_observations(observations):
  # Initialise while loop
  is_running = True
  # ask for observation to remove while user has positively confirmed.
  while(is_running):
    # Get user's response
    print("Are you sure you wish to delete an observation? y/n")
    confirmation = str(input())
    # If user response is y, then remove from set, otherwise exit
    if (confirmation == "y"):
      # Request which observation to remove
      print("Please enter an observation to remove:")
      ob_to_rem = str(input())
      # discard entry if matching the input
      if (ob_to_rem == observations):
        # Remove observation
        observations.discard(ob_to_rem)
    else: 
      # exit loop
      is_running = False

# set observations to local var, run remove
def run():


  # Display sorted set after removals
  # assign to local set 
  observations = observed()
  remove_observations(observations)
  # Initialise new set
  observations_set = set()

  # count number of each instance entered
  for observation in observations:
    # count the number of each type in observations set
    num = observations.count(observation)
    observations_set.add((observation, num))

  # Display sorted set
  for key, value in sorted(observations_set):
    print("{} observed {} times.".format(key, value))
  
  
# Start program
run() 