print("=" * 40)
print("      Practice 04 - Try Except Else")
print("=" * 40)
print()

try:
    number = int(input("Enter number: ").strip())

except ValueError:
    print("\nInvalid input. Please enter an integer.\n")

else:
    print(f"\nYou entered: {number}\n")

print("Program finished.\n")
