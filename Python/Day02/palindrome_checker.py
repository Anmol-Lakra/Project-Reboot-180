print("=" * 40)
print("         Palindrome Checker          ")
print("=" * 40)
print()

# Edge cases:
# 1. We cannot control if the user is entering string, int or special characters
# 2. We cannot warn the user when there is a space between the word or they have entered 2 words
# 3. We cannot warn the user when they give empty input
# 4. At this stage we cannot check and give a output if a string is palindrome or not

user_word = input("Enter a word: ").strip()
print()

print(f"Original        :       {user_word}")
print(f"Reversed        :       {user_word[::-1]}\n")

print("Thank You! for using Palindrome Checker\n")