# The program should start by displaying the message "How many numbers should I sum up?".
# The program should then retrieve the user's response.
# The program should then use a while loop to repeatedly prompt the user for a number.  The specified number should be added to a running total.
# Finally, the program should display the message "The answer is" followed by the answer.

print("How many numbers should I sum up?")
n = int(input())
print()

# initialise interation and total
i = 0
total = 0

while (i < n):
  # increment iteration
  i = i + 1
  # ask user for next number
  print("Please enter number {} of {}:".format(i,n))
  numentered = int(input())
  # add number entered to total
  total = total + numentered

#display total
print("The answer is {}".format(total))