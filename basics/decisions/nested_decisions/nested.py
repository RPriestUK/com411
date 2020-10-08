# The program should start by asking the user to enter the cover type (hard or soft) of the book.
# If the book has a "soft" cover then the program should ask the user if the book is "perfect bound".
# If the answer is "yes" then the message "Soft cover, perfect bound books are very popular!" should be displayed
# otherwise the message "Soft covers with coils or stitches are great for short books" should be displayed.
# Alternatively, if the book has a "hard" cover then the message "Books with hard covers can be more expensive!" should be displayed.

# if soft
  # is perfect? 
    # if yes
      # "Soft cover, perfect bound books are very popular!"
    # elif no
      # "Soft covers with coils or stitches are great for short books"
    # else error
# elif hard
  # "Books with hard covers can be more expensive!"
# else error

# Ask user for cover type
print("What type of cover does the book have, hard or soft?")
covertype = str(input())

# Check type and display relevant message
if (covertype.lower() == "soft"):
  print("Is the cover 'Perfect Bound'?")
  bound = str(input())
  if (bound.lower() == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  elif (bound.lower() == "no"):
    print("Soft covers with coils or stitches are great for short books")
  else:
    print("Error, please answer yes or no.")
elif (covertype.lower() == "hard"):
  print("Books with hard covers can be more expensive!")
else: 
  print("Error, please enter hard or soft cover type.")