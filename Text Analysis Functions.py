# Advanced Text Analyzer

def analyze_text(text):
    words = text.lower().split()
    vowels = "aeiou"

    word_count = len(words)
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in vowels)
    reversed_text = text[::-1]
    palindrome = text.lower() == reversed_text.lower()
    no_vowels = "".join([c for c in text if c.lower() not in vowels])

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    longest = max(words, key=len) if words else ""

    print("\n=== TEXT ANALYSIS ===")
    print("Words:", word_count)
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Reversed:", reversed_text)
    print("Palindrome:", "Yes" if palindrome else "No")
    print("Without vowels:", no_vowels)
    print("Longest word:", longest)
    print("Word Frequency:", freq)


# Taking input
text = input("Enter text: ")
analyze_text(text)