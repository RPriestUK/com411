# We wish to help Beep and Bop search the books.

# We will use the following data file (books.txt):

# Section:The Law Section
# The Magna Carta
# Section:The Technology Section
# How to build a robot
# How to build a flying car
# Section:The History Section
# The history of everything

# The program should consist of the following three functions:

# The first function should be named search and should take 1 parameter that represents the name of a file.
# The function should start by displaying the message "Searching...".
# The function should then create an empty list named sections.
# The function should then create an empty list named books.
# The function should then open the specified file for reading.
# For each line in the file, the function should do the following:
#     If the line begins with "Section" then
#          Retrieve the section name (e.g. "The Law Section" should be retrieved if the line is "Section:The Law Section". Note that you should use the methods str.startswith() and str.split() to help you with this.)
#          Add the section name to the list sections.
#      If the line does not being with "Section" then
#          Add the line to the list books.
# The function should then display the message "Done!".
# Finally, the function should return a tuple containing sections and books.
# The second function should be named save and should take 2 parameters.
# The first parameter is the name of file.
# The second parameter is is a tuple that represents the data to be stored.
# The function should display the message "Saving...".
# The function should then open the specified file for writing.
# The function should then write the line "Sections: [sections]" to the file where [sections] is each section in data.
# The function should then write the line "Books: [books]" to the file where [books] is each book in data.
# Finally, the function should display the message "Done!".
# The third function should be named run and should have no parameters.
# The function should call the first function to retrieve the tuple and store this in a local variable named data.
# The function should then pass variable as an argument to the second function along with the filename "section-books.txt".
# An example run of such a program is shown below:

# Searching...Done!
# Saving...Done!
# The content of the file section-books.txt should be as follows:

# Sections: The Law Section, The Technology Section, The History Section
# Books: The Magna Carta, How to build a robot, How to build a flying car, The history of everything

def search(filename):
  print("Searching...")
  # Initialise lists
  sections = []
  books = []

  # Open file
  with open(filename, "r") as file:
    # List lines from file and add to relevant list
    for line in file:
      # Check for 'section' substring
      if line.startswith('Section') == True:
        # Add section name to sections list
        # split the Section:SectionName and replace trailing new line with comma
        section = line.split(':')[1].replace("\n", ", ")
        sections.append(section)
      else:
        # Add book name to books list
        # replace trailing new line with comma
        book = line.replace("\n", ", ")
        books.append(book)
  print("Done!")
  return(sections, books)

# Save file
def save(filename, data):
  print("Saving...")
  
  # Open file
  with open(filename, "w") as file:
    # Create sections line
    file.write("Sections: ")
    for section in data[0]:
      file.write(section)
    # Create books line
    file.write("\nBooks: ")
    for book in data[1]:
      file.write(book)
  print("Done!")

def run():
  # Initialise variables
  sourcedata = search("data/files/txt/books.txt")
  destfile = "data/files/txt/section-books.txt"
  # Save file with sourcedata
  save(destfile,sourcedata)

run()