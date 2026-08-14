print("=" * 35)
print("   Practice 08 - Safe File Writer")
print("=" * 35)
print()

note = input("Enter a note: ").strip()

try:
    file = open("notes.txt", "a")
    file.write("\n" + note)

except PermissionError:
    print("Error encountered - Note cannot be written.\n")

else:
    print("Note saved successfully.\n")
    file.close()

finally:
    print("Program finished.\n")