"""
==========================================
PROJECT: Smart Calculator
PURPOSE: Perform arithmetic operations with type checking
AUTHOR: Asharib Malik
DATE: 2026-07-02
==========================================
"""

# Get two numbers from user
# Using int() because input() returns string by default
# Without int(), numbers would concatenate instead of adding
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

print("-" * 35)

# Addition
sum_result = number1 + number2
print("Sum of two numbers is:", sum_result)
print("Type of sum is:", type(sum_result))
print("-" * 35)

# Subtraction
difference = number1 - number2
print("Difference of two numbers is:", difference)
print("Type of difference is:", type(difference))
print("-" * 35)

# Multiplication
product = number1 * number2
print("Product of two numbers is:", product)
print("Type of product is:", type(product))
print("-" * 35)

# Division (always returns float in Python 3)
division = number1 / number2
print("Division of two numbers is:", division)
print("Type of division is:", type(division))
print("-" * 35)

# Floor Division (returns integer, removes decimal)
integer_division = number1 // number2
print("Integer division of two numbers is:", integer_division)
print("Type of integer division:", type(integer_division))
print("-" * 35)

# Modulus (returns remainder)
remainder = number1 % number2
print("Remainder of two numbers is:", remainder)
print("Type of remainder is:", type(remainder))
print("-" * 35)