# game.py - Jonathan

answer = input("Would you like to play a game? ")

while (answer[0].lower() == "y"):
# reads the index of the first letter entered into the input,
# and then force the answer into lower case
    answer = input("Would you like to play again? ")

print("Thank you, have a great day!")