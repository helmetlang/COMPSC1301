# A pedometer treats walking 1 step as walking 2.5 feet. Define a function 
# named feet_to_steps that takes a float as a parameter, representing the number 
# of feet walked, and returns an integer that represents the number of steps walked. 
# Then, write a main program that reads the number of feet walked as an input, 
# calls function feet_to_steps() with the input as an argument, and outputs the
# number of steps as an integer.

# Use floating-point arithmetic to perform the conversion.

def feet_to_steps(user_feet):
    steps_walked = user_feet / 2.5
    # 1 step = 2.5 feet
    return int(steps_walked)
    # stores the variable to be called later
    # important to note that steps_walked needs to be converted from a float to an int

if __name__ == '__main__':
    input_feet = float(input())
    # input of feet needs to be a float
    steps_walked = feet_to_steps(input_feet)
    # steps_walked is the function feet_to_steps and recalling the input of feet
    print(int(steps_walked))
    # printing the casted steps_walked that was originally casted as a float