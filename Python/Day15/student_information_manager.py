def display_title():
    print("=" * 35)
    print("     Student Information Manager")
    print("=" * 35)
    print()

def validate_text_input(user_input):
    if user_input == "":
        print("Invalid input - the input cannot be blank")
        return False
    elif user_input.isdigit():
        print("Invalid input - the input cannot be a number.\n")
        return False
    else:
        return True
         
def main():
    display_title()

    student = {}

    while True:
        user_name = input("Enter name: ").strip()
        input_valid = validate_text_input(user_name)
        print()
        if input_valid:
            student["name"] = user_name
            print()
            break

    while True:        
        try:
            user_age = int(input("Enter age: ").strip())

            if user_age < 1:
                print("Invalid age - Please enter proper age.\n")
                continue

        except ValueError:
            print("Invalid input - Please enter proper age.\n")

        else:
            student["age"] = user_age
            print()
            break

    while True:
        user_course = input("Enter course: ").strip()
        input_valid = validate_text_input(user_course)
        print()
        if input_valid:
            student["course"] = user_course
            print()
            break

    for key, value in student.items():
        print(key, value)

    print("\nThank you for using Student Information Manager.\n")

main()
        
