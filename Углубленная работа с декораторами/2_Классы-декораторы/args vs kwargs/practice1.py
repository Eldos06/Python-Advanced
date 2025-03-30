# Exercise 1: *args Usage
# Write a function that takes any number of positional arguments and returns the product (multiplication) of all the numbers.

# Hint: Use *args to handle a variable number of arguments.

def multip(*args):
    count = 1
    for arg in args:
        count *= arg

    return count

print(multip(2,3,4))