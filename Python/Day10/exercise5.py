def print_title():
    print("=" * 35)
    print("  Exercise 5 - Default Parameters")
    print("=" * 35)
    print()

def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name == "":
            print("Invalid input - Name cannot be blank.\n")
        elif name.isdigit():
            print("Invalid input - Name cannot be a number.\n")
        else:
            print()
            break

    return name

def greet(name="Guest"):
    print(f"Hello {name}")
    print("Have a nice day!\n")


def main():
    print_title()
    user_name = get_name()
    print("Function taking the default parameter:")
    greet()
    print("\nFunction taking the 'name' parameter when provided:")
    greet(user_name)

    print("\nThank you for using the program.\n")

main()