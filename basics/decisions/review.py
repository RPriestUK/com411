# We wish to create a program that demonstrates the following functionality:
# - Decisions with if...elif...else statements
# - Nested decisions
# - Multiple conditions with logical (AND, OR and NOT) operators

print("""
###########################
#       Welcome to        #
#   Chat with Beep v2!    #
#                         #
#       Created by        #
#     Richard Priest      #
#                         #
###########################""")
print() 
print("Hi, I'm Beep!")

# Display a picture of Beep the robot
print("\n")
print("   ###########")
print("# # (O  /  O) # #")
print("# #      /    # #")
print("   ###########")
print("\t  #####")
print("   ###########")
print("  #  # --- #  #")
print(" #   #o..  #   #")
print(" #   #     #   #")
print("  #  #     #  #")
print("   ###########")
print("\n")

print("Would you like to help me put my Lego bricks away?")
help = str(input())

if (help.lower() == "yes"):
  print("That's great, thank you!")
  print()
  # List colours to choose from
  print("Let's see, there's a lot here, we have different colours...")
  print()
  print("""Red Bricks
Yellow Bricks
Green Bricks
Blue Bricks
White Bricks""") 
  print()

  # Ask user for colour
  print("Which colour bricks shall we sort first?")
  colour = str(input())

  # colour chosen, next actions dependent on volume and shape according to the colour.
  if ((colour == "yellow") or (colour == "white")):
    # not many of either
    print()
    print("We'll need a small tub for those, there are only a few {} ones.".format(colour))
    print("1...") 
    print("2...") 
    print("3...") 
    print("All sorted, thank you!") 

  elif (colour == "red"):
    # lots, sort further by size, ask user.
    print()
    print("""Wow, there's a lot of those, we'll have to sort by size.
Shall we pick large or small {} bricks?""".format(colour))
    size = str(input())
    # Ask user for number
    print()
    print("And how many {} ones can you find?".format(size))
    number = int(input())
    
    # check for large and number larger than (or equal to) 6, or small ones
    if ((size.lower() == "large") and (number <= 6)):
      print()
      print("Phew, these are big!")
    elif ((size.lower() == "small")):
      print()
      print("This is easy peasy!")
    else:
      print()
      print("These aren't easy to sort, are they?")  

  elif (colour == "green"):
    # lots, sort further by shapes listed
    print()
    print("Ooh, these {} ones have lots of different shapes...".format(colour))
    print()
    print("""Rectangle
Square
Round""") 
    print()
    # Ask user for shape
    print("Can you choose the shape, please?")
    shape = str(input())
    print()
    if (shape.lower() == "rectangle"):
      print("Awesome, thanks, can you tell me how many {}s you can find?".format(shape))
      number = int(input())
      print("Wow, {}! I didn't realise there were so many! Lets count them...".format(number))
      if (number < 10):
        print(" █ " * number)
      else:
        print("--- SYSTEM BUSY ---")

    elif (shape.lower() == "square"):
      print("Let me sort those for you...")
      print()
      print("--- SYSTEM BUSY ---")

    elif (shape.lower() == "round"):
      print("I like {} ones, let me sort those for you...".format(shape))
      print()
      print("--- SYSTEM BUSY ---")   

    else:
      print("Ok, I'll sort them by weight instead.")
      print()
      print("--- SYSTEM BUSY ---")   

  elif (colour.lower() == "blue"):
    # not many, describe favourite
    print("There isn't many of these, I like the square ones.")

elif (help.lower() == "no"):
  print()
  print("Oh, Ok, I'll do it on my own.")
  print()
  print("--- SYSTEM BUSY ---")

elif (help.lower() == "later"):
  print()
  print("""Thank you, will wait until you've finished what you're doing.
  
  --- INITIATED SINGING SEQUENCE ---

  La la la LAAAA la.""")

else:
  print()
  print("""I'll think I'll ask someone else, thanks anyway!
  
  --- FLIGHT MODE ENGAGED ---""")