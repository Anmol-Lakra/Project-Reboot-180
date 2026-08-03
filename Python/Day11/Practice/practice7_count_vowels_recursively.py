# Edge cases:
# 1. User can enter special  characters which cannot be stopped
# 2. User can enter decimal numbers which cannot be stopped

def print_title():
    print("=" * 45)
    print("    Practice 7 - Count Vowels Recursively")
    print("=" * 45)
    print()

def get_text():
    while True:
        text = input("Enter text: ").strip()
        if text == "":
            print("Invalid input - Input cannot be blank.\n")
        elif text.isdigit():
            print("Invalid input - Enter text not numbers.\n")
        else:
            print()
            break
    return text

def count_vowels(text):
    if text == "":
        return 0
    if text[:1] in {"A", "E", "I", "O", "U"}:
        return 1 + count_vowels(text[1:])
    else:
        return 0 + count_vowels(text[1:])
    

def main():
    print_title()
    user_input = get_text()
    vowels = count_vowels(user_input.upper())

    print(f"No. of vowels: {vowels}\n")
    print("Thank you  for using Count Vowels Recursively.\n")
   
main()