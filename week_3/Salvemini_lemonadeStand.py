"""
Author: Brandon Salvemini
Date: 6/11/2024
File Name: Salvemini_lemonadeStand.py
Description: Python program that simulates a lemonade stand
"""

# Function to calculate the cost
def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

# Function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    return selling_price - (lemons_cost + sugar_cost)

# Variables for the cost of lemons, cost of sugar, and selling price
cost_of_lemons = 1.95
cost_of_sugar = 3.29
selling_price = 5.35

# Variables for total cost and profit
total_cost = calculate_cost(cost_of_lemons, cost_of_sugar)
profit = calculate_profit(cost_of_lemons, cost_of_sugar, selling_price)

# String variable for displaying the total cost
result_string = f"Total cost: ${cost_of_lemons} + ${cost_of_sugar} = ${total_cost}"

# Output the contents of the result_string variable to the screen
print(result_string)

# Output the profit to the screen
# The :.2f at the end of the profit variable formats it to two decimal places
# This was found here: https://realpython.com/python-f-strings/#formatting-strings-with-pythons-f-string
print(f"Profit: ${selling_price} - ${total_cost} = ${profit:.2f}")