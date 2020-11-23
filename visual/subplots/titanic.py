# You should create a program that does the following:
# The program should consist of the following two functions:

# The first function should be named read_data and should have 0 parameters
# The function should read the file visual/subplots/titanic.csv and store its content into a dictionary so that the dictionary contains the following key-value pairs (note that ... means there are more values).
# {
#     'survived':[1, 0, 1, 1, ...],
#     'sex':[male,female,male, ...],
#     'age':[22,38,...],
#     'fare':[7.25,53.1]
# }

# When reading the file, you should ignore any rows with missing values for survived, sex, age or fare.
# You should store the fare as a floating-point number with 2 decimal places.  You can, for example, use the function round to achieve this.
# Finally, the function should return the dictionary.

# The second function should be named run and should have no parameters. 
# The function should start by calling the first function and store the resulting dictionary in a local variable named data.
# The function should then produce 4 subplots using Matplotlib.  Each subplot should show any two of data sets (e.g. age and survived) plotted against one another using a suitable method (e.g. plot).  You are free to pick any visualisation method you wish but they must be appropriate to the data set and the insights you wish to make.

# What interesting observations can be made?

import matplotlib.pyplot as plt
import numpy as np
import csv

def read_data():
  # The function should read the file visual/subplots/titanic.csv and store its content into a dictionary so that the dictionary contains the following key-value pairs
  data = {}
  # Provide application with list of expected data (or blank list)
  listOfValidItems = ['Survived', 'Sex', 'Age', 'Fare'] # accepted data items
  # initialise other variables
  validColumns = []
  headerID = 0
  rowID = 0  

  # read from CSV file, check for valid columns and add the relevant data.
  with open("visual/subplots/titanic.csv") as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    # check each row for data, on first row - create keys, else append data to appropriate key
    for row in csv_reader:
      if (rowID == 0): # add headers
        for header in row:
          # tidy up header value 
          headerName = header.strip()
          # initialise new key with empty list value
          if (headerName in listOfValidItems):
            data[headerName] = [] # adds key to data dictionary
            validColumns.append((headerID, headerName)) # adds tuple to list of valid columns
          # If list is empty, then add all columns
          elif (listOfValidItems == []):
            data[headerName] = [] # adds key to data dictionary
            validColumns.append((headerID, headerName)) # adds tuple to list of valid columns
          else:
            pass #ignore
          headerID += 1
      else:
        # loop through columns to add values to each key
        columnID = 0
        skipRow = 0
        for item in row:
          # check for invalid (blank) data before processing
          if (item is None):
            skipRow += 1
          if (skipRow == 0):
            # loop through each validColumn to retrieve column referencing
            for index in range(0, len(validColumns), 1):
              # Retrieve each column from validColumns for each index location
              validColumn = validColumns[index]
              # Check current column matches valid column and use tuple matching relevant key in data dictionary
              if (validColumn[0] == columnID):
                for key in data:
                  # if key name matches column name, add data to key
                  if (key == validColumn[1]):
                      data[key].append(item.strip())
          columnID += 1
      rowID += 1
    csvFile.close() # Closes file to prevent locking and performance issues. 
  return data

def run():
  # The function should start by calling the first function and storing the resulting dictionary in a local variable named data.
  data = read_data()

  # initialise vars for dynamic plot creation according to number of keys
  #plot = 0
  numberOfPlots = len(data)

  # The function should then produce 4 subplots using Matplotlib. Each subplot should show any two of data sets (e.g. age and survived) plotted against one another using a suitable method (e.g. plot).  You are free to pick any visualisation method you wish but they must be appropriate to the data set and the insights you wish to make.
  fig, axs = plt.subplots(numberOfPlots, 1) # (rows, cols, params)
  fig.suptitle('Titanic Passenger Data')

  # loop through keys in dictionary (data) and create graph with labels
  #for key in data:
  #  axs[plot].plot(data[key])
  #  axs[plot].set_xlabel('Type')
  #  axs[plot].set_ylabel('Number')
  #  axs[plot].set_title(key)
  #  plot += 1

  # age vs. survived - bar - m/f-sur // m/f-notsur
  axs[0].scatter(data['Age'], data['Age']) 
  axs[0].plot(data['Survived']) 
  axs[0].set_ylabel('Age')
  axs[0].set_xlabel('Number')
  axs[0].set_title('Survival by Age')

  # age vs. survived
  #axs[1].plot(dataAge, dataSurvived) 
  #axs[1].set_xlabel('Survived')
  #axs[1].set_ylabel('Sex')
  #axs[1].set_title('Survival per Age')

  # fare vs. survived


  # all in one chart


  plt.tight_layout() # makes sure the subplots don't overlap
  plt.show() # Displays the graphs

run()