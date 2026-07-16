print("=" * 40)
print("           Palindrome Checker")
print("=" * 40)
print()

# Edge cases:
# 1. User can enetr an empty string

input_is_invalid = True
while input_is_invalid:
    user_input = input("Enter a word or a sentence: ").strip()
    if user_input == "":
        print("Invalid input - Input cannot be blank\n")
    else:
        input_is_invalid = False
        print()


normalized_input = user_input.replace(" ", "")
normalized_input = normalized_input.replace(",", "")
normalized_input = normalized_input.replace(".", "")
normalized_input = normalized_input.replace("?", "")
normalized_input = normalized_input.replace("!", "")

normalized_input = normalized_input.upper()

palindrome_to_compare = normalized_input[::-1]

if normalized_input == palindrome_to_compare:
    print("Palindrome.\n")
else:
    print("Not a palindrome.\n")

print("Thank you for using Palindrome Checker\n")
        


