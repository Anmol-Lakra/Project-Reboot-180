print("=" * 40)
print("   Practice 3 - Reading Student Record")
print("=" * 40)
print()

file = open("students.txt", "r")

data = file.read()

print(data)

file.close()

print("\nThank you for using Reading Student Record.\n")