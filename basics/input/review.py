# Create a small text based game which requires input from the user for initial settings, then performs tasks against the entered data to create an interactive scenario.

print("""
###########################
#       Welcome to        #
#     Chat with Beep!     #
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

# Ask user their name
print("What is your name?")
name = str(input())
print()
print("Pleased to meet you,", name + "!")
print()

# Ask user for user's age
print("How old are you,", name + "?")
userage = int(input())
beepage = int(324)
print()
print(str(userage) + "! That's a good age. I'm", str(beepage) + "!")

# Perform a calculation on the age difference
agediff = beepage - userage
agetimes = beepage / userage

# Display the calculations
print()
print("That means I'm", str(agediff), "years, or", str(agetimes), "times older than you!") 
print()

# Ask user about hobbies
print("Do you have any hobbies,", name, "?") 
hobby = str(input())
print() 

print("Hold on, I'm very old and couldn't quite read that, I need to put on my glasses. One moment...")
print() 

leftglass = "\Ὅ-"
rightglass = "-Ὅ/"

print("   ###########")
print("# # (" + leftglass + "/" + rightglass + ") # #")
print("# #      /    # #")
print("   ###########")
print() 
print("How do I look?")
print() 

print("Oh wow! I like", hobby, "too!")

print() 
print("Nice meeting you,", name + ". Have a good day and see you again soon!")