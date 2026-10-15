def display_title():
    print("=" * 40)
    print("      Nested Dictionary Statistics")
    print("=" * 40)
    print()

def calculate_total_and_average(students):
    total_students = 0
    total_age = 0
    for student_value in students.values():
        total_students += 1
        total_age += (student_value.get("age"))

    try:
        avg_age = total_age/total_students
    except ZeroDivisionError:
        print("There are no students in dictionary.\n")
        return 0,0,0
    return total_students, total_age, avg_age

def get_min_max_age(students):
    for value in students.values():
        min_age = value.get("age")
        max_age = value.get("age")
        break

    for student_value in students.values():
        if min_age > student_value.get("age"):
            min_age = student_value.get("age")
        if max_age < student_value.get("age"):
            max_age = student_value.get("age")
    return min_age, max_age


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

    total_students, total_age, avg_age = calculate_total_and_average(students)
    if total_students != 0:
        min_age, max_age = get_min_max_age(students)

        print("     Student statistics:")
        print("=" * 35, "\n")
        print(f"Total Students  :   {total_students}")
        print(f"Total age       :   {total_age}")
        print(f"Average age     :   {avg_age}")
        print(f"Youngest age    :   {min_age}")
        print(f"Oldest age      :   {max_age}\n")

    print("Thank you for using Nested Dictionary Statistics.\n")

main()