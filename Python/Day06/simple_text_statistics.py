print("="* 35)
print("        Simple Text Statistics")
print("="* 35)
print()

# Edge cases:
# 1. User can enter a blank
# 2. User can enter a digit
# 3. User can enter a special characters

is_input_incorrect = True
while is_input_incorrect:
    user_input = input("Enter a sentence: ").strip()
    if user_input == "":
        print("Invalid input - a sentence cannot be blank.\n")
    elif user_input.isdigit():
        print("Invalid input - a sentece cannot only have numbers.\n")
    else:
        is_input_incorrect = False

total_characters = 0
total_words = 0
uppercase_letters = 0
lowercase_letters = 0
digits = 0
spaces = 0
special_characters = 0

total_characters = len(user_input)

total_words = len(user_input.split())

for char in user_input:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special_characters += 1

print("Sentence Analysis: \n")
print(f"Total Characters            :       {total_characters}")
print(f"Total Words                 :       {total_words}")
print(f"Uppercase Letters           :       {uppercase_letters}")
print(f"Lowercase Letters           :       {lowercase_letters}")
print(f"Digits                      :       {digits}")
print(f"Spaces                      :       {spaces}")
print(f"Special Characters          :       {special_characters}\n")

normalized_input = user_input.replace(".", "")
normalized_input = user_input.replace(",", "")
normalized_input = user_input.replace("!", "")
normalized_input = user_input.replace("?", "")
normalized_input = user_input.replace(":", "")
    
all_the_words = normalized_input.split()

longest_word = all_the_words[0]
shortest_word = all_the_words[0]


for count in range(1, len(all_the_words)):
    if len(all_the_words[count]) > len(longest_word):
        longest_word = all_the_words[count]
    if len(all_the_words[count]) < len(shortest_word):
        shortest_word = all_the_words[count]


print(f"Longest word                :        {longest_word}")
print(f"Shortest word               :        {shortest_word}\n")

print("Thank You for using Simple Text Statistics\n")


     



        
