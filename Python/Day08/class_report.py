print("=" * 35)
print("            Class Report")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter blank inputs
# 2. User can enter alphabets/special characters as input
# 3. User can enter a negative number as input
# 4. User can enter zero as no. of students
# 5. User can enter marks more than 100
# 6. User can enter decimal numbers which cannot be handled in marks
# 7. User can enter blank spaces at the front or back of the input

#Input:
input_is_invalid = True
while input_is_invalid:
    no_of_students = input("Enter number of students: ").strip()
    if not no_of_students.isdigit():
        print("Invalid input - Please enter positive whole numbers\n")
    elif int(no_of_students) == 0:
        print("Invalid input - No. of students cannot be zero.\n")
    else:
        input_is_invalid = False
        print()

marks = []
no_of_students = int(no_of_students)

for i in range(no_of_students):
    input_is_invalid = True
    while input_is_invalid:
        student_marks = input(f"Enter marks of student {i+1}: ").strip() 
        if not student_marks.isdigit():
            print("invalid input - Please enter positive whole numbers.\n")
        elif int(student_marks) > 100:
            print("invalid marks - Marks cannot be more than 100.\n")
        else:
            input_is_invalid = False
            print()
    
    marks.append(int(student_marks))

#Calculation:
grades = []
total_marks = 0
highest_mark = marks[0]
lowest_mark = marks[0]
passed_students = 0
failed_students = 0

for j in range(no_of_students):

    total_marks += marks[j]

    if marks[j] > highest_mark:
        highest_mark = marks[j]
    if marks[j] < lowest_mark:
        lowest_mark = marks[j]
    
    if marks[j] >= 40:
        passed_students += 1
    else:
        failed_students += 1

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
        student_grade = "F"

    grades.append(student_grade)
avg_marks = total_marks/no_of_students

#Printing:
print("         Final Report:")
print("-" * 48)

for y in range(no_of_students):
    print(f"Marks of student {y+1}  :   {marks[y]}  :   ", end="")
    if marks[y] >= 40:
        print("Pass", end=" :   ")
    else:
        print("Fail", end=" :   ")
    print(f"Grade {grades[y]}")
print("-" * 48)
print(f"Total Students      :       {no_of_students}")
print(f"Passed Students     :       {passed_students}")
print(f"Failed Students     :       {failed_students}")
print(f"Highest Mark        :       {highest_mark}")
print(f"Lowest Mark         :       {lowest_mark}")
print(f"Total Marks         :       {total_marks}")
print(f"Average Marks       :       {avg_marks}\n")

print("Thank you for using Class Report\n")
