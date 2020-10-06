# Towards which direction should I paint (up, down, left or right)?
# input = up

# I am painting in the upward direction!

# Ask user for direction
print("Which direction should I move the paintbrush; up, down, left or right?")
activity = str(input())

# initilise direction variable
direction = ""

# If to determine direction entered
if (activity == "up"):
  direction = "upward"
  print("Ok, I'm painting {}.".format(direction))
elif (activity == "down"):
  direction = "downward"
  print("Ok, I'm painting {}.".format(direction))
elif (activity == "left"):
  direction = "left"
  print("Ok, I'm painting {}.".format(direction))
elif (activity == "right"):
  direction = "right"
  print("Ok, I'm painting {}.".format(direction))
else:
  print("Not sure I understand, sorry!")

