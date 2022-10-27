user_input = input().split()
# splits it by word instead of letters
word = user_input[0]
# indexes teh first word which is the fruit/item
number = user_input[1]
# indexes by the 2nd word, which is the number
while (word != "quit"):
    print("Eating {0} {1} a day keeps the doctor away.".format(number, word))
    user_input = input().split()
    word = user_input[0]
    number = user_input[1]
