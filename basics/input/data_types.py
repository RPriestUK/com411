# Ask user what their name is as a string
print("What is your name, human?")
name = input(str())

# Ask user what their age is as a whole number
print("How old are you, in years?")
age = input(int())

# Ask user what their height is as a decimal (float)
print("How tall are you, in metres?")
height = input(float())

# Ask user what their weight is as a whole number
print("How much do you weigh, to the nearest kilogram?")
weight = input(int())

# Calculate BMI weight divided by height squared to 2 decimal places
bmi = weight / (height ** 2)

# Display details back to user
print(name + "you are" + age + "years old, and your BMI is" + bmi)