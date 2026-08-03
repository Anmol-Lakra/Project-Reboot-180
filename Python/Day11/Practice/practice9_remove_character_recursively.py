def print_title():
    print("=" * 45)
    print("  Practice 9 - Remove Character Recursively")
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
            print("Invalid input - Please enter single character.\n")
        elif not is_invalid:
            print()
            break
    return  character

def input_validator(text):
    if text == "":
        print("Invalid input - input cannot be blank.\n")
        return True
    else:
        print()
        return False

def remove_character(text, character):
    if text == "":
        return ""
    if character.upper() != text[0].upper():
        return text[0] + remove_character(text[1:], character)
    else: 
        return remove_character(text[1:], character)


def main():
    print_title()
    user_text = get_text()
    user_character = get_character()
    text_after_removal = remove_character(user_text, user_character)

    print(f"Character \"{user_character}\" when removed from text \"{user_text}\" : {text_after_removal}\n")
    print("Thank you for using Remove Character Recursively.\n")

main()