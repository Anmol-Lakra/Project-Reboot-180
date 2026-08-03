def print_title():
    print("=" * 45)
    print(" Practice 10 - Replace Character Recursively")
    print("=" * 45)
    print()

def input_validator(text, is_Char):
    if text == "":
        print("Invalid input - Input cannot be blank.\n")
        return True
    elif is_Char:
        if len(text) > 1:
            print("Invalid input - Please enter 1 character.\n")
            return True
        else:
            return False
    else:
        print()
        return False

def get_text():
    while True:
        text = input("Enter text: ").strip()
        is_invalid = input_validator(text, False)
        if not is_invalid:
            break
    return  text

def get_old_character():
    while True:
        old_character = input("Enter the character you want to replace: ").strip()
        is_invalid = input_validator(old_character, True)
        if not is_invalid:
            print()
            break
    return old_character

def get_new_character():
    while True:
        new_character = input("Enter the new  character: ").strip()
        is_invalid = input_validator(new_character, True)
        if not is_invalid:
            print()
            break
    return new_character

def replace_character(text, old_character, new_character):
    if text == "":
        return ""
    if old_character.upper() == text[0].upper():
        return new_character + replace_character(text[1:], old_character, new_character)
    else:
        return text[0] + replace_character(text[1:], old_character, new_character)

def main():
    print_title()
    user_text = get_text()
    user_old_character = get_old_character()
    user_new_character = get_new_character()
    new_text = replace_character(user_text, user_old_character, user_new_character)

    print(f"Old text         :      {user_text}")
    print(f"Character \"{user_old_character}\" was replaced  by character \"{user_new_character}\".\n")
    print(f"New text         :      {new_text}\n")

    print("Thank you for  using Replace Character Recursively.\n")


main()  