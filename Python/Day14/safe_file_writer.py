def display_title():
    print("=" * 35)
    print("         Safe File Writer")
    print("=" * 35)
    print()

def write_file():
    filename = input("Enter filename: ").strip()
    data = input("Enter note: ").strip()

    try:
        file = open(filename + ".txt", "a")
        file.write(data + "\n")

    except PermissionError:
        print("\nError: the file could not be written.\n")

    else:
        file.close()
        print("\nData saved successfully.\n")


def main():
    display_title()
    write_file()
    print("Thank you for using Safe File Writer.\n")

main()