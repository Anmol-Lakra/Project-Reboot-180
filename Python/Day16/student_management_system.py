def display_menu():
    print("=" * 35)
    print("     Student Management System")
    print("=" * 35)
    print()

def number_validator(num):
    try:
        num = int(num)
        if num < 1:
            print("Invalid input - Input cannot be 0 or negative.\n")
            return False
    except ValueError:
        print("Invalid input - Please enter valid numbers.\n")
        return False
    else:
        print()
        return True

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

def get_students_dictionary():
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
    return students

def search_student_info(students):
    while True:
        student_id = input("Enter student ID: ").strip().lower()
        is_valid = text_validator(student_id)
        if not is_valid:
            continue
        else:
            if student_id in students:
                while True:
                    info_key = input("Enter information to search (name/age/course): ").strip()
                    is_valid = text_validator(info_key)
                    if is_valid:
                        info_key_not_found = True
                        for key, value in students[student_id].items():
                            if key == info_key.lower():
                                print(f"Student ID  :   {student_id}")
                                print(f"{info_key}      :   {value}\n")
                                info_key_not_found = False
                                return

                        if info_key_not_found:
                            print(f"Information '{info_key}' not found for {student_id}.\n")
                            return       
            else:
                print("Student not found.\n")
                return
        


def display_all_students(students):
    no_students = True

    for student_key, student_value in students.items():
        print(student_key, ":")
        for key, value in student_value.items():
            print(f"{key}: {value}")
        print()
        no_students = False

    if no_students:
        print("No student records available.\n")

def update_student_info(students):
    while True:
        student_id = input("Enter student ID: ").strip()
        is_valid = text_validator(student_id)
        if  not is_valid:
            continue
        else:
            student_id = student_id.lower()
            if student_id not in students:
                print("Student not found.\n")
                return
            else:
                while True:
                    info_key = input("Enter information to update: ").strip()
                    is_valid = text_validator(info_key)
                    if not is_valid:
                        continue
                    else:
                        if info_key.lower() not in students[student_id]:
                            print(f"Information '{info_key}' not found for {student_id}.\n")
                            return
                        else:
                            while True:
                                updated_data = input(f"Enter new {info_key.lower()}: ").strip()
                                if info_key.lower() == "age":
                                    is_valid = number_validator(updated_data)
                                    if is_valid:
                                        updated_data = int(updated_data)
                                else:
                                    is_valid = text_validator(updated_data)
                                    
                                info_key = info_key.lower()
                                if not is_valid:
                                    continue
                                else:
                                    students[student_id][info_key] = updated_data

                                    print("Student information updated successfully.\n")
                                    print(f"{student_id}:")
                                    for key, value in students[student_id].items():
                                        print(f"{key}   :   {value}")
                                    print()
                                    return
                                    
def delete_student_info(students):
    while True:
        student_id = input("Enter student ID: ").strip()
        is_valid = text_validator(student_id)
        if is_valid:
            student_id = student_id.lower()
            if student_id in students:
                while True:
                    info_to_delete = input("Enter information to delete: ").strip()
                    is_valid = text_validator(info_to_delete)
                    if is_valid:
                        info_to_delete = info_to_delete.lower()
                        if info_to_delete in students[student_id]:
                            del students[student_id][info_to_delete]

                            print("Student information deleted successfully.\n")
                            print(f"{student_id}:")
                            for key, value in students[student_id].items():
                                print(f"{key}   :   {value}")
                            print()
                            return
                        else:
                            print(f"Information '{info_to_delete}' not found for {student_id}.\n")
                            return
                    else:
                        continue
            else:
                print("Student not found.\n")
                return
        else:
            continue

def delete_student(students):
    while True:
        student_id  = input("Enter student ID to delete: ").strip()
        is_valid = text_validator(student_id)
        if is_valid:
            student_id = student_id.lower()
            if student_id in students:
                del students[student_id]

                print("Student deleted successfully.\n")
                print("Remaining students:\n")
                display_all_students(students)
                return

            else:
                print("Student not found.\n")
                return
        else:
            continue


    
