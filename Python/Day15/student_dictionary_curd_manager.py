def display_title():
    print("=" * 40)
    print("    Student Dictionary CRUD Manager")
    print("=" * 40)
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

def number_validator(num):
    try:
        num = int(num)
        if num < 1:
            print("Invalid input - Please enter valid input.\n")
            return False
    except ValueError:
        print("Invalid input - Please enter valid numbers.\n")
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
        age = input("Enter age: ").strip()
        is_valid = number_validator(age)
        if is_valid:
            print()
            return int(age)

def get_course():
    while True:
        course = input("Enter course: ").strip()
        is_valid = text_validator(course)
        if is_valid:
            print()
            return course

def create_student(name, age, course):
    student = {'name': name, 'age': age, 'course': course}
    return student

def display_menu():
    print("\n1. View information")
    print("2. Update information")
    print("3. Remove information")
    print("4. Exit\n")

    while True:
        choice = input("Enter your choice: ").strip()
        is_valid = number_validator(choice)
        if is_valid:
            if int(choice) > 4:
                print("Invalid choice - Choose correct choice.\n")
            else:
                return int(choice)

def view_information(student):
    print("\n----  The Information ----")
    for key, value in student.items():
        print(key, " : ", value)

def update_information(student):
    user_key = input("Enter the key for the value you want to update: ").strip()
    is_valid = text_validator(user_key)
    if is_valid:
        if (user_key in student):
            user_value = input("\nEnter the update: ").strip()
            if user_key.upper() == "NAME" or user_key.upper() == "COURSE":
                is_valid = text_validator(user_value)
                if is_valid:
                    student[user_key] = user_value
                    return student
                else:
                    return student
            else:
                is_valid = number_validator(user_value)
                if is_valid:
                    student[user_key] = int(user_value)
                    return student
                else:
                    return student
        else:
            print(f"{user_key} is not present in student dictionary.\n")
            return student
    else:
        return student

def remove_information(student):
    key_to_delete = input("Enter the Key whose value you want to remove: ").strip()
    is_valid = text_validator(key_to_delete)
    if is_valid:
        if (key_to_delete in student):
            del student[key_to_delete]
            return student
        else:
            print(f"{key_to_delete} is not present in student dictionary.\n")
            return student    
    else:
        return student    

def main():
    display_title()
    name = get_name()
    age = get_age()
    course = get_course()
    student = create_student(name, age, course)

    while True:
        menu_choice = display_menu()
        if menu_choice == 1:
            view_information(student)
        elif menu_choice == 2:
            student = update_information(student)
        elif menu_choice == 3:
            student = remove_information(student)
        else:
            break

    print("\nThank you for using Student Dictionary CRUD Manager.\n")


main()