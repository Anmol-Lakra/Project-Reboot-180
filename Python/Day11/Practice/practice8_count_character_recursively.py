def print_title():
    print("=" * 45)
    print("   Practice 8 - Count Character Recursively")
    print("=" * 45)
    print()

def get_text():
    while True:
        text = input("Enter text: ").strip()
        is_invalid = input_validator(text)
        if not is_invalid:
            print()
            break
    return text

def get_character():
    while True:
        character = input("Enter character: ").strip()
        is_invalid = input_validator(character)
        if len(character) > 1:
            print("Invalid character  - Please enter a single character.\n")
        elif not is_invalid:
            print()
            break
    return character

def input_validator(text):
    if text == "":
        print("Invalid input - input cannot be blank.\n")
        return True
    else:
        return False

def count_occurrences(text, character):
    if text == "":
        return 0
    if character == text[0]:
        return 1 + count_occurrences(text[1:], character)
    else:
        return 0 + count_occurrences(text[1:], character)
    
    
def main():
    print_title()
    user_text = get_text()
    user_character = get_character()
    character_in_text = count_occurrences(user_text.upper(), user_character.upper())

    print(f"Character \"{user_character}\" in text \"{user_text}\"     :   {character_in_text}\n")
    print("Thank you for using Count Character Recursively.\n")

main()


