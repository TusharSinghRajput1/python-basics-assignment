# Multiplication Table Program

num = int(input("Enter number: "))
range_end = int(input("Enter range end: "))

print(f"\nMultiplication Table of {num}")

for i in range(1, range_end + 1):
    print(f"{num} x {i} = {num * i}")