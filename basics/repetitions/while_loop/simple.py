# The program should start by displaying the message "How many cables should I remove?".
# The program should then read in the user's response.
# The program should then create a variable to track the number of removed cables and set this to 0.
# The program should then use a while loop to do the following:
#    Display the message "Removed cable."
#    Increment the variable for tracking the number of removed cables

print("How many cables should I remove?")
n = int(input())

# number of cables removed
i = 0

# Loop through cables to remove
while (i < n):
  print("Removed cable.")
  i = i + 1
