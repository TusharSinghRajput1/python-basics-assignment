# Simple Calculator with Error Handling

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handling division safely
    if num2 != 0:
        division = round(num1 / num2, 2)
        modulus = num1 % num2
    else:
        division = "Undefined (Cannot divide by zero)"
        modulus = "Undefined (Cannot divide by zero)"

    # Exponentiation
    power = num1 ** num2

    # Displaying results
    print("\n===== Results =====")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")
    print(f"{num1} % {num2} = {modulus}")
    print(f"{num1} ^ {num2} = {power}")


# Run the calculator
if __name__ == "__main__":
    calculator()