# COMPSCI 1301 Class October 5th 2022

CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12

feet = int(input("Enter the US height in feet: "))
inches = int(input("Enter the US height in inches: "))

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * INCHES_PER_FOOT + inches
    cm = total_inches * CM_PER_INCH
    return cm
	

	
centimeters = height_US_to_cm(feet, inches)
print('Centimeters:', centimeters)


# shift tab to unindent lines of code
# and then tab to indent it again
