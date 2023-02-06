'''
myrandom.py - generates 100 random numbers a file
'''

import random

f = open("mydata.txt", "w")

for x in range(1000):
    mynum = random.randint(1,100)
    f.write(str(mynum) + "\n")

f.close()