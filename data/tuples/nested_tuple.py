# We wish to create a program to help Beep and Bop cross the falling steps.

# The program should consist of the following two functions:
# The first function should be named steps and should have no parameters.
# The function should create a list of tuples named likelihoods.
# The function should populate the list with the following tuples:

# ("step 1", 50)
# ("step 2", 38)
# ("step 3", 27)
# ("step 4", 99)
# ("step 5", 4)

# Finally, the function should return the list of tuples.
# The second function should be named run and should have no parameters.
# The function should call the first function and store the returned list in a local variable.
# The function should then create two empty lists, good_steps and bad_steps.
# The function should then loop through the list of steps retrieved previously and do the following for each step:
#    if the likelihood of the step falling is 50 or more then add the tuple to bad_steps
#    otherwise add the tuple to good_steps
# Finally, the function should display a message "Good steps: {good}, Bad steps: {bad}" where {good} is the number of good steps and {bad} is the number of bad steps.
# An example run of such a program is shown below: 

# Good steps: 2, Bad steps: 3

def steps():
  likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods

def run():
  all_steps = steps()
  good_steps = []
  bad_steps = []

  for index in range(0, len(all_steps), 1):
    # Retrieve data from steps into current step according to index location
    step = all_steps[index]
    # Add data from tuple to relevant good/bad lists
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step)

  # Display output by listing the count (length) of each list
  print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))

run()