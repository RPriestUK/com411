# The program should start by displaying the message "How many live cables must I avoid?".
# The program should then read in the user's response.
# The program should then create a variable to track the number of live cables and set this to 0.
# The program should then use a while loop to do the following:
#    Display the message "Avoiding..." at the start of each iteration
#    Increment the variable for tracking the number of live cables
#    Display the message "...Done! [n] live cable avoided!" at the end of each iteration where [n] should be replaced by the current number of live cables.
# Finally, the program should display the message "All live cables have been avoided."

print("How many live cables must I avoid?")
n = int(input())

# live cables int initialised
lc = 0

# Loop while lc is less than number entered
while (lc < n):
  print("Avoiding...", end = "")
  lc = lc + 1
  print("Done! {} live cable avoided!".format(lc))

print("All live cables have been avoided.")