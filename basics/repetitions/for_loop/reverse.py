# We wish to create a program that allows us to display a phrase in reverse.

# The program should begin by displaying the message "What phrase do you see?".
# The program should then read in the user's response
# Finally, the program should use a for loop to display the phrase in reverse.

#ask user for phrase
print("What phrase do you see?")
p = str(input())

print()
print("Reversing...")
print()

# reverse the phrase
# initialise as empty string
rp = ""
for letter in range(len(p),0,-1):
  rp = rp + p[letter-1]

# display reversed phrase
print("The phrase is: {}".format(rp))