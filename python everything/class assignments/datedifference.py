import datetime

# Create a new date object representing the current date (May 30, 2016)
today  = datetime.date.today()

days_from_now = int(input('Enter number of days from now: '))

# Create a new timedelta object that represents a difference in the 
# number of days between dates.
day_difference = datetime.timedelta(days = days_from_now)

# Calculate new date
future_date = today + day_difference

print(days_from_now, 'days from now is', future_date.strftime('%B %d, %Y'))