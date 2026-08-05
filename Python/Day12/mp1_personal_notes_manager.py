print("=" * 45)
print("   Mini Project 1 - Personal Notes Manager")
print("=" * 45)
print()

note = input("Enter your note: ").strip()

file = open("notes.txt", "a")

file.write("\n" + note)

file.close()

print("\nNote saved successfully.\n")
print("Thank you for using Personal Notes Manager.\n")