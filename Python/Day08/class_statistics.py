print("=" * 35)
print("       Class Statistics")
print("=" * 35)
print()

# Edge cases:
# 1. User can enter a blank in no. of students and marks
# 2. User can enter an alphabet/special characters in no. of students and marks
# 3. User can enter blank spaces before and after the input
# 4. User can enter a zero in number of students
# 5. User can enter a negative number as input
# 6. User cannot enter decimal digits for marks, the isdigit() catches it to be false

input_is_invalid = True
while input_is_invalid:
    no_of_students = input("Enter the no. of students: ").strip()
    if not no_of_students.isdigit():
        print("Invalid input - Number of students should be a positive whole number:\n")
    elif int(no_of_students) == 0:
        print("Invalid input - Number of students in a class cannot be 0.\n")
    else:
        input_is_invalid = False
        print()

# Marks input:
marks = []
no_of_students = int(no_of_students)

for i in range(no_of_students):
    input_is_invalid = True
    while input_is_invalid:
        mark = input(f"Enter marks of Student {i+1} : ").strip()
        if not mark.isdigit():
            print("Invalid input - Marks should be positive whole numbers.\n")
        elif int(mark) > 100:
            print("Invalid input - Marks cannot be more than 100.\n")
        else:
            input_is_invalid = False
            print()

    marks.append(int(mark))

#Calulation:
total_marks = 0
highest_mark = marks[0]
lowest_mark = marks[0]

for mark in marks:
    total_marks = total_marks + mark

    if highest_mark < mark:
        highest_mark = mark
    if lowest_mark > mark:
        lowest_mark = mark

avg_marks = total_marks/no_of_students

#Printing
print("Marks entered:")
print("-" * 30)
for j in range(no_of_students):
    print(f"Student {j+1} marks     :       {marks[j]}")

print("-" * 30)       
print(f"Total Students      :       {no_of_students}")
print(f"Total marks         :       {total_marks}")
print(f"Average marks       :       {avg_marks}")
print(f"Highest marks       :       {highest_mark}")
print(f"Lowest mark         :       {lowest_mark}\n")

print("Thank You for using Class Statistics\n")