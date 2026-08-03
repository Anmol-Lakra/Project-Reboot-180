# Edge cases:
# 1. User can enter special characters which will be treated as a string
# 2. User can use alphabets and numbers which will be treated as string
# 3. User can enter decimal numbers which will be treated as string

def print_title():
    print("=" * 40)
    print("Practice 5 - Reverse String Recursively")
    print("=" * 40)
    print()

def get_text():
    while True:
        text = input("Enter text: ").strip()
        if text == "":
            print("Invalid input - Text cannot be blank.\n")
        elif text.isdigit():
            print("Invalid input - Text cannot be number.\n")
        else:
            print()
            break
    return text

def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[:1]

def main():
    print_title()
    user_input = get_text()
    final_string = reverse_string(user_input)

    print(f"Reversed String :   {final_string}\n")
    print(f"Thank you for using Reverse String Recursively.\n")

main()