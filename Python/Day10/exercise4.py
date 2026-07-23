COMPANY_NAME = "ABC"

def print_title():
    print("=" * 40)
    print("     Exercise 4 - Global Variables")
    print("=" * 40)
    print()

def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name == "":
            print("Input invalid - Name cannot be blank.\n")
        elif name.isdigit():
            print("Invalid input - Name cannot be a digit.\n")
        else:
            print()
            break

    return name

def greet(name):
    greeting = "Hello "
    print(greeting + name)
    print(f"Welcome to {COMPANY_NAME} company.\n")

def main():
    print_title()
    user_name = get_name()
    greet(user_name)

    print("Thank you for using the program.\n")

main()

