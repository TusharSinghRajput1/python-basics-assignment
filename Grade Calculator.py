# Student Result & Grade Calculator

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

# Pass/Fail Condition (Minimum 40 in each subject)
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