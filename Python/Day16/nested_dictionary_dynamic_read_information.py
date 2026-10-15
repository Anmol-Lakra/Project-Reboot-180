def display_title():
    print("=" * 45)
    print("  Nested Dictionary Dynamic Read Information")
    print("=" * 45)
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
        key = input("Enter student key: ").strip()
        is_valid = text_validator(key)
        if is_valid:
            return key


def get_information_key():
    while True:
        info_key = input("Enter information key: ").strip()
        is_valid = text_validator(info_key)
        if is_valid:
            return info_key    

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
            value = students[student_key][information_key]
            print(f"{information_key} : {value}\n")
        else:
            print(f"{information_key} is not present\n")
    else:
        print(f"{student_key} is not present\n")

    print("Thank you for using Nested Dictionary Dynamic Read Information.\n")

main()