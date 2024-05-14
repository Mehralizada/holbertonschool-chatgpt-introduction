#!/usr/bin/python3
import sys

# This function calculates the factorial of a number recursively.
# The factorial of 0 is 1. For any other positive integer n, 
# the factorial is the product of all positive integers less than or equal to n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# The script takes an argument from the command line, converts it to an integer,
# and passes it to the factorial function.
f = factorial(int(sys.argv[1]))

# The result of the factorial function is then printed to the console.
print(f)
