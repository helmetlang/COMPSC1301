change = int(input())


# input is 45
# break into dollars even though there are none
# break into quarters, get 1 quarter
# break into dimes, get 2
# break into nickels, get 0
# break into pennies and get 0


dollars = str(change // 100)
change %= 100
quarters = str(change // 25)
change %= 25
dimes = str(change // 10)
change %= 10
nickels = str(change // 5)
change %= 5
pennies = str(change // 1)
change %= 1


# needs an if statement for plurals
# needs conditional for eliminating anything that's just 0
print(dollars + " Dollars")
print(quarters + " Quarters")
print(dimes + " Dimes")
print(nickels + " Nickels")
print(pennies + " Pennies")
