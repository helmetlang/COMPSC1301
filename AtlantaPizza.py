import math

# AtlantaPizza.py – a simple pizza cost calculator

# Ask the person how many pizzas they want, get the # with eval()
number_of_pizzas = int( input("How many pizzas do you want: ") )

# Ask for the menu cost of each pizza
cost_per_pizza = float( input("How much does each pizza cost: ") )

# Calculate the total cost of the pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizza

# Calculate the sales tax owed, at 8.5% of the subtotal
tax_rate = 0.085 # we store 8.5% as the decimal value 0.085
sales_tax = subtotal * tax_rate

# Add the sales tax to the subtotal for the final total
total = subtotal + sales_tax

# Show the user the total amount due, including tax
print(f"The total cost is $ {total:,.2f}")
# print(f'{math.pi:.4f}')
    # f = format inside the () of print statement
    # inside curly braces is the existing variable you want to edit
    # :.(number) = how many decimal places you want it to edit
        # if you add a , to the existing 2f you format the commas for numbers in the thousands
print(f"This includes $ {subtotal:,.2f} for the pizza and")
print(f"$ {sales_tax:.2f} in sales tax.")
