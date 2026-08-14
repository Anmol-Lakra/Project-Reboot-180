print("=" * 40)
print("     Practice 07 - Safe File Reader")
print("=" * 40)
print()

try:
    file = open("notes.txt", "r")
    data = file.read()

except FileNotFoundError:
    print("File not found.\n")

else:
    print(data)
    file.close()

finally:
    print("Program finished.\n")
