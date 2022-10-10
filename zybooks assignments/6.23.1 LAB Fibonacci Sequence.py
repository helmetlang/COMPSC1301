# The Fibonacci sequence begins with 0 and then 1 follows. 
# All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. 
# Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. 
# Any negative index values should return -1.

# FIXME: Note: Use a for loop and DO NOT use recursion.

def fibonacci(n):
    result = 0
    # if n = 0 return 0
    # elseif: anything else return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n != 0: 
        return 1  
    return result




if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

# Fn = Fn1 + Fn2
# 