print("=" * 40)
print("          Student Marks Manager")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter a blank space in number of students and marks
# 2. User can enter alphabets/special characters in number of students and marks     
# 3. User can enter blank spaces at the begining or the end of number of students and marks

invalid_input = True
while invalid_input:
    no_of_students = input("Enter the number of students: ").strip()
    if not no_of_students.isdigit():
        print("Invalid input - No. of students should be a positive whole number.\n") 
    # elif int(no_of_students) < -1:
    #     print("Invalid input - No. of students cannot be negative.\n")
    elif int(no_of_students) == 0:
        print("Invalid input - No.of students in a class cannot be zero.\n")
    else:
        invalid_input = False
        print()

marks = []
no_of_students = int(no_of_students)

for i in range(no_of_students):

    invalid_input = True
    while invalid_input:
        mark = input(f"Enter the marks of student {i+1} : ").strip()
        if not mark.isdigit():
            print("Invalid marks - The marks of students should be a positive whole number.\n") 
        elif int(mark) < 0 or int(mark) > 100:
            print("Invalid marks - The marks of the student can be between 0-100.\n")
        else:
            invalid_input = False
            print()
    
    marks.append(int(mark))

print(f"    Class Marks - Total students: {no_of_students}")
print("-" * 40)
for j in range(no_of_students):
    print(f"Marks of student {j+1}    :       {marks[j]}")

print("\nThank You for using Student Marks Manager\n")

