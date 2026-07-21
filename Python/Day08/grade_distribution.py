print("=" * 35)
print("     Grade Distribution")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter a blank input
# 2. User can enter alphabets/special charcters
# 3. User can enter negative numbers
# 4. User can enter marks more than 100
# 5. User can enter decimal marks which cannot be handled yet
# 6. User can enter blank spaces at the front or end of the input

#No. of students input:
input_is_invalid = True
while input_is_invalid:
    no_of_students = input("Enter the no. of students: ").strip()
    if not no_of_students.isdigit():
        print("Invalid input - Please enter positive whole numbers.\n")
    elif int(no_of_students) == 0:
        print("Invalid input - No. of students cannot be zero.\n")
    else:
        input_is_invalid = False
        print()

#Marks input:
marks = []
no_of_students = int(no_of_students)

for i in range(no_of_students):
    input_is_invalid = True
    while input_is_invalid:
        student_marks = input(f"Enter marks of student {i+1}: ").strip()
        if not student_marks.isdigit():
            print("Invalid input - Please enter positive whole numbers.\n")
        elif int(student_marks) > 100:
            print("Invalid marks - Marks cannot be more than 100.\n")
        else:
            input_is_invalid = False
            print()
    
    marks.append(int(student_marks))

#Calculation:
grades = []

for j in range(no_of_students):
    if marks[j] >= 90:
        student_grade = "A"
    elif marks[j] >= 80:
        student_grade = "B"
    elif marks[j] >= 70:
        student_grade = "C"
    elif marks[j] >= 60:
        student_grade = "D"
    elif marks[j] >= 40:
        student_grade = "E"
    else:
        student_grade ="F"

    grades.append(student_grade)

#Printing:
print("Student's Marks and Grades:")
print("-" * 35)

for j in range(no_of_students):
    print(f"Marks of student {j+1}      :   {marks[j]}      :   Grade {grades[j]}")
print()

print("Thank you for using Grade Distribution.\n")