def display_title():
    print("=" * 40)
    print("     Nested Dictionary Dynamic Search")
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
        print("Invalid input - Enter a valid number.\n")
        return False
    else:
        print()
        return True


def get_information_key():
    while True:
        info_key = input("What information do you want to search by? ").strip()
        is_valid = text_validator(info_key)
        if is_valid:
            return info_key


def get_search_value(info_key):
    while True:
        search_value = input(f"Enter {info_key} to search: ").strip()
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
                }
            }

    information_key = get_information_key().lower()

    information_key_present = False
    for student_value in students.values():
        if information_key in student_value:
            information_key_present = True
            break

    if information_key_present:        
        search_value = get_search_value(information_key)

        value_found = False
        for student_key, student_value in students.items():
            if information_key == "age":
                if  student_value[information_key] == search_value:
                    student_key_found = student_key
                    value_found = True
            else:
                if  student_value[information_key].lower() == search_value:
                    student_key_found = student_key
                    value_found = True

        if value_found:
            print("Search value found!\n")
            for key,  value in students[student_key_found].items():
                print(key, " : ", value)
            print()
        else:
            print("Search value not found.\n")

    else:
        print(f"{information_key} key not present in the dictionary\n")

    print("Thank you for using Nested Dictionary Dynamic Search.\n")

main()