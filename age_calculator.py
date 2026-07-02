"""
==========================================
PROJECT: Age Calculator
PURPOSE: Calculate age from birth year
AUTHOR: Asharib Malik
DATE: 2026-07-02
==========================================
"""

# Get current year and birth year from user
current_year = int(input("Enter current year: "))
birth_year = int(input("Enter birth year: "))

# Calculate age
total_age = current_year - birth_year

# Display results
print("Your age is:", total_age)
print("Type of age is:", type(total_age))

# Display memory address of age variable
print("Memory address of age:", id(total_age))
print("-" * 35)