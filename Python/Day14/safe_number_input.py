print("=" * 35)
print("         Safe Number Input")
print("=" * 35)
print()

while True:
    try:
        number = int(input("Enter number: ").strip())

    except ValueError:
        print("Invalid number. Try again.\n")

    else:
        print(f"Valid number: {number}\n")
        break

print("Thank you for using Safe Number Input.\n")