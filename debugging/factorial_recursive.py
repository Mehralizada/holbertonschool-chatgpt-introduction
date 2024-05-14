#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from the command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
