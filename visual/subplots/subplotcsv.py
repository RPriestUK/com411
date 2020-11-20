# You should now create the program that does the following:
# The program should consist of the following two functions:

# The first function should be named read_data and should have 0 parameters
# The function should read the file visual/subplots/temps.csv and store its contents into a dictionary so that the dictionary contains the following key-value pairs:
# {
#     'week1':[12, 14, 16, 15, 17, 16, 17],
#     'week2':[18, 21, 20, 21, 23, 17, 16]
# }

# Finally, the function should return the dictionary.
# The second function should be named run and should have no parameters. 
# The function should start by calling the first function and storing the resulting dictionary in a local variable named data.
# The function should then display the values using Matplotlib such that the resulting Figure consists of 2 subplots arranged vertically and sharing the same x-axis.  The first subplot should show a plot for week1 and the second subplot should show a plot for week2.
# Code your solution and be sure to include appropriate comments in your code.

import matplotlib.pyplot as plt
import csv

def read_data(): 
  # The function should read the file visual/subplots/temps.csv and store its contents into a dictionary 
  
  # initialise vars
  data = {}
  rowid = 0

  with open("visual/subplots/temps.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # check each row for data, on first row - create keys, else append data to appropriate key
    for row in csv_reader:
      if rowid == 0:
        for item in row:
          # initialise new key with empty list value
          data[item.strip()] = []
      else:
        # loop through columns to add values to each key
        for key in data:
          columnid = 0
          data[key].append(row[columnid].strip())
          columnid += 1
      rowid += 1
    csvfile.close()
  return data

def run():
  # The function should start by calling the first function and storing the resulting dictionary in a local variable named data.
  data = read_data()

  # initialise vars for dynamic plot creation according to number of keys
  plot = 0
  numberofplots = len(data)

  # Initialise figure settings
  # Display the values using Matplotlib such that the resulting Figure consists of 2 subplots arranged vertically and sharing the same x-axis.  The first subplot should show a plot for week1 and the second subplot should show a plot for week2.
  fig, axs = plt.subplots(numberofplots, 1, sharex=True) # (rows, cols, params)
  fig.suptitle('Temperature per week')

  # loop through keys in dictionary (data) and create graph with labels
  for key in data:
    axs[plot].plot(data[key])
    axs[plot].set_xlabel('Day')
    axs[plot].set_ylabel('Temp')
    axs[plot].set_title(key)
    plot += 1

  plt.tight_layout() # makes sure the subplots don't overlap
  plt.show() # Displays the graphs

run()