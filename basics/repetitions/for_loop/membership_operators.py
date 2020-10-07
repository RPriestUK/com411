# We wish to create a program that allows us to display a phrase in reverse.
#
# The program should begin by displaying the message "What phrase do you see?".
# The program should then read in the user's response
# Finally, the program should use a for loop with an appropriate membership operator (IN / NOT IN) to display the phrase in reverse.

# What phrase do you see?
# sucoP sucoH
 
# Reversing...

# The phrase is: Hocus Pocus


print("What phrase do you see?")
p = str(input())

print()
print("Reversing...")
print()

# reverse the phrase
# initialise as empty string
rp = ""
for item in reversed(p):
  rp = rp + item

# display reversed phrase
print("The phrase is: {}".format(rp))
print()