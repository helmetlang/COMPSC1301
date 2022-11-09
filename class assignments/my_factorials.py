# import my_funcs
from my_funcs import factorial

n = int(input('Enter number: '))
fact = factorial(n)
# fact = my_funcs.factorial(n)
for i in range(1, n + 1):
    print(i, end=' ')
    if i != n:
        print('*', end=' ')

print('=', fact)