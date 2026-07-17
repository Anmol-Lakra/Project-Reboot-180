print("=" * 45)
print("Mini Project 1 — Rectangle Pattern Generator")
print("=" * 45)
print()

# Edge cases:
# 1. User can enter a blank space
# 2. User can enter decimal numbers
# 3. Usercan enter special characters


input_is_invalid = True
while input_is_invalid:
    no_of_rows = input("Enter rows: ").strip()
    if no_of_rows == "":
        print("Invalid input- rows cannot be blank.\n")
    elif no_of_rows.isdigit() == False:
        print("Invalid input - rows can only be numbers.\n")
    elif no_of_rows == "0":
        print("Invalid input - rows cannot be zero.\n")
    else: 
        input_is_invalid = False
        print()

input_is_invalid = True
while input_is_invalid:
    no_of_columns = input("Enter columns: ").strip()
    if no_of_columns == "":
        print("Invalid input- columns cannot be blank.\n")
    elif no_of_columns.isdigit() == False:
        print("Invalid input - columns can only be numbers.\n")
    elif no_of_columns == "0":
        print("Invalid input - columns cannot be zero.\n")
    else: 
        input_is_invalid = False
        print()        

no_of_rows = int(no_of_rows)
no_of_columns = int(no_of_columns)

for row in range(no_of_rows):
    for column in range(no_of_columns):
        print("*", end=" ")
    print()

print("Thank you for using Rectangle Pattern Generator\n")