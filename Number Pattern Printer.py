# Pattern Printing Program

rows = int(input("Enter height: "))

# Pattern 1
print("\nPattern 1")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 2
print("\nPattern 2")
for i in range(1, rows + 1):
    print((str(i) + " ") * i)

# Pattern 3
print("\nPattern 3")
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Pattern 4
print("\nPattern 4")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()