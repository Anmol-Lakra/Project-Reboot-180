def display_title():
    print("=" * 35)
    print("         Safe File Reader")
    print("=" * 35)
    print()

def read_file():
    file_name = input("Enter filename: ").strip()
    try:
        file = open(file_name, "r")
        data = file.read()

    except FileNotFoundError:
        print("Error: File not  found.\n")

    else:
        print("\n----File Contents----")
        print(data)
        print()
        file.close()

def main():
    display_title()
    read_file()
    print("Thank you for using Safe File Reader.\n")

main()