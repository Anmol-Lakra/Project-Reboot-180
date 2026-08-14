print("=" * 35)
print("     Practice 02 - Safe Division")
print("=" * 35)
print()

number1 = int(input("Enter number 1: ").strip())
number2 = int(input("Enter number 2: ").strip())

try:
    answer = number1/number2
    print(f"\nResult: {answer}\n")
except ZeroDivisionError:
    print("\nCannot divide by zero.\n")

print("Program finished.\n")