def find_student_by_info(students):
    while True:
        info_to_search = input("Enter information to search: ").strip().lower()
        is_valid = text_validator(info_to_search)

        if not is_valid:
            continue

        # Check whether the information key exists
        info_to_search_found = False

        for student_id in students:
            if info_to_search in students[student_id]:
                info_to_search_found = True
                break

        if not info_to_search_found:
            print(f"'{info_to_search}' is not found.\n")
            return

        # Get the value to search
        while True:
            value_to_search = input("Enter value to search: ").strip()

            if info_to_search == "age":
                is_valid = number_validator(value_to_search)

                if is_valid:
                    value_to_search = int(value_to_search)
            else:
                is_valid = text_validator(value_to_search)
                value_to_search = value_to_search.lower()

            if not is_valid:
                continue

            print(f"Students matching {info_to_search} = {value_to_search}:")
            print("=" * 35)

            value_to_search_not_found = True

            # Search through all student records
            for student_id in students:

                # CORRECTION: Skip students missing the requested field
                if info_to_search not in students[student_id]:
                    continue

                student_value = students[student_id][info_to_search]
                student_match_found = False

                if info_to_search == "age":
                    if student_value == value_to_search:
                        student_match_found = True
                else:
                    if str(student_value).lower() == value_to_search:
                        student_match_found = True

                if student_match_found:
                    value_to_search_not_found = False

                    print(f"{student_id}:")
                    for key, value in students[student_id].items():
                        print(f"{key} : {value}")
                    print()

            if value_to_search_not_found:
                print(
                    f"'{value_to_search}' not found in "
                    f"'{info_to_search}'.\n"
                )

            return


              

def display_student_statistics(students):
    student_number = len(students)
    total_age = 0
    youngest_age = None
    oldest_age = None
    age_count = 0

    for student_key in students:
        if "age" in students[student_key]:
            age = students[student_key]["age"]
            total_age += age
            age_count += 1

            if youngest_age is None or youngest_age > age:
                youngest_age = age
            if oldest_age is None or oldest_age < age:
                oldest_age = age

   
        else:
            print(f"{student_key} age information not available.\n")

    if age_count == 0:
        print("No student age information available.\n")
        return

    avg_age = total_age/age_count

    print("Student Statistics:")
    print("=" * 30)
    print(f"Total Students      :       {student_number}")
    print(f"Student with age    :       {age_count}")
    print(f"Average age         :       {avg_age}")
    print(f"Youngest age        :       {youngest_age}")
    print(f"Oldest age          :       {oldest_age}\n")   

      

def display_course_distribution(students):
  
    course_counter = {}
    course_not_present = True

    for student_key in students:
        if "course" in students[student_key]:
            course_not_present = False
            new_course = students[student_key]["course"].lower()
            if new_course not in course_counter:
                course_counter[new_course] = 1
            else:
                course_counter[new_course] += 1

    for key,  value in course_counter.items():
        print(f"{key}       :   {value}")
    print()

    if course_not_present:
        print("No course information available.\n")




def find_student_by_course(students):
    while True:
        course_input = input("Enter course: ").strip()
        is_valid = text_validator(course_input)
        if is_valid:
            print(f"Students enrolled in {course_input}:")
            print("=" * 30)

            student_found = False
            for student_id, student_value in students.items():
                if "course" in students[student_id]:
                    if (student_value["course"]).lower() == course_input.lower():
                        student_found = True

                        print(f"{student_id}:")
                        for key, value in student_value.items():
                            if key == "course":
                                continue
                            else:
                                print(f"{key}   :   {value}")
                        print()

                else:
                    print(f"course information not present in {student_id}.\n")

            if not student_found:
                print(f"No students found enrolled in {course_input}.\n")
            
            return



def main():

    students = get_students_dictionary()

    while True:
        display_menu()
        print("1. Display all students")
        print("2. Search student information")
        print("3. Update  student information")
        print("4. Delete student information")
        print("5. Delete student")
        print("6. Find students by information")
        print("7. Display student statistics")
        print("8. Display course distribution")
        print("9. Find students by course")
        print("10. Exit\n")

        choice = input("Enter choice: ").strip()
        is_valid = number_validator(choice)
        if not is_valid:
            continue
        else:
            choice = int(choice)
            if choice > 10:
                print("Invalid choice - choose a number between 1-10.\n")
                continue
            elif choice == 1:
                display_all_students(students)
            elif choice == 2:
                search_student_info(students)
            elif choice == 3:
                update_student_info(students)
            elif choice == 4:
                delete_student_info(students)
            elif choice == 5:
                delete_student(students)
            elif choice == 6:
                find_student_by_info(students)
            elif choice == 7:
                display_student_statistics(students)
            elif choice == 8:
                display_course_distribution(students)
            elif choice == 9:
                find_student_by_course(students)
            elif choice == 10:
                break
    
    print("Thank you for using student Management System.\n")            

main()
