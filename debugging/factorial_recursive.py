#!/usr/bin/python3
import sys

# Function description:
# The `factorial` function calculates the factorial of a given number n using recursion.
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# Factorial is defined as: n! = n * (n-1) * (n-2) * ... * 1, with the base case of 0! = 1.

# Parameters:
# n (int): The number for which the factorial is to be calculated. This should be a non-negative integer.
#          The function expects an integer input from the user (from the command line argument).

# Returns:
# int: The factorial of the number n. If n is 0, the function returns 1 (the base case of factorial).
#      Otherwise, it returns the result of n multiplied by the factorial of n-1 (recursive case).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the input number from the command line argument
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)

