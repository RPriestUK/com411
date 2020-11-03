# We wish to create a program to help Beep and Bop identify the patterns.

# The program should consist of the following four functions:
# The first function should be named short_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"101"
# "occurrences":5
# Finally, the function should return the dictionary.

# The second function should be named medium_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"111000"
# "occurrences": 25
# Finally, the function should return the dictionary

# The third function should be named long_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"1100110011001100"
# "occurrences":50
# The fourth function should be named run and should have no parameters.
# The function should start by displaying the message "Analysing patterns...".
# The function should then create a dictionary with the following key-value pairs:
# "short sequence": value returned from first function
# "medium sequence": value returned from second function
# "long sequence": value returned from third function
# Finally, the function should display the content of the dictionary as key-value pairs using an appropriate loop

# An example run of such a program is shown below:

# Analysing patterns...
# short sequence: {'sequence': '101', 'occurrences': 5}
# medium sequence: {'sequence': '111000', 'occurrences': 25}
# long sequence: {'sequence': '1100110011001100', 'occurrences': 50}

def short_pattern():
  # populate dictionary
  pattern = {"sequence":"101", "occurrences":5}
  return pattern

def medium_pattern():
  # populate dictionary
  pattern = {"sequence":"111000", "occurrences": 25}
  return pattern

def long_pattern():
  # populate dictionary
  pattern = {"sequence":"1100110011001100", "occurrences":50}
  return pattern

def run():
  print("Analysing patterns...")
  # created nested dictionary with sequences
  nested = {"Short Sequence":short_pattern(), "Medium Sequence":medium_pattern(), "Long Sequence":long_pattern()}

  # loop through each nested dictionary item and display
  for key, value in nested.items():
    print("{}: {}".format(key, value))

run()