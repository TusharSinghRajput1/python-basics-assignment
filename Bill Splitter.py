# Bill Splitter with Tax and Tip

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