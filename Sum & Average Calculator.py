# Number Statistics Program

try:
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Please enter a number greater than 0.")
        exit()
except ValueError:
    print("Invalid input! Please enter an integer value.")
    exit()

numbers = []

for i in range(count):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print("\n=== RESULTS ===")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)