def display_title():
    print("=" * 35)
    print("     Student Dictionary Manager")
    print("=" * 35)
    print()

def text_validator(text):
    if text == "":
        print("Invalid input - Input cannot be blank.\n")
        return False
    elif text.isdigit():
        print("Invalid input - Input cannot be a number.\n")
        return False
    else:
        return True

def get_name():
    while True:
        name = input("Enter name: ").strip()
        is_valid = text_validator(name)
        if is_valid:
            print()
            return name

def get_age():
    while True:
        try:
            age = int(input("Enter age: ").strip())
            if age < 1:
                print("Invalid input - Please enter proper age.\n")
                continue

        except ValueError:
            print("Invalid input -  Please enter proper age.\n")

        else:
            print()
            return age

def get_course():
    while True:
        course = input("Enter course: ").strip()
        is_valid = text_validator(course)
        if is_valid:
            print()
            return course

def create_student(name, age, course):
    student = {
        'name': name,
        'age': age,
        'course': course
    }
    return student

def main():
    display_title()
    name = get_name()
    age = get_age()
    course = get_course()
    student = create_student(name, age, course)

    for key, value in student.items():
        print(key, " : ", value)

    print("\nThank you for Student Dictionary Manager.\n")


main()