print("=" * 40)
print("         Student Grade Validator         ")
print("=" * 40)
print()

# Edge cases:
# 1. Student name is entered blank
# 2. Name has space at the begining and at the end
# 3. Name has numbers/special characters mixed in it
# 4. Student marks entered is blank
# 5. Student marks entered has alphabets/special characters
# 6. Blank Space front, end and at the middle of the marks
# 7. Student's marks is negative or more than 100
# 8. Student gets exact 80 or 100
# 9. Student gets exact 60 or 79
# 10.Student gets exact 40 or 59
# 11. Student gets exact 0 or 39
# 12. Decimal numbers cannot be accepted as marks 

student_name = input("Enter student's Full Name: ").strip().title()
if student_name == "":
    print("Invalid student name - Please enter the Student's name.\n")
else:
    student_marks = input("Enter student's marks: ").strip()
    print()    
    if student_marks == "":
        print("Invalid marks - Please enter valid marks\n")
    elif student_marks.find(" ") != -1:
        print("Invalid marks - Marks cannot have spaces. Try again.\n")   
    elif student_marks[0] == "-":
        print("Marks cannot be negative - Please enter valid marks.\n")
    elif student_marks.find(".") != -1:
        print("Marks cannot be decimal - Please enter valid marks.\n")    
    elif int(student_marks) > 100:
        print("Marks cannot be more than 100 - Please enter valid marks.\n")
    else:

        student_marks = int(student_marks)
        print("     Student's Report Card:      ")
        print("*" * 36)
        print(f"Student Name        :       {student_name}")
        print(f"Marks               :       {student_marks}")

        if student_marks >= 80:
            print(f"Grade               :       A")
            status_flag = True
            
        elif student_marks >= 60:
            print(f"Grade               :       B")
            status_flag = True
            
        elif student_marks >= 40:
            print(f"Grade               :       C")
            status_flag = True

        else:
            print(f"Grade               :       D")
            status_flag = False

            if status_flag:
                print("Status              :       Pass")
            else:
                print("Status              :       Fail")    

print("Thank You for using Student Grade Validator.\n")
