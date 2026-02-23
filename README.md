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

try:
    # Taking full birth date
    day = int(input("Enter birth day (DD): "))
    month = int(input("Enter birth month (MM): "))
    year = int(input("Enter birth year (YYYY): "))

    # Creating birth date object
    birth_date = datetime(year, month, day)

except ValueError:
    print("Invalid date input!")
    exit()

# Current date
today = datetime.now()

# Age calculation
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
print("\n=== AGE DETAILS ===")
print(f"Current Age: {age_years} years")
print(f"Age in Months: {age_months}")
print(f"Age in Days: {age_days}")
print(f"Age in Hours: {age_hours}")
print(f"Age in Minutes: {age_minutes}")
print(f"Years until 100: {years_to_100}")
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
        
# -----------------------------------
# Question 11: Number Pattern Printer
# Name: Tushar Kumar
# -----------------------------------

rows = int(input("Enter height: "))

print("\nPattern 1")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 2")
for i in range(1, rows + 1):
    print((str(i) + " ") * i)

print("\nPattern 3")
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("\nPattern 4")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
# -----------------------------------
# Question 12: Multiplication Table
# Name: Tushar Kumar
# -----------------------------------

num = int(input("Enter number: "))
range_end = int(input("Enter range end: "))

print(f"\nMultiplication Table of {num}")

for i in range(1, range_end + 1):
    print(f"{num} x {i} = {num * i}")
# -----------------------------------
# Question 13: Sum & Average Calculator
# Name: Tushar Kumar
# -----------------------------------

count = int(input("How many numbers? "))

numbers = []

for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print("\n=== RESULTS ===")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
# -----------------------------------
# Question 14: Factorial Calculator
# Name: Tushar Kumar
# -----------------------------------

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    factorial = 1
    steps = ""

    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i) + " × " if i != 1 else "1"

    print(f"{num}! = {steps} = {factorial}")
# -----------------------------------
# Question 15: Prime Number Checker
# Name: Tushar Kumar
# -----------------------------------

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")

# Range primes
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers in range:")

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
# -----------------------------------
# Question 16: Number Guessing Game
# Name: Tushar Kumar
# -----------------------------------

import random

while True:
    number = random.randint(1, 100)
    attempts = 7
    guessed = False

    print("\nGuess the number between 1 and 100")

    while attempts > 0:
        guess = int(input("Enter guess: "))
        attempts -= 1

        if guess == number:
            print("Correct! You guessed it.")
            guessed = True
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        print("Attempts left:", attempts)

    if not guessed:
        print("You failed. Number was:", number)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
# -----------------------------------
# Question 17: Palindrome Checker
# Name: Tushar Kumar
# -----------------------------------

text = input("Enter word or number: ")

clean_text = text.lower()
reversed_text = clean_text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

if clean_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")
# -----------------------------------
# Question 18: Calculator Using Functions
# Name: Tushar Kumar
# -----------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")
    choice = input("Enter choice: ")

    if choice == '7':
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    elif choice == '5':
        print("Result:", modulus(a, b))
    elif choice == '6':
        print("Result:", power(a, b))
    else:
        print("Invalid choice")
# -----------------------------------
# Question 19: Text Analysis Functions
# Name: Tushar Kumar
# -----------------------------------

def analyze_text(text):
    words = text.lower().split()
    vowels = "aeiou"

    word_count = len(words)
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in vowels)
    reversed_text = text[::-1]
    palindrome = text.lower() == reversed_text.lower()
    no_vowels = "".join([c for c in text if c.lower() not in vowels])

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    longest = max(words, key=len)

    print("\n=== TEXT ANALYSIS ===")
    print("Words:", word_count)
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Reversed:", reversed_text)
    print("Palindrome:", "Yes" if palindrome else "No")
    print("Without vowels:", no_vowels)
    print("Longest word:", longest)
    print("Word Frequency:", freq)

text = input("Enter text: ")
analyze_text(text)
# -----------------------------------
# Question 20: Number System Functions
# Name: Tushar Kumar
# -----------------------------------

import math

def factorial(n):
    return math.factorial(n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d)**power for d in str(n))

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

while True:
    print("\n1.Factorial 2.Prime 3.Fibonacci 4.SumDigits 5.Reverse")
    print("6.Armstrong 7.GCD 8.LCM 9.Perfect 10.Exit")
    choice = input("Enter choice: ")

    if choice == '10':
        break

    if choice == '1':
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif choice == '2':
        n = int(input("Enter number: "))
        print("Prime:", is_prime(n))

    elif choice == '3':
        n = int(input("Enter n: "))
        print("Fibonacci:", fibonacci(n))

    elif choice == '4':
        n = int(input("Enter number: "))
        print("Sum of digits:", sum_of_digits(n))

    elif choice == '5':
        n = int(input("Enter number: "))
        print("Reversed:", reverse_number(n))

    elif choice == '6':
        n = int(input("Enter number: "))
        print("Armstrong:", is_armstrong(n))

    elif choice == '7':
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("GCD:", gcd(a, b))

    elif choice == '8':
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("LCM:", lcm(a, b))

    elif choice == '9':
        n = int(input("Enter number: "))
        print("Perfect number:", is_perfect_number(n))
