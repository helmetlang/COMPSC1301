# 9/9/22 Friday Class

# Retirement.py


# Note unlike java you cannot put variable type before the name, you have to put it after initializing the variable
# Which is important for me to remember
monthly = float(input("How much do you invest per month? "))
rate = float(input("What is your annual rate in %? "))
years = int(input("How many years until you retire? "))

total = 0

# For loop, for x in y = 
for x in range((years)):
    total *=  1 + rate/100
    # total times itself = 1 year divided by the rate, and in the first year you dont get interest
    total += monthly * 12
    # Initializing monthly

print(f"After {years:d} years, you would have ${total:,.2f} when you retire")
# d is the type for an integer
# f is the type for float
