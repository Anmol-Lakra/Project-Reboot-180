def display_title():
    print("=" * 35)
    print("     Get Valid Number")
    print("=" * 35)
    print()

def get_valid_number():
    while True:
        try:
            num = int(input("Enter number: ").strip())

        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        return num

def main():
    display_title()
    number = get_valid_number()
    print(f"User input: {number}\n")
    print("Thank you for using Get Valid Number.\n")

main()


