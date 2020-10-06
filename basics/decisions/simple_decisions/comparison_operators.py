# The program should start by prompting the user to enter the first number.
# The program should then read in the user’s first number.
# The program should then prompt the user to enter thesecond number.
# The program should then read in the user’s second number.
# The program should then decide which of the two numbers is the smallest and display the message "The first number is the smallest!" if the first number is smaller, "The second number is the smallest!" if the second number is smaller or "Both are equal!" if both numbers are equal in value.

print("Please enter a number:")
num1 = int(input())

print("Please enter a second number:")
num2 = int(input())

if (num1 > num2):
  print("Your first number ({}) is the largest.".format(num1))
elif (num1 < num2):
  print("Your second number ({}) is the largest.".format(num2))
