print('Opening file myfile.txt.')
f = open('myfile.txt')  # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:')
print(contents)