# The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally, the program should display the number of even numbers and odd numbers entered.

# - Initialise vars
# - Number of inputs to request from user
numcount = 3
# - Number of odds or evens counted
evencount = 0
oddcount = 0
# - Array of numbers entered
numsentered = []
# - Iterations for while loop
i = 0
# - Array of even numbers gathered
evennums = []
# - Array of odd numbers gathered
oddnums = []

# Ask user for first number
print("I would like to check {} numbers to count the number of odd and even numbers.".format(numcount))

# Add each entered number to numsentered array 
while (i < numcount):
  if (i < 1):
    qnum = "first"
  elif (i >= 1):
    qnum = "another"
  print("Please enter {} number:".format(qnum))
  numsentered.append(int(input()))
  i = i + 1 

# Check each number if odd or even
for num in numsentered:
  if (num % 2 != 0):
    oddnums.append(num)
  else: 
    evennums.append(num)

# - Count number of odds and evens
evencount = len(evennums)
oddcount = len(oddnums)

# Display results
print("In the numbers you have entered, {} are even ({}) and {} are odd ({}).".format(evencount, evennums, oddcount, oddnums))