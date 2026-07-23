# Edge case:
# 1. Special characters cannot be handled by the program
# 2. It cannot handle a name with a dot



def print_title():
    print("=" * 45)
    print("Exercise 6 - Positional & Keyword Arguments")
    print("=" * 45)
    print()

def get_name():
    is_invalid = True
    while is_invalid:
        first_name = input("Enter first name: ").strip().title()
        is_invalid = input_validator(first_name)

    is_invalid = True
    while is_invalid:
        last_name = input("Enter last name: ").strip().title()
        is_invalid = input_validator(last_name)

    return first_name, last_name

def input_validator(name):
    if name == "":
        print("Invalid input - Name cannot be blank.\n")
        return True
    elif name.isdigit():
        print("Invalid input - Name cannot be a digit.\n")
        return True
    elif "." in name:
        print("Invalid input - Name cannot have decimal numbers.\n")
        return True
    else:
        print()
        return False

def display_name(f_name, l_name):
    print(f"{f_name} {l_name}")

def main():
    print_title()
    first_name, last_name = get_name()

    print("Using Positional Arguments:")
    display_name(first_name, last_name)
    print()

    print("Using Keyword Arguments:")
    display_name(l_name=last_name, f_name=first_name)

    print("\nThank you for using the program.\n")

main()