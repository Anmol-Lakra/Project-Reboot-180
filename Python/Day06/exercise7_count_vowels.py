print("Exercise 7 — Count Vowels")
print()
word = "Education"
vowel_counter = 0
consonant_counter = 0
for char in word.upper():
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        vowel_counter += 1
    else:
        consonant_counter += 1

print(f"Vowels = {vowel_counter}\n")

print("Mentor challange - count consonants")
print(f"Consonants = {consonant_counter}")