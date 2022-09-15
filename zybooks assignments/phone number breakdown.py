# done two different ways
# one i made using len
# one i made using the actual correct math



phone_number = int(input())

i = 1234
Calculation = i % 10

print(Calculation)

i = i // 10

print(str(i) + "-" + str(Calculation))
phone_number = str(i) + "-" + str(Calculation)

# 123-4



    # len version 
phone_number = input()

len(phone_number) == 10
    
print('(' + phone_number[0] + phone_number[1] + phone_number[2] + ')' + ' ' + phone_number[3] + phone_number[4] +  phone_number[5]
+ '-' + phone_number[6] + phone_number[7] + phone_number[8] + phone_number[9])

# This works however I want to put this into a format statement or try to make it look better
# Should probably also be solved with math and not just a len list/statement

