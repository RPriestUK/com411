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
  # define empty set
  Observations = set()
  # loop for 7 input requests
  for count in range(5):
    # Ask user for objects they have observed and add to set
    print("Please enter an observation:")
    Observations.add(input())
  return Observations

def remove_observations(observations):
  print("Are you sure you wish to delete an observation?")
  confirmation = str(input())
  while confirmation == "y":
    if confirmation == "y":
      # Request which observation to remove
      print("Please enter an observation to remove:")
      ob_to_rem = str(input())
      # discard entry if matching the input
      if (ob_to_rem == ""):
        # Remove observation
        observations.discard(ob_to_rem)
    else: 
      # leave observations
      print("Removal cancelled.")

def run():
  Observations = set()
  Observations(observed())
  remove_observations(Observations)