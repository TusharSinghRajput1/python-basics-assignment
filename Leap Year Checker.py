# Leap Year Checker

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input! Enter a valid year.")
    exit()

# Leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a LEAP YEAR.")
    print("Reason: Divisible by 4 and not divisible by 100 unless divisible by 400.")
else:
    print(f"{year} is NOT a leap year.")
    print("Reason: Does not satisfy leap year conditions.")