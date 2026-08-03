def print_title():
    print("=" * 35)
    print("        Recursive Fibonacci")
    print("=" * 35)
    print()

def get_number():
    while True:
        number = input("Enter position of Fibonacci series: ").strip()
        if not number.isdigit():
            print("Invalid input - Enter positive whole number.\n")
        elif int(number) == 0:
            print("Invalid input - Position of number cannot be zero.\n")
        else:
            number = int(number)
            break
    return number

def calculate_fibonacci(position):
    if position == 1:
        return 1
    if position == 2:
        return 1

    return calculate_fibonacci(position - 1) + calculate_fibonacci(position - 2)

def print_total(fibonacci_number, position):
    print()
    print(f"Fibonacci number at position {position} is {fibonacci_number}")

def main():
    print_title()
    number_position = get_number()
    fibonacci_number = calculate_fibonacci(number_position)
    print_total(fibonacci_number, number_position)

    print("\nThank you for using Recursive Fibonacci.\n")

main()