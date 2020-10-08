# We wish to create a program that allows us to display a grid of ASCII emoji.

# The program should start by asking the user how many rows and columns they would like.
# The program should then display a grid of ascii emoji where the size of grid matches the number of rows and columns specified by the user.


# An example run of such a program is shown below:

# How many rows should I have?
# 2

# How many columns should I have?
# 3
 
# Here I go:

# :-) :-) :-)
# :-) :-) :-)

# Done!

# Ask user for number of rows
print("How many rows should I have?")
r = int(input())

# Ask user for number of columns
print("How many columns should I have?")
c = int(input())

print("Here I go:")

# create ascii emoji
ae = ":-)"

# range(start, stop, step)
# number of rows then number of columns
for rows in range(0, r, 1):
    for columns in range(0, c, 1):
        print(ae, end="")
    print()