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
import csv

def read_data():
  # as data input is fixed, we can specify the keys when creating the dictionary, rather than gather dynamically
  data = {'survived':[], 'sex':[], 'age':[], 'fare':[]}

  # open file and process into each key
  with open('visual/subplots/titanic.csv') as file:
    csv_reader = csv.reader(file)

    # ignore header row by skipping 
    header = next(csv_reader)

    for line in csv_reader:
      # extract required values using appropriate indexes
      survived = line[1].strip()
      sex = line[4].strip()
      age = line[5].strip()
      fare = line[9].strip()  

      # only add the data to the dictionary if not empty
      if (survived != "" and sex != "" and age != "" and fare != ""):
        data['survived'].append(bool(int(survived)))

        # split data according to gender
        if (sex == 'male'): 
          data['sex'].append('male')
        else:
          data['sex'].append('female')
        
        # convert numerical data to floats and round to 2 dp where required
        data['age'].append(float(age))
        data['fare'].append(round(float(fare), 2))

  return data

def plot_age_vs_survival(ax, data):
  # create dictionaries for each age group
  children = {'survived':[], 'deceased':[]} # < 18
  adults = {'survived':[], 'deceased':[]} # 18 -> 65
  elderly = {'survived':[], 'deceased':[]} # 65+

  # populate each dictionary
  for index in range(len(data['age'])):
    age = data['age'][index]
    survived = data['survived'][index]

    # add to relevant dictionary according to age and survival
    if (age < 18 and survived):
      children['survived'].append(age)
    elif (age < 18 and not survived):
      children['deceased'].append(age)
    elif (age < 65 and survived):
      adults['survived'].append(age)
    elif (age < 65 and not survived):
      adults['deceased'].append(age)
    elif (survived == True):
      elderly['survived'].append(age)
    else:
      elderly['deceased'].append(age)
  
  # prepare labels and totals
  labels = ['children', 'adults', 'elderly']
  survivors = [len(children['survived']), len(adults['survived']), len(elderly['survived'])]
  deceased = [len(children['deceased']), len(adults['deceased']), len(elderly['deceased'])]

  # display suitable bar plots
  ax.bar(labels, survivors, label='Survived')
  ax.bar(labels, deceased, bottom=survivors, label='Deceased') # labels, total, y coordinates of bar base
  ax.set_ylabel('age')
  ax.legend() # adds legend for survived/deceased on bar
  ax.set_title('Age vs Survival')


def plot_fare_vs_survival(ax, data):
  survived = []
  deceased = []

  for index in range(len(data['fare'])):
    fare = data['fare'][index]
    # append survival boolean to relevant list. 
    if (data['survived'][index]):
      survived.append(fare)
    else:
      deceased.append(fare)
  
  ax.scatter(range(len(survived)), survived, label='Survived')
  ax.scatter(range(len(deceased)), deceased, label='Deceased')
  ax.set_ylabel('fare')
  ax.legend()
  ax.set_title('Fare vs Survival')

def plot_sex_vs_survival(ax, data):
  males = {'survived':[], 'deceased':[]}
  females = {'survived':[], 'deceased':[]}

  for index in range(len(data['sex'])):
    sex = data['sex'][index]
    if (sex == 'male' and data['survived'][index]):
      males['survived'].append(sex)
    elif (sex == 'male' and not data['survived'][index]):
      males['deceased'].append(sex)
    elif (sex == 'female' and data['survived'][index]):
      females['survived'].append(sex)
    else:
      females['deceased'].append(sex)
  
  labels = ['male', 'female']
  survivors = [len(males['survived']), len(females['survived'])]
  deceased = [len(males['deceased']), len(females['deceased'])]

  ax.bar(labels, survivors, label='Survived')
  ax.bar(labels, deceased, bottom=survivors, label='Deceased')
  ax.set_ylabel('passengers')
  ax.legend()
  ax.set_title('Sex vs Survival')


def plot_all_vs_survival(ax, data):
  children = {
    'male': {'survived':[], 'deceased':[]},
    'female': {'survived':[], 'deceased':[]}
  }

  adults = {
    'male': {'survived':[], 'deceased':[]},
    'female': {'survived':[], 'deceased':[]}
  }

  elderly = {
    'male': {'survived':[], 'deceased':[]},
    'female': {'survived':[], 'deceased':[]}
  }

  for index in range(len(data['age'])):
    age = data['age'][index]

    # children
    if (age < 18):
      if (data['sex'][index] == 'male' and data['survived'][index]):
        children['male']['survived'].append(age)
      elif (data['sex'][index] == 'male' and not data['survived'][index]):
        children['male']['deceased'].append(age)
      elif (data['sex'][index] == 'female' and data['survived'][index]):
        children['female']['survived'].append(age)
      elif (data['sex'][index] == 'female' and not data['survived'][index]):
        children['female']['deceased'].append(age)

    # adults
    elif (age < 65):
      if (data['sex'][index] == 'male' and data['survived'][index]):
        adults['male']['survived'].append(age)
      elif (data['sex'][index] == 'male' and not data['survived'][index]):
        adults['male']['deceased'].append(age)
      elif (data['sex'][index] == 'female' and data['survived'][index]):
        adults['female']['survived'].append(age)
      elif (data['sex'][index] == 'female' and not data['survived'][index]):
        adults['female']['deceased'].append(age)

    # elderly
    else:
      if (data['sex'][index] == 'male' and data['survived'][index]):
        elderly['male']['survived'].append(age)
      elif (data['sex'][index] == 'male' and not data['survived'][index]):
        elderly['male']['deceased'].append(age)
      elif (data['sex'][index] == 'female' and data['survived'][index]):
        elderly['female']['survived'].append(age)
      elif (data['sex'][index] == 'female' and not data['survived'][index]):
        elderly['female']['deceased'].append(age)

  x_labels = ['children', 'adults', 'elderly']
  male_survivors = [len(children['male']['survived']), len(adults['male']['survived']), len(elderly['male']['survived'])]
  female_survivors = [len(children['female']['survived']), len(adults['female']['survived']), len(elderly['female']['survived'])]

  ax.plot(x_labels, male_survivors, label='Male Survivors')
  ax.plot(x_labels, female_survivors, label='Female Survivors')
  ax.set_title('Age, Sex vs Survival')
  ax.legend()
  ax.set_title('Fare vs Survival')


def run():
  data = read_data()

  # plots arranged in a 2 by 2 grid
  fig, axs = plt.subplots(2, 2)

  # display plots with fixed locations on axs
  plot_age_vs_survival(axs[0, 0], data)
  plot_fare_vs_survival(axs[0, 1], data)
  plot_sex_vs_survival(axs[1, 0], data)
  plot_all_vs_survival(axs[1, 1], data)
  
  plt.tight_layout() # makes sure the subplots don't overlap
  plt.show() # Displays the graphs

run()