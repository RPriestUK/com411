# We wish to create a program that listens for sounds in the cave.

# The program should start by defining a function that has the name listen and which takes 0 parameters.
# The function should do the following:
#    Ask the user to enter a word representing a sound.
#    Display the message "That was a loud" followed by the word entered by user and an exclamation mark.
# Finally, the program should contain a call to your function listen

def listen():
  # Ask the user to enter a word representing a sound.
  print("What sound did I hear?")
  sound = str(input())

  # Display the message "That was a loud" followed by the word entered by user and an exclamation mark.
  print("That was a loud {}!".format(sound))

# call listen function
listen()

