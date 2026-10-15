def display_title():
    print("=" * 40)
    print("   Nested Dictionary Course Statistics")
    print("=" * 40)
    print()

def calculate_course_counts(students):
    course_counter = {}
    for student_value in students.values():
        course = student_value.get("course")
        if course in course_counter:
            course_counter[course] += 1
        else:
            course_counter[course] = 1
    return course_counter

def print_course_counter(course_counter):
    print("Course distribution:")
    print("=" * 30)

    for key, value in course_counter.items():
        print(f"{key}   :   {value} students")

def main():
    display_title()

    students = {
        "student1": {"name": "Rahul", "age": 22, "course": "Python"},
        "student2": {"name": "John", "age": 25, "course": "Java"},
        "student3": {"name": "Alice", "age": 22, "course": "Python"},
        "student4": {"name": "David", "age": 24, "course": "Python"}
    }

    course_counter = calculate_course_counts(students)
    print_course_counter(course_counter)

    print("\nThank you for using Nested Dictionary Course Statistics.\n")


main()