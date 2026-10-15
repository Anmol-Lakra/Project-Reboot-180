def display_title():
    print("=" * 40)
    print("     Nested Dictionary Dynamic Read")
    print("=" * 40)
    print()

def text_validator(text):
    if text == "":
        print("Invalid input - Input cannot be blank.\n")
        return False
    elif text.isdigit():
        print("Invalid input - Input cannot be a number.\n")
        return  False
    else:
        print()
        return True


def get_student_key():
    while True:
        key = input("Enter student key: ").strip()
        is_valid = text_validator(key)
        if is_valid:
            return key

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
        print(f"{student_key}:")
        for key, value in students[student_key].items():
            print(key, " : ", value)
        print()
    else:
        print(f"{student_key} not present\n")

    print("Thank you for using Nested Dictionary Dynamic Read.\n")

main()