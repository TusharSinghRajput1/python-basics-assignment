# python-basics-assignment
Name: Tushar Kumar  
Course: BE ECE  
College:CMR Institute of Technology (CMRIT)  


## 📘 Assignment Details

This repository contains my Python Basics Assignment covering Modules 1–6.

The assignment includes programs based on:

- Python Fundamentals
- Operators & Conditions
- Loops
- Strings
- Functions
- Mathematical Logic
# -----------------------------------
# Question 1: Personal Bio Card
# Name: Tushar Kumar
# -----------------------------------

name = "Tushar Kumar"
age = 22
course = "BE ECE"
college = "CMRIT"
email = "tuku22ece@cmrit.ac.in"

print("╔════════════════════════════════════╗")
print("║          STUDENT BIO CARD          ║")
print("╠════════════════════════════════════╣")
print(f"║ Name    : {name:<23}║")
print(f"║ Age     : {str(age) + ' years':<23}║")
print(f"║ Course  : {course:<23}║")
print(f"║ College : {college:<23}║")
print(f"║ Email   : {email:<23}║")
print("╚════════════════════════════════════╝")
# -----------------------------------
# Question 2: Simple Calculator
# Name: Tushar Kumar
# -----------------------------------

# Taking user input with error handling
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division safely
if num2 != 0:
    division = round(num1 / num2, 2)
else:
    division = "Undefined (Cannot divide by zero)"

# Modulus (works only if not zero)
if num2 != 0:
    modulus = num1 % num2
else:
    modulus = "Undefined (Cannot divide by zero)"

# Exponentiation
power = num1 ** num2

# Displaying results
print("\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ^ {num2} = {power}")
# -----------------------------------
# Question 3: String Manipulator
# Name: Tushar Kumar
# -----------------------------------

# Taking sentence input
sentence = input("Enter a sentence: ")

# Original sentence
print("\nOriginal:", sentence)

# Characters count
char_with_spaces = len(sentence)
char_without_spaces = len(sentence.replace(" ", ""))

# Word count
words = sentence.split()
word_count = len(words)

# Case conversions
uppercase = sentence.upper()
lowercase = sentence.lower()
titlecase = sentence.title()

# First & Last word
first_word = words[0] if word_count > 0 else ""
last_word = words[-1] if word_count > 0 else ""

# Reversed sentence
reversed_sentence = sentence[::-1]

# Display results
print("Characters (with spaces):", char_with_spaces)
print("Characters (without spaces):", char_without_spaces)
print("Words:", word_count)
print("UPPERCASE:", uppercase)
print("lowercase:", lowercase)
print("Title Case:", titlecase)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)
# -----------------------------------
# Question 4: Age Calculator
# Name: Tushar Kumar
# -----------------------------------

from datetime import datetime

# Taking birth year input
try:
    birth_year = int(input("Enter your birth year: "))
except ValueError:
    print("Invalid input! Please enter a valid year.")
    exit()
# -----------------------------------
# Question 7: Temperature Converter
# Name: Tushar Kumar
# -----------------------------------

while True:
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting program...")
        break

    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid input! Please enter numeric value.")
        continue

    if choice == '1':
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result:.2f}°F")

    elif choice == '2':
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result:.2f}°C")

    elif choice == '3':
        result = temp + 273.15
        print(f"{temp}°C = {result:.2f}K")

    elif choice == '4':
        result = temp - 273.15
        print(f"{temp}K = {result:.2f}°C")

    elif choice == '5':
        result = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F = {result:.2f}K")

    elif choice == '6':
        result = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K = {result:.2f}°F")

    else:
        print("Invalid choice! Please select 1-7.")
# Current year
current_year = datetime.now().year

# Calculations
age_years = current_year - birth_year
age_months = age_years * 12
age_days = age_years * 365      # Approximation
age_hours = age_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Display results
print("\n=== AGE DETAILS ===")
print(f"Current Age: {age_years} years")
print(f"Age in Months: {age_months}")
print(f"Age in Days (approx): {age_days}")
print(f"Age in Hours: {age_hours}")
print(f"Age in Minutes: {age_minutes}")
print(f"Years until 100: {years_to_100}")
# -----------------------------------
# Question 5: Bill Splitter
# Name: Tushar Kumar
# -----------------------------------

