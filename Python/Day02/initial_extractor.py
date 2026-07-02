print("=" * 35)
print("         Initial Extractor           ")
print("=" * 35)
print()

full_name = input("Enter your full name: ").strip().title()
index_of_space = full_name.find(" ")
print()

print(f"The initials of {full_name} : {full_name[0]}{full_name[index_of_space+1]}\n")

print("Thank you! for using Initial Extractor\n")
