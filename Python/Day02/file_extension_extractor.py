print("=" * 45)
print("         File Extension Extractor            ")
print("=" * 45)
print()

# Edge cases:
# 1. It does not work if two dots(.) are present in the name
# 2. It cannot differentiate if the input data is string, int or special character
# 3. It takes a blank input when pressed enter
# 4. It gives wrong extension if a file is written without extension

file_name = input("Enter your file name with extension: ").strip()
string_length = len(file_name)
index_of_dot = file_name.find(".")
print()

print(f"Filename    :   {file_name[0:index_of_dot]} \nExtension   :   {file_name[index_of_dot+1:string_length]}\n")

print("Thank you! for using File Extension Extractor\n")