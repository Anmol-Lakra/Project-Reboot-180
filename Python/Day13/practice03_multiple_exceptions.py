print("=" * 40)
print("    Practice 03 - Multiple Exceptions")
print("=" * 40)
print()

try:    
    number1 = int(input("Enter number 1: ").strip())
    number2 = int(input("Enter number 2: ").strip())
    answer = number1 / number2
    print(f"\nResult: {answer}")

except ValueError:
    print("\nInvalid input.\n")    

except ZeroDivisionError:
    print("\nCannot divide by zero.\n")

print("Program finished.\n")