import csv

file_name = input()
words = []
new_words = []
#  get rid of the duplicates within the first list, 
#  second list and nested if statement that only adds words 
# that aren't contained within it, resulting in a new list of one copy of each word from the first
with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #  Delimiter is a sequence of one or more characters used to specify the boundary between separate,
    # independent regions in plain text
    for row in csv_reader:
        for word in row:
            words.append(word)
        for word in words:
            freq = words.count(word)
            if word not in new_words:
                new_words.append(word)
                print(word, freq)
                
