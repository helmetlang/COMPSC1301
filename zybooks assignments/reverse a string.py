while True: # while the statement is true
    string = str(input()) # has to be converted to a string for input
    if string == 'Done' or string == 'done' or string == 'd': # allows to exit program
        break # break out of this call
    reverse = '' # creates an empty string
    for i in string: 
        reverse = i+ reverse
    print(reverse)
