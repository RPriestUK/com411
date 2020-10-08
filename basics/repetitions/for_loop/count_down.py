# We wish to create a program that counts down the distance (in number of steps) to the cave.

# The program should begin by displaying the message "How far are we from the cave?".
# The program should then read in the user's response (a distance)
# Finally, the program should use a for loop to display the number of steps remaining.

# Ask user the number of steps to cave
print("How far are we from the cave?")
n = int(input())
print()

# Loop through number of steps to cave
for count in range(n, 0, -1):
  print("{} steps remaining".format(n))
  n = n - 1