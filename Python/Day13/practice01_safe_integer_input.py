print("=" * 35)
print("  Practice 01 - Safe Integer Input")
print("=" * 35)
print()

number = input("Enter number: ").strip()
try:
    int(number)
    print(f"You entered: {number}\n")
except ValueError:
    print("Invalid input. Please enter an integer.\n")

print("Program finished.\n")