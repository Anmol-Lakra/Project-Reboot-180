def print_title():
    print("=" * 40)
    print("Exercise 7 - Functions Calling Functions")
    print("=" * 40)
    print()

def get_dimensions():
    is_invalid = True
    while is_invalid:
        length = input("Enter length: ").strip()
        is_invalid, length = input_validator(length)

    is_invalid = True
    while is_invalid:
        breadth = input("Enter breadth: ").strip()
        is_invalid, breadth = input_validator(breadth)    

    return length, breadth

def input_validator(dimension):
    if dimension == "":
        print("Invalid input - Input cannot be blank.\n")
        return True, dimension
    elif "." in dimension:
        dimension = float(dimension)
        return False, dimension
    elif not dimension.isdigit():
        print("Invalid input - Please enter positive numbers.\n")
        return True, dimension
    else:
        print()
        dimension = int(dimension)
        return False, dimension

def calculate_area(length, breadth):
    area = length * breadth
    return area

def calculate_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    return perimeter

def display_result(length, breadth):
    area_of_rectangle = calculate_area(length, breadth)
    perimeter_of_rectangle = calculate_perimeter(length, breadth)

    print(f"Area        :       {area_of_rectangle}")
    print(f"Perimeter   :       {perimeter_of_rectangle}\n")

def main():
    print_title()
    length, breadth = get_dimensions()
    display_result(length, breadth)

    print("Thank You for using the program.\n")

main()