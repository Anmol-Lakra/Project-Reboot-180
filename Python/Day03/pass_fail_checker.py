print("=" * 40)
print("         Pass/Fail Checker           ")
print("=" * 40)
print()

# Edge cases:
# 1. input of alphabets/special characters cannot be checked as of now
# 2. cannot detect alphabets/special characters between the numbers
# 3. Student's name cannot detect if numbers/sepcial characters are entered in name
# 4. Decimal marks cannot be entered

mistake_flag = 0

student_name = input("Enter student's full name: ").strip().title()
print()
if student_name == "":
    print("Student name cannot be blank - Please enter correct name.\n")
    mistake_flag = 1
else:
    student_marks = input("Enter student's marks: ").strip()
    print()

    if student_marks == "":
        print("No marks entered - Please enter marks again.\n")
        mistake_flag = 1
    else:
        blank_finder = student_marks.find(" ")
        if blank_finder != -1:
            print("Spaces between marks - Please enter marks again.\n")
            mistake_flag = 1
        else:
            if student_marks[0] == "-":
                print("Marks cannot be negative - Please enter marks again.\n")
                mistake_flag = 1
            else:
                decimal_finder = student_marks.find(".")
                if decimal_finder != -1:
                    print("Decimal marks not accepted - Please enter marks again.\n")
                    mistake_flag = 1
                else:
                    student_marks = int(student_marks)

                    if student_marks > 100:
                        print("Marks cannot be more than 100 - Please enter marks again.\n")
                        mistake_flag = 1
                    else:        
                        if student_marks >= 80:
                            student_grade = "Grade A"
                        elif student_marks >= 60:
                            student_grade = "Grade B"
                        elif student_marks >= 40:
                            student_grade = "Grade C"
                        else:
                            student_grade = "Fail"

if mistake_flag == 0:
    print("Student's Report Card")
    print("*" * 22)

    print(f"Name of student     :       {student_name}")
    print(f"Marks obtained      :       {student_marks}")
    print(f"Status              :       {student_grade}\n")

print("Thank You for using Pass/Fail Checker!\n")
