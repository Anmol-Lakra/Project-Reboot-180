def display_title():
    print("=" * 35)
    print("   Nested Dictionary Count Search")
    print("=" * 35)
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
        print("Invalid input - Enter valid numbers.\n")
        return False
    else:
        print()
        return True

def get_info_key():
    while True:
        info_key = input("Enter information key: ").strip()
        is_valid = text_validator(info_key)
        if is_valid:
            return info_key.lower()

def get_search_value(info_key):
    while  True:
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

    information_key = get_info_key()
    info_key_present = False
    for student_value in students.values():
        if information_key in student_value: 
            info_key_present = True    
            break

    if info_key_present:
        search_value = get_search_value(information_key)
        count = 0

        for student_value in students.values():
            if information_key == "age":
                if student_value[information_key] == search_value:
                    count += 1
            else:
                if student_value[information_key].lower() == search_value:
                    count += 1

        if  not count:
            print(f"{search_value} not present\n")
        else:
            print(f"No. of matching students : {count}\n")
    else:
        print(f"{information_key} not present\n")

    print("Thank you for using Nested Dictionary Count Search.\n")


main()