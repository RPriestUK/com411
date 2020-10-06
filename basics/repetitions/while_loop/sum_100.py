# The program should start by displaying the message "Calculating the sum of the first 100 numbers...".
# The program should then use a while loop to calculate the sum of the first 100 numbers from 1 to 100 (inclusive). Finally, the program should display the message "...Done! The answer is" followed by the answer.

print("Calculating the sum of the first 100 numbers...")

# initialise both iteration and result
i = 0
result = 0

while (i < 101):
  # add iteration to result
  result = result + i
  i = i + 1
  
print("...Done! The answer is {}".format(result))