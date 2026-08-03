def print_title():
    print("=" * 40)
    print("  Practice 12 - Recursive Binary Search")
    print("=" * 40)
    print()

def get_number():
    return [2, 5, 8, 12, 15, 19, 25]

def get_target():
    while True:
        target_number = input("Enter target number: ").strip()
        if not target_number.isdigit():
            print("Invalid input - Enter whole numbers.\n")
        else:
            return target_number

def binary_search(numbers, target):
    if len(numbers) == 0:
        return False
    middle_index = len(numbers)//2
    if target == numbers[middle_index]:
        return True
    elif target < numbers[middle_index]:
        return binary_search(numbers[:middle_index], target)
    else:
        return binary_search(numbers[middle_index+1:], target)
    

def main():
    print_title()
    numbers_list = get_number()
    target_number = int(get_target())
    target_present = binary_search(numbers_list, target_number)
    if target_present:
        print(f"{target_number} was found in the numbers list.\n")
    else:
        print(f"{target_number} was not found in the numbers list.\n")

    print("Thank you for using Recursive Binary Search.\n")

main()