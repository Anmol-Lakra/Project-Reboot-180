def print_title():
    print("=" * 45)
    print("  Understanding Local Variables in Recursion")
    print("=" * 45)
    print()

def count_down(number):
    print("Before:", number)
    if number == 1:
        return 

    count_down(number - 1)
    print("After:", number)

def main():
    print_title()
    count_down(3)


main()
