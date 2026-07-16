print("=" * 35)
print("       Word Frequency Counter")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter blank

input_validator = True
while input_validator:
    user_sentence = input("Enter a sentence: ").strip()
    if user_sentence == "":
        print("Invalid sentence - sentence cannot be blank\n")
    else:
        input_validator = False

input_validator = True
while input_validator:
    word_to_search = input("Enter a word: ").strip()
    if word_to_search == "":
        print("Invalid word - word cannot be blank\n")
    elif " " in word_to_search:
        print("invalid word - space cannot be present between the word\n")
    else:
        input_validator = False
        print()

words_in_sentence = user_sentence.split()
word_counter = 0
temp_word_to_search = word_to_search.upper()

for word in words_in_sentence:
    if "," in word:
        word = word.replace(",", "")
    if "." in word:
        word = word.replace(".", "")
    if "!" in word:
        word = word.replace("!", "")
    if "?" in word:
        word = word.replace("?", "")

    if temp_word_to_search == word.upper():
        word_counter += 1

print(f"The word {word_to_search} appears {word_counter} times.\n")

# Bonus Challenge:
print(f"Total words: {len(words_in_sentence)}\n")

print("Thank You for using Word Frequency Counter\n")



    