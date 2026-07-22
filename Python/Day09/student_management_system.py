# Edge cases:
# 1. Decimal numbers are not accepted as marks


def print_title():
    print("=" * 35)
    print("     Student Management System")
    print("=" * 35)

def get_no_of_students():
    input_is_invalid = True
    while input_is_invalid:
        num_students = input("Enter number of students: ").strip()
        if not num_students.isdigit():
            print("Invalid input - No. of students is a positive whole number.\n") 
        elif int(num_students) == 0:
            print("Invalid input - No. of students cannot be zero.\n")
        else:
            input_is_invalid = False
            print()

    return int(num_students)

def collect_student_names(num_students):
    names_list = []
    for i in range(num_students):
        input_is_invalid = True
        while input_is_invalid:
            name_of_student = input(f"Enter the name of student {i+1}: ").strip().title()
            if name_of_student == "":
                print("Invalid input - Name cannot be blank.\n")
            elif name_of_student.isdigit():
                print("Invalid name - Please enter valid name.\n")
            else:
                names_list.append(name_of_student)
                input_is_invalid = False
    
    print()
    return names_list

def collect_marks(total_students, names):
    marks = []
    for i in range(total_students):
        input_is_invalid = True
        while input_is_invalid:
            mark = input(f"Enter marks of {names[i]}:   ").strip()
            if not mark.isdigit():
                print("Invalid input - Enter positive whole numbers.\n")
            elif int(mark) > 100:
                print("Invalid input - Marks cannot be more than 100.\n")
            else:
                marks.append(int(mark))
                input_is_invalid = False
                
    print()
    return marks

def calculate_total(marks):
    total_marks = 0
    for mark in marks:
        total_marks += mark

    return total_marks

def calculate_average(total_marks, total_students):
    average_marks = total_marks/total_students

    return average_marks

def calculate_highest_lowest(marks_list):
    highest = marks_list[0]
    lowest = marks_list[0]
    for mark in marks_list:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark

    return highest, lowest

def find_topper_student(total_students, students_marks, highest_mark, names):
    toppers = []
    for i in range(total_students):
        if students_marks[i] == highest_mark:
            toppers.append(names[i])

    return toppers


def print_result(total_students, names, marks, total_marks, average, highest_mark, lowest_mark, toppers):
    print("     Class Report:")
    print("-" * 35)

    for i in range(total_students):
        print(f"Marks of {names[i]}     :    {marks[i]}")
    print("-" * 35)

    print(f"Total marks     :       {total_marks}")
    print(f"Average marks   :       {average}")
    print(f"Highest mark    :       {highest_mark}")
    print(f"Lowest mark     :       {lowest_mark}\n")

    print("Topper Student(s):")
    for topper in toppers:
        print(f"{topper} ({highest_mark})")
    print()


def main():

    print_title()

    students_count = get_no_of_students()

    students_names_list = collect_student_names(students_count)

    students_marks_list = collect_marks(students_count, students_names_list)

    students_total_marks = calculate_total(students_marks_list)

    students_average_marks = calculate_average(students_total_marks, students_count)

    highest_mark, lowest_mark = calculate_highest_lowest(students_marks_list)

    topper_students = find_topper_student(students_count, students_marks_list, highest_mark, students_names_list)

    print_result(students_count, students_names_list, students_marks_list,
                 students_total_marks, students_average_marks, highest_mark, lowest_mark, topper_students)

    print("Thank You for using Student Management System.\n")


main()

