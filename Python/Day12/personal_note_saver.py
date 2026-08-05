print("=" * 40)
print("  Mini Project 1 - Personal Note Saver")
print("=" * 40)
print()

note = input("Enter your note: ").strip()
file = open("notes.txt", "a")
file.write("\n" + note)
file.close()