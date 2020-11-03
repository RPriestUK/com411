# We wish to create a program to help Beep and Bop decipher the pattern.
# The program should consist of the following two functions:

# The first function should be named pattern and should have no parameters.
# The function should create a dictionary named sequences.
# The function should populate the dictionary with the following items: "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1
# Finally, the function should return the dictionary
# The second function should be named run and should have no parameters. 
# The function should call the first function and display the dictionary returned by the call.

# An example run of such a program is shown below:

# {'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}

def pattern():
  sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
  return sequences

def run():
  print(pattern())


run()
