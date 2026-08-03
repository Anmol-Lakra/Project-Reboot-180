def print_title():
    print("=" * 40)
    print("        Recursive Number Analyzer")
    print("=" * 40)
    print()

def get_number():
    while True:
        number = input("Enter the number: ").strip()
        if not number.isdigit():
            print("Invalid input - Please enter positive whole number.\n")
        elif int(number) == 0:
            print("Invalid input - the number cannot be zero.\n")
        else:
            print()
            break
    return number

def calculate_sum(number):
    if number == 1:
        return 1
    return number + calculate_sum(number - 1)

def calculate_factorial(number):
    if number == 1:
        return 1
    return number * calculate_factorial(number - 1)

def count_digits(number):
    if number == "":
        return 0
    return 1 + count_digits(number[:-1])

def reverse_digits(number):
    if number == "":
        return ""
    return number[-1] + reverse_digits(number[:-1])

def print_results(sum_of_nos, factorial, digits, reverse_number):
    print(f"Sum             : {sum_of_nos}")
    print(f"Factorial       : {factorial}")
    print(f"No.of digits    : {digits}")
    print(f"Reverse number  : {reverse_number}\n")
    

def main():
    print_title()
    user_number = get_number()
    sum_of_n_nos = calculate_sum(int(user_number))
    factorial_of_number = calculate_factorial(int(user_number))
    no_of_digits = count_digits(user_number)
    reverse_number = reverse_digits(user_number)
    print_results(sum_of_n_nos, factorial_of_number, no_of_digits, reverse_number)
    print("Thank you for using Recursive Number Analyzer.\n")
    

main()