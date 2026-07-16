print("=" * 35)
print("         Character Analyzer")
print("=" * 35)
print()

input_checker = True
while input_checker:
    user_input = input("Enter a word or sentence: ").strip()
    if user_input == "":
        print("Invalid input - input must contain a word or a sentence.\n")
    else:
        input_checker = False
        print()

total_characters = 0
upper_case_letters = 0
lower_case_letters = 0
digits = 0
space_counter = 0
special_characters = 0

for char in user_input:
    total_characters += 1
    if char.isupper():
        upper_case_letters += 1
    elif char.islower():
        lower_case_letters += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        space_counter += 1
    else:
        special_characters += 1

print("Character Analysis:\n")
print(f"Total Characters        :       {total_characters}")
print(f"Uppercase               :       {upper_case_letters}")
print(f"Lowercase               :       {lower_case_letters}")
print(f"Digits                  :       {digits}")
print(f"Blank Spaces            :       {space_counter}")
print(f"Special Characters      :       {special_characters}\n")

print("Thank you for using Character Analyzer\n")