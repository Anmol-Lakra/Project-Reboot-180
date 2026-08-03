def print_title():
    print("=" * 50)
    print("  Practice 11 - Find Maximum in List Recursively")
    print("=" * 50)
    print()

def get_numbers():
    numbers = [15, 2, 1, 8, 9]
    return numbers

        
def find_maximum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    remaining_max = find_maximum(numbers[1:])
    if numbers[0] < remaining_max:
        return remaining_max
    else:
        return numbers[0] 

def main():
    print_title()
    numbers_list = get_numbers()
    max_number = find_maximum(numbers_list)
    print(f"Numbers : {numbers_list}")
    print(f"The maximum number : {max_number}\n")
    print("Thank you for using Find Maximum in List Recursively.\n")

main()