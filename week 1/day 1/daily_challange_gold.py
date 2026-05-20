# Birthday Cake Program


from datetime import datetime

# Ask the user for their birthdate
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Extract day, month, and year
day, month, year = birthdate.split("/")

# Convert year to integer
year = int(year)

# Get the current year
current_year = datetime.now().year

# Calculate age
age = current_year - year

# Get the last digit of the age
candles = age % 10

# If the last digit is 0, display 1 candle
if candles == 0:
    candles = 1

# Create the candle line
candle_line = " " * 7 + "_" * candles + "i" * candles + "_" * candles

# Create the cake design
cake = f"""
{candle_line}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# Function to check leap year
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# Display two cakes if born in a leap year
if is_leap_year(year):
    print(cake)
    print(cake)
else:
    print(cake)