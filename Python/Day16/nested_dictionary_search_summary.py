def display_title():
    print("=" * 40)
    print("    Nested Dictionary Search Summary")
    print("=" * 40)
    print()

def text_validator(text):
    if text == "":
        print("Invalid input - Input cannot be blank.\n")
        return False
    elif text.isdigit():
        print("Invalid input - Input cannot be a digit.\n")
        return False
    else:
        print()
        return True

def number_validator(num):
    try:
        num = int(num)
        if num < 1:
            print("Invalid input - Please enter valid age.\n")
            return  False
    except ValueError:
        print("Invalid input - Please enter valid digit.\n")
        return False
    else:
        print()
        return True

def get_information_key():
    while True:
        information_key = input("Enter information key: ").strip()
        is_valid = text_validator(information_key)
        if is_valid:
            return information_key.lower()

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

    information_key = get_information_key()
    info_key_present = False
    for value in students.values():
        if information_key in value:
            info_key_present = True
            break


    if info_key_present:
        search_value = get_search_value(information_key)
        matching_students = []

        for student_key, student_value in students.items():
            if information_key == "age":
                if student_value[information_key] == search_value:
                    matching_students.append(student_key)
            else:
                if student_value[information_key].lower() == search_value:
                    matching_students.append(student_key) 

        if len(matching_students) == 0:
            print(f"{search_value} not present\n")
        else:
            print("Search Results:")
            print("=" * 30, "\n")

            print(f"Matching students: {len(matching_students)}\n")

            for student in matching_students:
                print(student)
            print()
    else:
        print(f"{information_key} not present\n")

    print("Thank you for using Nested Dictionary Search Summary.\n") 

main()