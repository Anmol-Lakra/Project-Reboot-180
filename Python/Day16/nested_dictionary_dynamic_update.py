def display_title():
    print("=" * 40)
    print("    Nested Dictionary Dynamic Update")
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


def number_validator(num):
    try:
        num = int(num)
        if num < 1:
            print("Invalid input - Input cannot be less than 1.\n")
            return False
    except ValueError:
        print("Invalid input - Enter valid  number.\n")
        return False
    else:
        print()
        return True


def get_student_key():
    while True:
        student = input("Enter student key: ").strip()
        is_valid = text_validator(student)
        if is_valid:
            return student


def get_update_key():
    while True:
        update_key = input("Enter update_key: ").strip()
        is_valid = text_validator(update_key)
        if is_valid:
            return update_key


def get_new_value(key):
    while True:
        new_value = input("Enter new value: ").strip()
        if key == "age": 
            is_valid = number_validator(new_value)
            if is_valid:
                return int(new_value)
        else:
            is_valid = text_validator(new_value)
            if is_valid:
                return new_value
        


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

    student = get_student_key().lower()
    if student in students:
        update_key = get_update_key().lower()
        if update_key in students[student]:
            new_value = get_new_value(update_key)
            students[student][update_key] = new_value
        else:
            print(f"{update_key} not present\n")
    else:
        print(f"{student} not present\n")


    print("----student dictionary----\n")    
    for student_key, student_value in students.items():
        print(f"{student_key}:")
        for key, value in student_value.items():
            print(key, " : ", value)
        print()

main()