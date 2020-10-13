# We wish to create a program to play a game of "Guess the Number".
# The program should use the module random.
# The program should start by displaying the message "Please enter the minimum value:"
# The program should then read in the user's number.
# The program should then display the message "Please enter the maximum value:"
# The program should then read in the user's number.
# The program should then generate and store a random number between the minimum and maximum value specified by the user.
# The program should then display the message "I am thinking of a number between {min} and {max}.  Can you guess what it is?" where {min} and {max}are the minimum and maximum values specified by the user.
# The program should then do the following repeatedly until the user guesses the correct answer:
#    read in the user's guess
#    if the guess is too low then display the message "Your guess is too low."
#    otherwise if the guess is too high then display the message "Your guess is too high."
#    In any case, display the message "Try again:".
#The program should display the following message once the user guessed the correct number: "Congratulations! You guessed my number!".
# Once you have the above program working as intended, you should turn it into a user-defined function name play_guess_the_number and call the function appropriately.

import random as rnd

def play_guess_the_number():
 
  def guess_check(randomnumber, guessednumber):
    if (guessednumber == randomnumber):
      result = print("\nCongratulations! You guessed my number!\n")
    elif (guessednumber > randomnumber):
      result = print("Your guess is too high.")
      ask_for_next_guess()
    elif (guessednumber < randomnumber):
      result = print("Your guess is too low.")
      ask_for_next_guess()
    return result

  def ask_for_next_guess():
    print("\nPlease try again:")
    guess = int(input())
    guess_check(ranv, guess)

  def get_min_value():
    # Ask user for minimum number
    print("\nPlease enter the minimum value:")
    minvalue = int(input())
    return minvalue

  def get_max_value():
    # Ask user for minimum number
    print("\nPlease enter the maximum value:")
    maxvalue = int(input())
    return maxvalue
    
  def choose_random_number(minv, maxv):
    # Create random number for user to guess
    return rnd.randrange(minv, maxv, 1)
 
  # initialise variables
  minv = 0
  maxv = 0
  ranv = 0

  # Set variables to user inputted numbers and work out random number
  minv = get_min_value()
  maxv = get_max_value()   

  # Check that the maximum value is greater than the minimum value
  while (minv >= maxv):
      print("\n* Please choose a maximum value larger than the minimum value. *")
      maxv = get_max_value()
  
  # Assign random number to variable using min/max entered by user
  ranv = choose_random_number(minv, maxv)
  
  # Ask user to guess the random number
  print("\nI am thinking of a number between {} and {}. Can you guess what it is?".format(minv, maxv))
  guessednumber = int(input())

  # Check entered value against random number 
  guess_check(ranv, guessednumber)

play_guess_the_number()