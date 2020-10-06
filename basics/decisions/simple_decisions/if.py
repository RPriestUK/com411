# What type of book is this?
# (input) adventure
# 
# I like adventure books!
#
# Finished reading book.

print("What type of book do you have?")
booktype = str(input())

if (booktype == "adventure"):
  print("I like {} books!".format(booktype))

print("I've finished reading that book now, very interesting!")