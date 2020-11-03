# We wish to create a program to display information about the current working folder.

# The program should consist of the following two functions:

# The first function should be named cwd and should have no parameters.
# The function should retrieve the file path for the current working folder.
# The function should then display the message "The current working folder is {path}" where {path} is the previously retrieved path.
# The function should then display the message "The folder contains the following:".
# Finally, the function should then display each file contained in the current working folder.
# The second function should be named run and should have no parameters. 
# The function should display the message "Processing...".
# The function should then call the first function (cwd).

# An example run of such a program is shown below:

# Processing...
# The current working folder is /home/runner/com411
# The folder contains the following:
# cwd.py

import os 

# Retrieve current working directory (cwd) and files
def cwd():
  # check path
  path = os.getcwd()
  # Display results
  print(f"The current working folder is {path}")
  print("The folder contains the following:")
  # List files in folder path
  for file in os.listdir(path):
    print(file)

# Launch program
def run():
  print("Processing...")
  cwd()

run()