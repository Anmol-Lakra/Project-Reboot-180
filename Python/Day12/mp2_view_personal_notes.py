print("=" * 40)
print("  Mini Project 2 - View Personal Notes")
print("=" * 40)
print()

print("Saved notes:\n")

file = open("notes.txt", "r")

display_notes = file.read()

print(display_notes)

file.close()

print("\nThank you for using View Personal Notes.\n")