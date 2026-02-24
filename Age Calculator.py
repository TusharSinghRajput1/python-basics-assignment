from datetime import datetime

try:
    # Taking full birth date
    day = int(input("Enter birth day (DD): "))
    month = int(input("Enter birth month (MM): "))
    year = int(input("Enter birth year (YYYY): "))

    # Creating birth date object
    birth_date = datetime(year, month, day)

except ValueError:
    print("Invalid date input! Please enter valid numbers.")
    exit()

# Current date
today = datetime.now()

# Age calculation (years)
age_years = today.year - birth_date.year

# Adjust if birthday not yet occurred this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

# Time difference
difference = today - birth_date

age_days = difference.days
age_months = age_years * 12
age_hours = age_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Display results
print("\n===== AGE DETAILS =====")
print("Age in Years:", age_years)
print("Age in Months:", age_months)
print("Age in Days:", age_days)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years remaining to turn 100:", years_to_100)