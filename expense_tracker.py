# Expense Tracker project built by Sir-Eye

# I will include comments with stpes as I go along the code build for an easier walkthrough. Enjoy!

# Step 1: Print a welcome message
print("Welcome to Your Expense Tracker!")

# Step 2: Variables to track expenses
food_expense = 0
transport_expense = 0
entertainment_expense = 0


# Step 3: Ask the User for input
food_expense = float(input("How much did you spend on food today? "))
transport_expense = float(input("How much did you spend on transport today? "))
entertainment_expense = float(input("Howmuch did you spend on entertainment today? "))


# Step 4: Calculate the total expenses
total_expense = food_expense + transport_expense + entertainment_expense


# Step 5: Print total expense
print("Total expense for today is: $", total_expense)


# Step 6: Print a summary of all expenses
print(f"Summary - Food: ${food_expense}, Transport: ${transport_expense}, Entertainment: ${entertainment_expense}")

