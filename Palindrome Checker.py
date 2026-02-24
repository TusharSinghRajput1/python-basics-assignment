# Palindrome Checker

text = input("Enter word or number: ")

clean_text = text.lower()
reversed_text = clean_text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

if clean_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")