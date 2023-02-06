# names_and_ages.py
'''
the user enters names and ages, separated by commas,
then can look up an age.
'''

names_and_ages = input("Enter names and ages, separated by commas:\n").lower().title()

# print_names_and_ages)
ages_dict = {} # make sure to set up an empty dictionary

for pair in names_and_ages.split(","):
    pair = pair.strip()
    splitpair = pair.split()
    # print(splitpair)
    ages_dict[splitpair[0]] = int(splitpair[1])

print(ages_dict)

person = input("Enter an age you want you look up: ").strip().title()
if person in ages_dict:
    print(person + " is " + str(ages_dict[person]) + " years old.")
else:
    print("I dont have that peron's age.")

print("Here are all the ages in your family: ")
for name in ages_dict:
    print(name +  " is " + str(ages_dict[name]))

print("Here are all the ages in your family: ")
for name, age in ages_dict.items():
    print(name +  " is " + str(age))
