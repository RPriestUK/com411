# Beep and Bop wish to create a program which manipulate cryptic words. The program should prompt the user to enter a word. The program should then prompt the user to choose one of the following options:

# 1) Display in a Box – display the word in an ascii art box
# 2) Display Lower-case – display the word in lower-case e.g. hello
# 3) Display Upper-case – display the word in upper-case e.g. HELLO
# 4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
# 5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.

# The program should then read the option number entered by the user and carry out the appropriate actions.

# The program should contain 6 user-defined functions. One for each of the above options and one to run the program. 

def word_in_box(wordentered):
  # return the word in an ascii art box
  middle = ("\n* {} *\n".format(wordentered))
  border = ("*" * (len(middle) - 2))
  # concat top, middle and bottom of box
  box = border + middle + border
  # return completed box
  return box

def word_lower_case(wordentered):
  # return word in lower case
  return wordentered.lower()

def word_upper_case(wordentered):
  # return word in upper case
  return wordentered.upper()

def word_mirrored(wordentered):
  # return word in reverse
  mirrored = ("{} | {}".format(wordentered, ''.join(reversed(wordentered))))
  return mirrored

def word_repeat(wordentered):
  # Ask the user how many times to display the word 
  print("How many times should the word repeat?")
  r = int(input())

  # Initialise repeated string and iterations
  repeated = ""
  i = 0 

  # Build repeated string by alternate between upper and lower case for number of times entered by user
  while (i < r):
    if (i % 2 != 0):
      repeated = repeated + "\n" + word_upper_case(wordentered)
    else: 
      repeated = repeated + "\n" + word_lower_case(wordentered)
    i = i + 1
  
  # display the word that many times alternating between upper-case and lower-case.
  return repeated

# Ask user for word
print("Please enter a word")
wordentered = str(input())

# Ask user for option for updating word entered
print("\nPlease choose an option:")
print("\n1) Display in a Box")
print("2) Display Lower-case")
print("3) Display Upper-case")
print("4) Display Mirrored")
print("5) Repeat")
print() 
option = int(input())

# call function associated with user choice
if (option == 1):
  print(word_in_box(wordentered))
elif (option == 2):
  print(word_lower_case(wordentered))
elif (option == 3):
  print(word_upper_case(wordentered))
elif (option == 4):
  print(word_mirrored(wordentered))
elif (option == 5): 
  print(word_repeat(wordentered))