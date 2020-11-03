# We wish to create a program to help Beep and Bop record what they can see in the distance.

# The program should consist of the following two functions:

# The first function should be named observed and should have no parameters.
# The function should create a set named observations.
# The function should populate the list with the following items: "Flying Car", "Sky Scraper", "Laser" and "Dome". 
# Finally, the function should return the set observations.
# The second function should be named run and should have no parameters. 
# The function should call the first function and display the set returned by the call.


def observed():
  # Create set with observations
  observations = set({"Flying Car", "Sky Scraper", "Laser", "Dome"})
  return observations

def run():
  # Display result
  print(observed())

run()