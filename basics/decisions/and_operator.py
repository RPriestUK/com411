# The program should start by displaying the message "What did I hear?"
# The program should then read the user's response
# The program should then display the message "What did I see?"
# The program should then read the user's response
# The program should then do the following:
#     If the user entered "grrr" and "two red eyes" then program should display the             message "There is a scary creature. I should get out of here!".
#     Otherwise the program should display the message "I am a little scared but I will         continue."

# Ask user what they heard
print("What did I hear?")
heard = str(input())

# Ask user what they saw
print("What did I see?")
saw = str(input())

# Check both conditions are true, else continue message
if ((heard.lower() == "grr") and (saw.lower() == "two red eyes")):
  print("There is a scary creature. I should get out of here!")
else: 
  print("I am a little scared but I will continue.")