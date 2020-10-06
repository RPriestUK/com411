# The program should begin by displaying the message "How many mountains should I display?".
# The program should then read in the user's response
# Finally, the program should use a for loop to display the specified number of ASCII mountains.

print("How many mountains should I display?")
n = int(input())

print("Displaying...")

for count in range(0, n, 1):
  print("      __        ")
  print("     /  \_      ")
  print("    /^    \     ")
  print("   /  ^    \_   ")
  print(" _/ ^ ^     ^\  ")
  print("/  ^     ^    \ ")