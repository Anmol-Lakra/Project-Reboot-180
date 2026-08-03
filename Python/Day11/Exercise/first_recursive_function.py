def print_title():
    print("=" * 35)
    print("     First Recursive Function")
    print("=" * 35)
    print()

def count_down(number):
    if number < 1:
        return
    
    print(number)
    count_down(number - 1)

def main():
    print_title()
    count_down(5)

    print("\nThank you for using the program.\n")

main()