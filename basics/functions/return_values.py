# Bop is trying to distribute their weight so that both Beep and Bop can reach the top of the bridge ladder quicker. A program to help Bop achieve this consists of three functions as follows:

# The first function should be named sum_weights and should have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the total weight.

# The second function should be named calc_avg_weight and should also have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the average weight of the bots. It should do this by calling the first function and using the return value.

# The third function should be named run and should have 0 parameters. The function should prompt the user to enter the weight for each bot. The function should then prompt the user to enter either the word "sum" or "average". If the user types in "sum" then this function should display the total age as given by the first function ( sum_weights"). Otherwise if the user types in "average" then this function should display the average weight as given by the second function ( calc_avg_weight).

# The program should also contain a single call to your run function at the end of your program that looks as follows:

# Run the program
# run()


# Function to calculate and return the total weight.
def sum_weights(beepweight, bopweight):
  total = beepweight + bopweight
  return total

# Function to calculate and return the average weight of the bots. It should do this by calling the first function and using the return value.
def calc_avg_weight(beepweight, bopweight):
  avg = sum_weights(beepweight, bopweight) / 2
  return avg

# Function should prompt the user to enter the weight for each bot, 
# then prompt the user to enter either the word "sum" or "average".
# If the user enters "sum" then display result of sum_weights, if the user types in "average" then display the result of calc_avg_weight.
def run():
  print("Please enter the weight of Beep")
  beepweight = int(input())
  print("Please enter the weight of Bop")
  bopweight = int(input())

  print("Would you like the sum or average of the weights?")
  choice = str(input())

  # If user has entered 'sum' then provide sum, if 'average' provide average, else error.
  if (choice.lower() == "sum"):
    print("The sum of Beep and Bop's weight is {}".format(sum_weights(beepweight, bopweight)))
  elif (choice.lower() == "average"):
    print("The average of Beep and Bop's weight is {}".format(calc_avg_weight(beepweight, bopweight)))
  else: 
    print("Please choose 'sum' or 'average' when trying again.")

# Call function 'run'
run()