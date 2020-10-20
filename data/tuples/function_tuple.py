# We wish to create a variation of our previous program to help Beep and Bop cross the falling steps.

# # The program should consist of the following two functions:
# The first function should be named likelihood and should have no parameters.
# The function should create a tuple named likelihoods.
# The function should populate the tuple with the following numerical data which represents the likelihood a step will fall:
# 50, 38, 27, 99, 4
# Finally, the function should find and return the minimum and maximum values in a tuple.
# An example run of such a program is shown below: 
# Minimum likelihood of falling: 4%
# Maximum likelihood of falling: 99%

def likelihood():
  # Create a tuple and return both minimum and maximum value
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run():
  # Run likelihood() and print outputs
  likelihoods = likelihood()
  print("Minimum likelihood of falling: {}%".format(likelihoods[0]))
  print("Maximum likelihood of falling: {}%".format(likelihoods[1]))

run()