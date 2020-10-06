# We wish to create a program to help Bop calculate the factorial of a specified number.

# The program should start by displaying the message "Please enter a number:".
# The program should then use a while loop to calculate the factorial of the specified number.
# Finally, the program should display the message "The factorial is" followed by the answer.

# successively multiplying a variable initialized to 1 by the integers up to n (if any) will compute n!

print("Please enter a number:")
n = int(input())

i = 0
total = 0

while (i < n):
  i = i + 1
  # cannot multiply by 0, so total = 1 on first iteration
  if (total < 1):
    total = 1
  else:
    total = total * i

print("The factorial is {}".format(total))