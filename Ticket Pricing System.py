# Movie Ticket Billing System

try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))
except ValueError:
    print("Invalid input! Please enter correct values.")
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

# Total amount before discount
total = base_price * tickets

# Weekend discount (20%)
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * total
else:
    discount = 0

final_amount = total - discount

# Display bill
print("\n=== TICKET BILL ===")
print(f"Base Price per Ticket: ₹{base_price}")
print(f"Total before discount: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")