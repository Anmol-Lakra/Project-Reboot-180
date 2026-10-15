def display_title():
    print("=" * 40)
    print("    Multi-Student Information Manager")
    print("=" * 40)
    print()


def string_validator(user_string):
    if user_string == "":
        print("Invalid input - Input cannot be blank.\n")
        return False
    elif user_string.isdigit():
        print("Invalid input - Input cannot be a number.\n")
        return False
    else:
        print()
        return True
    

def int_validator(user_int):
    try:
        user_int = int(user_int)
        if user_int < 1:
            print("Invalid input - Age cannot be less than 1.\n")
            return False
    except ValueError:
        print("Invalid input - Please  enter valid age.\n")
        return False
    else:
        print()
        return True
    

def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        is_valid = string_validator(name)
        if is_valid:
            return name
        

def get_age():
    while True:
        age = input("Enter age:").strip()
        is_valid =  int_validator(age)
        if is_valid:
            return int(age)


def get_course():
    while True:
        course = input("Enter course: ").strip()
        is_valid = string_validator(course)
        if is_valid:
            return course



def main():
    display_title()

    count =  0
    students = {}

    while True:
        count += 1
        name = get_name()
        age = get_age()
        course = get_course()

        students[f"student{count}"] = {
            "name": name,
            "age": age,
            "course": course
        }

        while True:
            choice = input("Do you want to continue [Y/N]: ").strip().upper()
            if choice == "Y" or choice == "N":
                print()
                break
            else:
                print("Invalid choice - Enter 'Y' or 'N'\n")

        if choice == "N":
            break

    print("*" * 35)
    print("----- student dictionary -----\n")
    for student_key, student_value in students.items():
        print(f"{student_key} :")
        for key, value in student_value.items():
            print(key, " : ", value)
        print()

    print("Thank you for using Multi-Student Information Manager.\n")        

main()