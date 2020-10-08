# Beep's program should first ask the user to enter a sequence of characters consisting of dashes and two markers e.g. "X----X".
# The program should then ask the user to enter a character representing the marker e.g. X.
# The program should then count the number of dashes between the two markers.
# Finally, the program should print the total number of characters between the markers.

# Some example runs of the program are shown below:

# Please enter a sequence
# x---x

# Please enter the character for the marker
# x
 
# The distance between the markers is 3.



# Ask user for sequence of characters
print("Please enter a sequence")
s = str(input())
print() 

# Ask user for marker character
print("Please enter the character for the marker")
m = str(input())
print()

# Initialise distance and marker variables
d = 0
m1 = -1 # Starts negative in case first marker is at position 0
m2 = -1 # Starts negative in case first marker is at position 0

# Loop through positions to find the markers
for spos in range(0, len(s), 1):
  l = s[spos]

  # Check if the character matches the marker set by user
  if (l == m):
    if (m1 == -1): # If first marker hasn't updated, then this is the first marker
        m1 = spos
    else:
      m2 = spos

# Work out distance between markers, and remove second marker's character location from the sum
d = (m2 - m1) - 1

# Display result
print("The distance between the markers is {}".format(d))