"""
==========================================
PROJECT: Temperature Converter
PURPOSE: Convert Celsius to Fahrenheit and Kelvin
AUTHOR: Asharib Malik
DATE: 2026-07-02
==========================================
"""

# Get temperature in Celsius from user
# Using float() because temperature can be decimal
celsius = float(input("Enter a temperature in Celsius: "))
print("You entered Celsius:", celsius)

# Convert Celsius to Fahrenheit
# Formula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32
print("Celsius to Fahrenheit is:", fahrenheit)
print("Type of Fahrenheit:", type(fahrenheit))

# Convert Celsius to Kelvin
# Formula: K = C + 273.15
kelvin = celsius + 273.15
print("Kelvin is:", kelvin)
print("Type of Kelvin is:", type(kelvin))