# Prime Number Checker and Range Prime Finder

# Single number check
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")


# Range prime numbers
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers in range:")

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:   # This else belongs to the for-loop
            print(n, end=" ")