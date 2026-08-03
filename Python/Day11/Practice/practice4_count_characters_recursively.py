# Edge cases:
# 1. User can enter decimal digits which cannot be handled
# 2. User can enter special characters

def print_title():
    print("=" * 45)
    print("  Practice 4 - Count Characters Recursively")
    print("=" * 45)
    print()

def get_text():
    while True:
        text = input("Enter text: ").strip()
        if text == "":
            print("Invalid input - Input cannot be blank.\n")
        elif text.isdigit():
            print("Invalid input - Input cannot be a number.\n")
        else:
            print()
            break
    return text

def count_characters(text):
    if text == "":
        return 0
    return 1 + count_characters(text[1:])

def main():
    print_title()
    user_input = get_text()
    no_of_characters = count_characters(user_input)

    print(f"Number of characters in {user_input} : {no_of_characters}\n")

    print("Thank you for using Count Characters Recursively.\n")


main()