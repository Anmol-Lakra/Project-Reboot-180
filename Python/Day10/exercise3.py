def print_title():
    print("=" * 35)
    print("    Exercise 3 - Local Variables")
    print("=" * 35)
    print()

def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name == "":
            print("Invalid input - Name cannot be blank.\n")
        elif name.isdigit():
            print("Invalid input - Name cannot be a digit.\n")
        else:
            break

    return name

def greet(name):
    message = "Hello "
    print(message + name)


def main():
    print_title()
    user_name = get_name()
    greet(user_name)

    print("Thank You for using this program.\n")

main()