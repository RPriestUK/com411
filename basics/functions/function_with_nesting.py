# We wish to create a program to help Beep and Bop escape the large boulder.

# The program should start by defining a function that has the name identify and which takes 0 parameters.
# The function should do the following:
#    Ask the user to enter a word representing what they see.
#    Read the user's response.
#    If the user's response is "a large boulder" then the message "It's time to run!" should be displayed.
#    Otherwise the message "We will be fine." should be displayed.
# Finally, the program should contain a call to your identify function.

def what_was_that():
  # Ask the user to enter a word representing what they see.
  print("What do you see?")
  sight = str(input())

  # Check string matches threat else display fine message
  if (sight.lower() == "a large boulder"):
    print("It's time to run!")
  else:
    print("We'll be fine.")

what_was_that()