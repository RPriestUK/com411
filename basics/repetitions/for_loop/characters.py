# We wish to create a program that allows us to display a word character by character.

# The program should begin by displaying the message "What strange markings do you see?".
# The program should then read in the user's response
# Finally, the program should use a for loop to display each character in the user's reponse along with its index position on a new line.

print("What strange markings do you see?")
m = str(input())
print() 
print("Identifying...")
print()
for letter in range(0, len(m), 1):
  print("Index {}: {}".format(letter, m[letter]))
print() 
print("Done!")