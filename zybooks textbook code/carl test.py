string = input("Enter a word you want reversed: ")
reverse = ''
length = len(string)

for i in range (-1, -length-1, -1):
    reverse = reverse + string[i]

print(reverse)