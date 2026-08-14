print("=" * 35)
print("    Practice 10 - Student Record")
print("=" * 35)
print()

try:
    name = input("Enter student name: ").strip()
    age = int(input("Enter age: ").strip())

    file = open("students.txt", "a")
    file.write(f"\n{name} - {age}")

except ValueError:
    print("\nInvalid input - Please enter a valid age.\n")

except PermissionError:
    print("\nStudent record not saved.\n")

else:
    print("\nStudent record saved successfully.\n")
    file.close()

finally:
    print("Program finished.\n")
