print("=" * 35)
print("     Practice 09 - Notes Manager")
print("=" * 35)
print()

note = input("Enter note: ").strip()

try:
    file = open("notes.txt", "a")
    file.write("\n" + note)

except PermissionError:
    print("Note was not saved successfully.\n")

else:
    print("Note saved successfully.\n")
    file.close()

try:
    file = open("notes.txt", "r")    
    data = file.read()

except FileNotFoundError:
    print("Sorry! The file was not found.\n")

else:
    print("Your notes:")
    print(data)
    file.close()

finally:
    print("\nProgram finished.\n")