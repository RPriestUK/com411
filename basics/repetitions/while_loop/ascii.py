# The program should start by displaying the message "How many bars should be charged?".
# The program should then read in the user's response.
# The program should then create a variable to track the number of bars charged and set this to 0.
# The program should then use a while loop to do the following:
#    Display the message "Charging:".
#    Increment the variable for tracking the number of charged bars.
#    Display the number of charged bars.
# Finally, the program should display the message "The battery is fully charged."

print("How many bars should be charged?")
n = int(input())

# Initialise level of charge
lc = 0

# loop while level of charge is less than number entered
while (lc < n):
  print()
  print("Charging:", end = "")
  lc = lc + 1
  # display an ascii icon for battery level for each level of charge
  print(" █ " * lc)
print()
print("The battery is fully charged.")