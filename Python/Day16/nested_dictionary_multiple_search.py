def display_title():
    print("=" * 40)
    print("    Nested Dictionary Multiple Search")
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
            print("Invalid input - Please enter valid numbers.\n")
            return False
    except ValueError:
        print("Invalid input - Please enter valid numbers.\n")
        return False
    else:
        print()
        return True

    

def get_information_key():
    while True:
        info_key = input("Enter information key: ").strip()
        is_valid = text_validator(info_key)
        if is_valid:
            return info_key

def get_search_value(info_key):
    while True:
        search_value = input("Enter search value: ").strip()
        if info_key == "age":
            is_valid = number_validator(search_value)
            if is_valid:
                return int(search_value)
        else:
            is_valid = text_validator(search_value)
            if is_valid:
                return search_value.lower()
            
        


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
        },
        "student3": {
            "name": "Alice",
            "age": 22,
            "course": "Python"
        },
        "student4": {
            "name": "David",
            "age": 24,
            "course": "Python"
        }
    }

    info_key = get_information_key().lower()

    info_key_present = False
    for student_value in students.values():
        if info_key in student_value:
            info_key_present = True
            break

    if info_key_present:
        search_value = get_search_value(info_key)
        matching_students = []

        for student_key, student_value in students.items():
            if info_key == "age":
                if student_value[info_key] == search_value:
                    matching_students.append(student_key)
            else:
                if student_value[info_key].lower() == search_value:
                    matching_students.append(student_key)

        if len(matching_students) != 0:
            for student_key in matching_students:
                for key, values in students[student_key].items():
                    print(key, " : ", values)
                print()
        else:
            print(f"{search_value} not present\n")
    else:
        print(f"{info_key} not present\n")

    print("Thank you for using Nested Dictionary Multiple Search.\n")

main()