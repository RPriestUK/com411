# The program should display the message "Please enter a phrase:".
# The program should then read in the user's response.
# The program should then dispaly the word "Bop" repeatedly x number of times where x is the number of characters in the phrase entered by the user.
# For example, if the user enters "Hello", the computer will print "Bop" five times since there are five characters in the phrase "Hello".

print("Please enter a phrase:")
p = str(input())

# initialise iterations
i = 0

# while i is less than length of p, go Bop. 
while (i < len(p)):
  print("Bop ", end="")
  i = i + 1