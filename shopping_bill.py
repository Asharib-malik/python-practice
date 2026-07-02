"""
==========================================
PROJECT: Shopping Bill
PURPOSE: Calculate total price of items
AUTHOR: Asharib Malik
DATE: 2026-07-02
NOTE: Bug - string concatenation instead of addition
      Will fix after learning float() and type casting
==========================================
"""

# Get item details from user
item1_name = input("Enter item 1 name: ")
item1_price = input("Enter item 1 price: ")

item2_name = input("Enter item 2 name: ")
item2_price = input("Enter item 2 price: ")

item3_name = input("Enter item 3 name: ")
item3_price = input("Enter item 3 price: ")

# Display items
print(f"Item 1: {item1_name} - {item1_price} Rs")
print(f"Item 2: {item2_name} - {item2_price} Rs")
print(f"Item 3: {item3_name} - {item3_price} Rs")
print("-" * 35)

# BUG ALERT: This concatenates strings instead of adding numbers
# Example: "50" + "30" + "20" = "503020" instead of 100
# FIX: Use float(item1_price) after learning type casting
total_price = item1_price + item2_price + item3_price

print("-" * 35)
print("Total price is:", total_price)
print("Type of total price is:", type(total_price))