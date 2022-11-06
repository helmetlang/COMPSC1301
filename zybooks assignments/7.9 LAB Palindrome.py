name = input("Write your word here:  ")

if str(name) == str(name)[::-1]:
    print(name + " is a palindrome")
else:
    print(name + " is not a palindrome")
