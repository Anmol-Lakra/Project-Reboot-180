print("=" * 35)
print("       Pass/Fail Analyzer")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter blank input
# 2. User can enter special characters/alphabets as input
# 3. User can enter negative numbers as input
# 4. User can enter marks more than 100
# 5. User can enter spaces at the end or starting of input

#No. of students input
input_is_invalid = True
while input_is_invalid:
    no_of_students = input("Enter the no. of students: ").strip()
    if not no_of_students.isdigit():
        print("Invalid input - Please enter a positive whole number.\n")
    elif int(no_of_students) == 0:
        print("Invalid input - No. of students cannot be zero.\n")
    else:
        input_is_invalid = False
        print()

#Student Marks input:
marks = []
no_of_students = int(no_of_students)

for i in range(no_of_students):
    input_is_invalid = True
    while input_is_invalid:
        student_marks = input(f"Enter the marks of student {i+1}: ").strip()
        if not student_marks.isdigit():
            print("Invalid input - Marks should be positive whole numbers.\n")
        elif int(student_marks) > 100:
            print("Invalid marks - Marks cannot be more than 100.\n")
        else:
            input_is_invalid = False
            print()
    
    marks.append(int(student_marks))

#Calculation:
passed_students = 0
failed_students = 0

for mark in marks:
    if mark >= 40:
        passed_students += 1
    else:
        failed_students += 1

#Report printing
print("     Final Report:")
print("-" * 35)

for j in range(no_of_students):
    print(f"Marks of student {j+1}      :       {marks[j]}")
print()

print(f"Total Students      :       {no_of_students}")
print(f"Passed Students     :       {passed_students}")
print(f"Failed Students     :       {failed_students}\n")

print("Thank You for using Pass/Fail Analyzer\n")