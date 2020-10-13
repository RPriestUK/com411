# We wish to create a program that adjusts the light level of Beep and Bop's night vision.

# The program should begin by displaying the message "What level of brightness is required?".
# The program should then read in the user's response (an even number representing the brightness level)
# The program should then use the user's response to generate a range of even numbers between 2 and the number entered by the user.
# Finally, the range should be used to control a for loop that displays asterix symbols to represent the current light level.

# Ask user for brightness level
print("What level of brightness is required?")
n = int(input())

# check user has entered an even number
if (n % 2 != 0):
  print("Sorry, {} is an odd number, please enter an even number.".format(n))
else:
  print("\nAdjusting brightness...")
  print()

  for count in range(2, (n + 2), 2):
    # create ASCII icons numbered by count
    b = "*" * count
    print("Beep's brightness level: {}".format(b))
    print("Bop's brightness level: {}".format(b))
  print("Adjustment Complete.")