print("=" * 40)
print("       Practice 1 - Save User Name")
print("=" * 40)
print()

name = input("Please enter name: ").strip()
file = open("names.txt", "a")
file.write("\n" + name)
file.close()