print("=" * 45)
print("  Mini Project 2 — Right Triangle Generator")
print("=" * 45)
print()

# Edge cases:
# 1. User can input a blank
# 2. User can input alphabets/special characters
# 3. User can input 0

input_is_invalid = True
while input_is_invalid:
    height = input("Enter the height: ").strip()
    if height == "":
        print("Invalid input - height cannot be blank.\n")
    elif height.isdigit() == False:
        print("Invalid input - Height must be a positive whole number.\n")
    elif height == "0":
        print("invalid input - Height must be a positive whole number.\n")
    else:
        input_is_invalid = False
        print()

height = int(height)

for row in range(height):
    for col in range(row + 1):
        print("*", end=" ")
    print()

print("Thank you for using Right Triangle Generator\n")