# We wish to help Beep and Bop search the books.
# We will use the following data file (books.txt):

# Section:The Law Section
# The Magna Carta
# Section:The Technology Section
# How to build a robot
# How to build a flying car
# Section:The History Section
# The history of everything

# The program should consist of the following two functions:

# The first function should be named search and should take 1 parameter that represents the name of a file.
# The function should start by displaying the message "Searching...".
# The function should then create an empty dictionary named data.
# The function should then open the specified file for reading.
# For each line in the file, the function should do the following:
#     If the line begins with "Section" then
#         Retrieve the section name (e.g. "The Law Section" should be retrieved if the line is "Section:The Law Section". Note that you should use the methods str.startswith() and str.split() to help you with this.)
#         Store the section name in a variable named section that will be used as a key for the dictionary data.
#     If the line does not being with "Section" then
#         Add the line with the key section to the dictionary data. Note the dictionary should have a list of values for each key.
# The function should then display the message "Done!".
# Finally, the function should return the dictionary.
# The second function should be named run and should have no parameters.
# The function should call the first function with the file name "data/files/txt/books.txt" to retrieve the dictionary and store this in a local variable named data.
# The function should then write out the data to the file "data/files/txt/generated.csv" in CSV format so that it looks similar to the following:

# The Law Section,The Magna Carta
# The Technology Section,How to build a robot
# The Technology Section,How to build a flying car
# The History Section,The history of everything

def search(filename):
  print("Searching...")
  # Initialise dictionary & vars
  data = {}
  section = ""
  book = ""

  # Open file
  with open(filename, "r") as file:
    # List lines from file and add to relevant list
    for line in file:
      # Check for 'section' substring
      if line.startswith('Section') == True:
        # Add section name to dictionary
        # split the Section:SectionName and remove trailing new line char
        section = line.split(':')[1].replace("\n", ", ")
      else:
        # Add book name to dictionary
        # remove trailing new line char
        book = line.replace("\n", ", ")
        data[section] = book
  
  print("Done!")
  return data

def run():
  print(search("data/files/txt/books.txt"))

run()