def print_characters(text):
    if text == "":
        return
    print(text[:1])
    print_characters(text[1:])
     

def main():
    print("=" * 45)
    print("  Practice 2 - Print Characters Recursively")
    print("=" * 45)
    print()

    text = "HELLO"
    print_characters(text)

    print("\nThank you for using the program.\n")

main()