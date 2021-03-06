# The program should start by asking the user to enter the type of adventure.
# If the type of adventure is "scary" or "short" then the program should display the message "Entering the dark forest!".
# If the type of adventure is "safe" or "long" then the program should display the message "Taking the safe route!".
# Otherwise, in all other cases, the message "Not sure which route to take." should be displayed.

# Ask user for adventure type
print("Please enter the type of adventure")
ad = str(input())

# if adventure chosen is scary or short, then take the dark forest, elseif safe or long, then safe route.

# Check adventure type and display relevant message
if ((ad.lower() == "scary") or (ad.lower() == "short")):
  print("Entering the dark forest!")
elif ((ad.lower() == "safe") or (ad.lower() == "long")):
  print("Taking the safe route!")
else:
  print("Not sure which route to take.")