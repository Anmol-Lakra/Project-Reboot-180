print("=" * 40)
print("      Practice 06 - Safe Calculator")
print("=" * 40)
print()

try:
    number1 = int(input("Enter number 1: ").strip())
    number2 = int(input("Enter number 2: ").strip())
    print()

    answer = number1 / number2
    print(f"Result: {answer}\n")

except ValueError:
    print("Invalid input. Please enter integers.\n")

except ZeroDivisionError:
    print("Cannot divide by zero.\n")

else:
    print("Calculation completed successfully.")

finally:
    print("Program finished.\n")