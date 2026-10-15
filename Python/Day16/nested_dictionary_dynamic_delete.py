def display_title():
    print("=" * 40)
    print("    Nested Dictionary Dynamic Delete")
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
        print()
        return True


def get_student_key():
    while True:
        student_key = input("Enter student key: ").strip()
        is_valid = text_validator(student_key)
        if is_valid:
            return student_key


def get_information_key():
    while True:
        information_key = input("Enter information key you want to delete: ").strip()
        is_valid = text_validator(information_key)
        if is_valid:
            return  information_key

    

def main():
    display_title()

    students = {
            "student1": {
                "name": "Rahul",
                "age": 22,
                "course": "Python"
            },
            "student2": {
                "name": "John",
                "age": 25,
                "course": "Java"
            }
        }

    student_key = get_student_key().lower()
    if student_key in students:
        information_key = get_information_key().lower()
        if information_key in students[student_key]:
            del students[student_key][information_key]
            print(f"{information_key} deleted successfully.\n")
        else:
            print(f"{information_key} not present.\n")
    else:
        print(f"{student_key} not present.\n")        


    print("-----student dictionary-----\n")
    for stud_key, stud_value in students.items():
        print(f"{stud_key}:")
        for key, value in stud_value.items():
            print(key, " : ", value)
        print()

    print("Thank you for using Nested Dictionary Dynamic Delete.\n")

main()