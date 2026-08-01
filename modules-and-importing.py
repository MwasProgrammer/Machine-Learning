# Math module
import math

# Square root
print('Square root of 144:', math.sqrt(144))

total_days = 50
work_days = 5
week = total_days/7

print('Full weeks: ', math.floor(week))

# Random modules
import random
print('\nRandom number generator')
print(f"Random integers between 1 and 10: {random.random()}")

childhood_friends = ["Peter", "Kibocha", "Mary", "Mercy"]
print("\nRandom selection: ", random.choice(childhood_friends))

random.shuffle(childhood_friends)
print('Shuffled list: ', childhood_friends)

# DateTime module
print()
from datetime import datetime, date
print("Today's date and time are", datetime.now())

birth_date = date(2002, 10, 7)
today = date.today()
days_living_on_earth = (today - birth_date)
print('Days living on earth:', days_living_on_earth, 'days.')