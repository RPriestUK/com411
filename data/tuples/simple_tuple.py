# We wish to create a program to help Beep and Bop decide which steps to take.

# The program should consist of the following two functions:

# The first function should be named likelihood and should have no parameters.
# The function should create a tuple named likelihoods.
# The function should populate the tuple with the following numerical data which represents the likelihood a step will fall:
# 50, 38, 27, 99, 4
# Finally, the function should return the step with the smallest likelihood of falling
# The second function should be named run and should have no parameters. 
# The function should call the first function and stored the returned value in a local variable
# The function should then display a message in the format: "Minimum likelihood of falling: {value}%" where {value} is the value returned by the previous function call.


def likelihood():
  # Create a tuple and return minimum value
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)

def run():
  # Run likelihood() and print output
  likelihoods = likelihood()
  print("Minimum likelihood of falling: {}%".format(likelihoods))

run()