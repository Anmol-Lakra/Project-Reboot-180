def print_title():
    print("=" * 35)
    print("       Sum of First N Numbers")
    print("=" * 35)
    print()

def get_number():
    while True:
        number = input("Enter number: ").strip()
        if not number.isdigit():
            print("Invalid input - Enter a positive whole number.\n")
        elif int(number) == 0:
            print("Invalid input - The number cannot be zero.\n")
        else:
            number = int(number)
            print()
            break
    return number

def calculate_sum(number):
    if number == 1:
        return 1

    return number + calculate_sum(number - 1)

def print_result(sum):
    print(f"The sum :    {sum}\n")

def main():
    print_title()
    user_number = get_number()
    total_sum = calculate_sum(user_number)
    print_result(total_sum)

    print("Thnak You for using Sum of First N Numbers.\n")

main()