# The program should consist of the following two functions:
# The first function should be named search and should take 1 parameter that represents a file name
# The function should start by displaying the message "Searching...".
# The function should then open the specified file for reading.
# For each line in the file, the function should display the message "Looked in {location}" where {location} is a line from the file.
# Finally, the function should display the message "...Done!".
# The second function should be named run and should have no parameters.
# The function should call the first function with the argument "locations.txt".

# An example run of such a program is shown below:

# Searching...
# Looked in The Law Section.
# Looked in The Art Section
# Looked in The Technology Section.
# Looked in The History Section.
# ...Done!

def search(filename):
  print("Searching...")
  # open file
  with open(filename) as file:
    # List locations from file
    for location in file:
      print(f"Looked in {location}", end = "")
  print("\n...Done!")

def run():
  search("data/files/txt/books.txt")

run()