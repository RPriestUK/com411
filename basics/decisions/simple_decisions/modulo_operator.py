# Please enter a whole number.
# input: number

# The number '' is an odd number.


# Ask the user for a whole number
print("Please enter a whole number:")
number = int(input())

# check number for remainder after dividing by 2 (using '% 2'), if there is a  remainder, then it's an odd number, else it's an even number
if (number % 2 != 0):
  print("The number {} is an odd number.".format(number))
else:
  print("The number {} is an even number.".format(number))

