# We wish to create a program to help Beep and Bop record how many of each type of item they saw (e.g. 2 skyscrapers, 5 neon signs, etc.).

# The program should consist of the following two functions:
# The first function should be named observed and should have no parameters.
# The function should create a list named observations.
# The function should populate the list with 7 values read in from the user.  There should be some duplicate values.
# Finally, the function should return the list named observations.
# The second function should be named run and should have no parameters.
# The function should start by displaying the message "Counting observations...".
# The function should then call the first function and store the returned list in a local variable.
#The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list e.g. ("Skyscraper", 2)
# Finally, the function should display the content of the set.

def observed():
  # define empty list
  observations = []
  # loop for 7 input requests
  for count in range(7):
    # Ask user for objects they have observed and add to list
    print("Please enter an observation:")
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  # assign to local set 
  observations = observed()
  observations_set = set()
  # count number of each instance entered
  for observation in observations:
    # count the number of each type in observations set
    num = observations.count(observation)
    observations_set.add((observation, num))
  # Display number
  for key, value in observations_set:
    print("{} observed {} times.".format(key, value))
  

run()
