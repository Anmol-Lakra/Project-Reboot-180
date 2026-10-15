def display_title():
    print("=" * 45)
    print("   Nested Dictionary Dynamic Delete Student")
    print("=" * 45)
    print()

def text_validator(text):
    if text == "":
        print("Invalid input - Input cannot be blank.\n")
        return  False
    elif text.isdigit():
        print("Invalid input - Input cannot be a number.\n")
        return False
    else:
        print()
        return True


def get_student_key():
    while True:
        student_key = input("Enter the student key to delete: ").strip()
        is_valid = text_validator(student_key)
        if is_valid:
            return student_key
        

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

    stud_key = get_student_key().lower()
    if stud_key in students:
        del students[stud_key]
        print(f"{stud_key} deleted successfully.\n")
    else:
        print(f"{stud_key} not present\n")


    print("-----Student Dictionary-----\n")
    for student_key, student_value in students.items():
        print(f"{student_key}:")
        for key,  value in student_value.items():
            print(key, " : ", value)
        print()


main()