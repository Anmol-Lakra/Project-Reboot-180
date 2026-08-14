print("=" * 40)
print("     Practice 05 - Try Except Finally")
print("=" * 40)
print()

try:
    number = int(input("Enter number: ").strip())
    print(f"\nYou entered: {number}\n")

except ValueError:
    print(f"\nInvalid input. Please enter an integer.\n")

finally:
    print("This program has finished.\n")    