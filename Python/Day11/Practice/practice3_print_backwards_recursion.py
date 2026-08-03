def print_backwards(text):
    if text == "":
        return
    print_backwards(text[1:])
    print(text[0])

def main():
    print("=" * 45)
    print("    Practice 3 - Print Backwards Recursion")
    print("=" * 45)
    print()

    text = "HELLO"

    print_backwards(text)

    print("\nThank you for using the program.\n")

main()

