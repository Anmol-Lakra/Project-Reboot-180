def print_title():
    print("=" * 45)
    print("  Practice 6 - Recursive Palindrome Checker")
    print("=" * 45)
    print()

def get_text():
    while True:
        text = input("Enter a string: ").strip()
        if text == "":
            print("Invalid input - String cannot be blank.\n")
        else:
            print()
            break
    return text

def is_palindrome(text):
    if text == "" or len(text) == 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def main():
    print_title()
    user_input = get_text()
    is_string_palindrome = is_palindrome(user_input)

    if is_string_palindrome:
        print(f"The string '{user_input}' is palindrome.\n")
    else:
        print(f"The string '{user_input}' is not a palindrome.\n")

    print("Thank you for using Recursive Palindrome Checker.\n")

main()