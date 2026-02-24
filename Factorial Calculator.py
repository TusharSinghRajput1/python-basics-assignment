# Factorial Program with Steps

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
        if i != 1:
            steps += str(i) + " × "
        else:
            steps += "1"

    print(f"{num}! = {steps} = {factorial}")