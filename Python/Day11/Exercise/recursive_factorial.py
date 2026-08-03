def print_title():
    print("=" * 30)
    print("     Recursive Factorial")
    print("=" * 30)
    print()

def get_number():
    while True:
        number = input("Enter a number: ").strip()
        if not number.isdigit():
            print("Invalid input - Enter positive whole number.\n")
        elif int(number) == 0:
            print("Invalid input - Number cannot be zero.\n")
        else:
            number = int(number)
            print()
            break
    return number

def calculate_factorial(number):
    if number == 1:
        return 1

    return number * calculate_factorial(number - 1)

def main():
    print_title()
    user_number = get_number()
    factorial = calculate_factorial(user_number)

    print(f"Factorial of {user_number}  :   {factorial}\n")
    print("Thank you for using Recursive Factorial.\n")

main()