try:
    total_bill = float(input("Enter total bill amount: ₹"))
    number_of_people = int(input("Enter number of people: "))
    tax_percent = float(input("Enter tax percentage: "))
    tip_percent = float(input("Enter tip percentage: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

if number_of_people <= 0:
    print("Number of people must be greater than 0.")
    exit()

# Calculations
tax_amount = (tax_percent / 100) * total_bill
bill_after_tax = total_bill + tax_amount

tip_amount = (tip_percent / 100) * bill_after_tax
final_total = bill_after_tax + tip_amount

amount_per_person = final_total / number_of_people

# Display breakdown
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{total_bill:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
print(f"After Tax: ₹{bill_after_tax:.2f}")
print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
print(f"Total Bill: ₹{final_total:.2f}")
print(f"Amount Per Person: ₹{amount_per_person:.2f}")
# -----------------------------------
# Question 6: Grade Calculator
# Name: Tushar Kumar
# -----------------------------------

try:
    print("Enter marks for 5 subjects (out of 100):")
    
    sub1 = float(input("Subject 1: "))
    sub2 = float(input("Subject 2: "))
    sub3 = float(input("Subject 3: "))
    sub4 = float(input("Subject 4: "))
    sub5 = float(input("Subject 5: "))
    
except ValueError:
    print("Invalid input! Please enter numeric marks.")
    exit()

# Total & Percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Grade Calculation
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Pass/Fail Condition
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display Results
print("\n=== RESULT ===")
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Final Result: {result}")
# -----------------------------------
# Question 7: Temperature Converter
# Name: Tushar Kumar
# -----------------------------------

while True:
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Program exited.")
        break

    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid input! Enter numeric value.")
        continue

    if choice == '1':
        result = (temp * 9/5) + 32
        print(f"{temp} °C = {result:.2f} °F")

    elif choice == '2':
        result = (temp - 32) * 5/9
        print(f"{temp} °F = {result:.2f} °C")

    elif choice == '3':
        result = temp + 273.15
        print(f"{temp} °C = {result:.2f} K")

    elif choice == '4':
        result = temp - 273.15
        print(f"{temp} K = {result:.2f} °C")

    elif choice == '5':
        result = (temp - 32) * 5/9 + 273.15
        print(f"{temp} °F = {result:.2f} K")

    elif choice == '6':
        result = (temp - 273.15) * 9/5 + 32
        print(f"{temp} K = {result:.2f} °F")

    else:
        print("Invalid choice! Please select 1–7.")
# -----------------------------------
# Question 8: Leap Year Checker
# Name: Tushar Kumar
# -----------------------------------

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input! Enter a valid year.")
    exit()

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a LEAP YEAR.")
    print("Reason: Divisible by 4 and not divisible by 100 unless divisible by 400.")
else:
    print(f"{year} is NOT a leap year.")
    print("Reason: Does not satisfy leap year conditions.")
# -----------------------------------
# Question 9: Ticket Pricing System
# Name: Tushar Kumar
# -----------------------------------

try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))
except ValueError:
    print("Invalid input!")
    exit()

# Base price by age
if age < 3:
    base_price = 0
elif 3 <= age <= 12:
    base_price = 150
elif 13 <= age <= 59:
    base_price = 300
else:
    base_price = 200

total = base_price * tickets

# Weekend discount
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * total
else:
    discount = 0

final_amount = total - discount

print("\n=== TICKET BILL ===")
print(f"Base Price per Ticket: ₹{base_price}")
print(f"Total before discount: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")
# -----------------------------------
# Question 10: ATM Simulator
# Name: Tushar Kumar
# -----------------------------------

balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        print(f"Current Balance: ₹{balance}")

    elif choice == '2':
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print(f"New Balance: ₹{balance}")
            else:
                print("Invalid amount.")
        except ValueError:
            print("Invalid input.")

    elif choice == '3':
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount > 0 and balance - amount >= 500:
                balance -= amount
                print("Withdrawal successful!")
                print(f"New Balance: ₹{balance}")
            else:
                print("Insufficient balance or minimum ₹500 must remain.")
        except ValueError:
            print("Invalid input.")

    elif choice == '4':
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice!")
        
