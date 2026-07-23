# Edge cases:
# 1. User can input multiple dots which cannot be handled as we are not using try/except

def print_title():
    print("=" * 47)
    print("Exercise 2 - Area and Perimeter of a rectangle")
    print("=" * 47)
    print()

def get_rectangle_dimensions():
    input_is_invalid = True
    while input_is_invalid:
        length = input("Enter length of the rectangle: ").strip()
        input_is_invalid, rectangle_length = validate_input(length)
        print()

    input_is_invalid = True
    while input_is_invalid:
        breadth = input("Enter the breadth of the rectangle: ").strip()
        input_is_invalid, rectangle_breadth = validate_input(breadth)
        print()

    return rectangle_length, rectangle_breadth

def validate_input(user_input):
    if user_input == "":
        print("Invalid input - input cannot be blank.\n")
        return True, user_input
    elif "." in user_input:
        user_input = float(user_input)
        return False, user_input
    elif not user_input.isdigit():
        print("Invalid input - please input positive numbers.\n")
        return True, user_input
    else:
        user_input = int(user_input)
        return False, user_input

def calculate_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2*(length + breadth)

    return area, perimeter

def print_result(area, perimeter):
    print(f"The area of the rectangle       :   {area}")
    print(f"The perimeter of the rectangle  :   {perimeter}\n")

def main():
    print_title()
    rectangle_length, rectangle_breadth = get_rectangle_dimensions()
    area_of_rectangle, perimeter_of_rectangle = calculate_area_perimeter(rectangle_length, rectangle_breadth)
    print_result(area_of_rectangle, perimeter_of_rectangle)

    print("Thank you for using Area and Perimeter of a rectangle.\n")

main()