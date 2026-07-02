"""
==========================================
PROJECT: Type Detective
PURPOSE: Check data types of variables and user inputs
AUTHOR: Asharib Malik
DATE: 2026-07-02
==========================================
"""

# Get name directly (hardcoded)
name = "Ali"
print("Name:", name)
print("Name type:", type(name))

# Get name from user input
name_input = input("Enter your name: ")
print("Type of name as input:", type(name_input))

# Get number directly (hardcoded)
number = 29
print("Number:", number)
print("Number type:", type(number))

# Get number from user input
number_input = input("Enter a number: ")
print("Type of number as input:", type(number_input))

# Get decimal directly (hardcoded)
decimal = 3.5
print("Decimal:", decimal)
print("Decimal type:", type(decimal))

# Get decimal from user input
decimal_input = input("Enter your decimal value: ")
print("Type of decimal as input:", type(decimal_input))

# NOTE: input() always returns string type
# Type casting not learned yet, so keeping it simple