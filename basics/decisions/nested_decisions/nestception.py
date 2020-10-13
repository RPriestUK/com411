# The program should start by displaying the message "Where should I look?"
# The program should then read the user's response
# The program should then do the following:

# - If the user enters "in the bedroom" then the program should display the message "Where in the bedroom should I look?".
#         If the user enters "under the bed" then the program should respond with "Found              some shoes but no battery"
#         otherwise it should respond with "Found some mess but no battery."

# - If the user enters "in the bathroom" then the program should display the message "Where in the bathroom should I look?". 
#         If the user enters "in the bathtub"the program should respond with "Found a rubber duck but no battery"
#         otherwise it should respond with "Found a wet surface but no battery."

# - If the user enters "in the lab" the program should display the message "Where in the        lab should I look?". 
#         If the user enters "on the table" the program should respond with "Yes! I found             my battery!"
#         otherwise it should respond with "Found some tools but no battery."

# - If the user enters anything other than the above then the message "I do not know where that is but I will keep looking." should be displayed.

# Initialise variables
lookplace = ""
lookroom = ""

# Ask user where to look
print("Where should I look?")
lookroom = str(input())

# Check where to look and display relevant message/follow up question
# Check bedroom if relevant
if (lookroom.lower() == "in the bedroom"):
  print("Where in the bedroom should I look?")
  lookplace = str(input())
  if (lookplace == "under the bed"):
    print("Found some shoes but no battery")
  else: 
    print("Found some mess but no battery.")

# Check bathroom if relevant
elif (lookroom.lower() == "in the bathroom"): 
  print("Where in the bathroom should I look?")
  lookplace = str(input())
  if (lookplace == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else: 
    print("Found a wet surface but no battery.")

# Check lab if relevant
elif (lookroom.lower() == "in the lab"): 
  print("Where in the lab should I look?")
  lookplace = str(input())
  if (lookplace == "on the table"):
    print("Yes! I found my battery!")
  else: 
    print("Found some tools but no battery.")

# Else error message
else: 
  print("I do not know where that is but I will keep looking.")