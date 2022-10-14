# The Fibonacci sequence begins with 0 and then 1 follows. 
# All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. 
# Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. 
# Any negative index values should return -1.

# FIXME: Note: Use a for loop and DO NOT use recursion.

def fibonacci(n):
  if n < 0:
    print("Please enter a positive number")
    return -1

  previous_1 = 0
  previous_2 = 1
  
  if n == 0:
    return previous_1
  elif n == 1:
    return previous_2
  else:
    # calculate fibonacci
    for _ in range(2, n + 1):
      next_val = previous_1 + previous_2
      previous_1 = previous_2
      previous_2 = next_val

    return next_val
if __name__ == '__main__':
    start_num = int(input("Enter a fibonacci number: "))
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')