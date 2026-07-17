print("=" * 45)
print("     Mini Project 3 — Inverted Triangle")
print("=" * 45)
print()

# Edge cases:
# 1. User can enter blank
# 2. User can enter alphabets/special characters
# 3. User can enter 0
# 4. User can enter decimal values
# 5. User can enter only whitespace only inputs

input_is_invalid = True
while input_is_invalid:
    height = input("Enter height: ").strip()
    if height == "":
        print("Invalid input - Height cannot be blank.\n")
    elif height.isdigit() == False:
        print("Invalid input - Height can only be a positive whole number.\n")
    elif height == "0":
        print("Invalid input - Height must be greater than zero..\n")
    else:
        input_is_invalid = False
        print()

height = int(height)

for row in range(height):
    for col in range(height - row):
        print("*", end=" ")
    print()

print("Thank you for using Inverted Triangle\n")