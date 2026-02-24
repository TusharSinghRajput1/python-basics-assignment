# Function-Based Calculator

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
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '7':
        print("Calculator closed.")
        break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

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
        print("Invalid choice! Please select 1-7.")