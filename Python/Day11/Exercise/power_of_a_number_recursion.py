def print_title():
    print("=" * 40)
    print("     Power of a Number (Recursion)")
    print("=" * 40)
    print()

def get_base():
    is_invalid = True
    while is_invalid:
        base = input("Enter Base: ").strip()
        is_invalid = validate_input(base)
    return int(base)

def get_exponent():
    is_invalid = True
    while is_invalid:
        exponent = input("Enter Exponent: ").strip()
        is_invalid = validate_input(exponent)
    return int(exponent)

def validate_input(number):
    if not number.isdigit():
        print("Invalid input - Enter positive whole numbers.\n")
        return True
    elif int(number) == 0:
        print("Invalid input - Number cannot be zero.\n")
        return True
    else:
        return False

def calculate_power(base, exponent):
    if exponent == 1:
        return base

    return base * calculate_power(base, exponent - 1)


def main():
    print_title()
    base_number = get_base()
    exponent_number = get_exponent()
    final_result = calculate_power(base_number, exponent_number)

    print(f"{base_number} raised to the power of {exponent_number} =  {final_result}\n")
    print("Thank you for using Power of a Number (Recursion).\n")


main()