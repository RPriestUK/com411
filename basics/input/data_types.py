# Ask user what their name is as a string
print("What is your name, human?")
name = str(input())

# Ask user what their age is as a whole number
print("How old are you, in years?")
age = int(input())

# Ask user what their height is as a decimal (float)
print("How tall are you, in metres?")
height = float(input())

# Ask user what their weight is as a whole number
print("How much do you weigh, to the nearest kilogram?")
weight = int(input())

# Calculate BMI weight divided by height squared to 2 decimal places
bmi = round(weight / (height ** 2), 2)

# Display details back to user
print(name, "you are", age, "years old, and your BMI is", bmi)
