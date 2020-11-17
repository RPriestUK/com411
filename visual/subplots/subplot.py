# You are now required to develop a program to process the file.
# The program should consist of the following two functions:

# The first function should be named read_data and should take 1 parameter that represents a file path and name.
# The function should start by opening the specified file in read mode.
# The function should then read each line in the file and store it into a list.
# The function should then close the file if it is not automatically closed.
# Finally, the function should return the list of values.
# The second function should be named run and should take 0 parameters.
# The function should start by calling the first function with the file path and name visual/subplots/temps.txt and assign the resulting list of values to a local variable named data.
# The function should then display the list of values named data in a Matplotlib graph consisting of two subplots placed horizontally.  The first subplot should show the data as a line graph and the second subplot should show the data as a bar chart.
 
# Code your solution and be sure to include appropriate comments in your code.

import matplotlib.pyplot as plt
import csv  

def read_data(filepathname):
  # The function should start by opening the specified file in read mode.  
  data = []
  # The function should then read each line in the file and store it into a list.
  with open(filepathname, "r") as file:
    lines = file.readlines()
    for line in lines:
      data.append(line)
  # The function should then close the file if it is not automatically closed.
    file.close()
  # Finally, the function should return the list of values.
  return data

def run():
  # The function should start by calling the first function with the file path and name visual/subplots/temps.txt and assign the resulting list of values to a local variable named data.
  data = (read_data("visual/subplots/temps.txt"))
  print(data)
  # The function should then display the list of values named data in a Matplotlib graph consisting of two subplots placed horizontally.  
  fig, axs = plt.subplots(1,2)
  # The first subplot should show the data as a line graph and the second subplot should show the data as a bar chart.
  axs[0].plot(data)
  axs[1].bar(data, height=1)

  plt.tight_layout() # makes sure the subplots don't overlap
  plt.show() # Displays the graphs

run()