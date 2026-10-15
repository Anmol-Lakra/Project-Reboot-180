def display_title():
    print("=" * 40)
    print(" Nested Dictionary Students by Course")
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

def get_input_course():
    while True:
        input_course = input("Enter course: ").strip()
        is_valid = text_validator(input_course)
        if is_valid:
            return input_course.lower()

def get_matching_students(students, input_course):
    matching_students = {}
    for student_key, student_value in students.items():
        if student_value.get("course").lower() == input_course:
            matching_students[student_key] = {}
            for key, value in student_value.items():
                if key != "course":
                    matching_students[student_key][key] = value
            
    return matching_students

def print_matching_students(matching_students, input_course):
    print(f"Students enrolled in {input_course}:")
    print("=" * 35, "\n")
    for student_key, student_value in matching_students.items():
        print(student_key, ":")
        for key, value in student_value.items():
            print(f"{key}   :   {value}")
        print()

def main():
    display_title()

    students = {
        "student1": {"name": "Rahul", "age": 22, "course": "Python"},
        "student2": {"name": "John", "age": 25, "course": "Java"},
        "student3": {"name": "Alice", "age": 22, "course": "Python"},
        "student4": {"name": "David", "age": 24, "course": "Python"}
    }

    input_course = get_input_course()
    matching_students = get_matching_students(students, input_course)
    if  len(matching_students) != 0:
        print_matching_students(matching_students, input_course)
    else:
        print(f"No students found enrolled in {input_course}\n")

    print("Thank you for using Nested Dictionary Students by Course.\n")

main()
