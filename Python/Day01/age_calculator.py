from datetime import date

print("==============================")
print("       Age Calculator         ")
print("==============================")
print()
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age_years = current_year - birth_year
print()

print(f"Hello {name}!")
print()

print(f"Your age is approximately {age_years} years.")
print(f"Next year you will be {age_years+1} years old.")
print()

print("You have lived approximately : ")
print(f"{age_years*365} days")
print(f"{age_years*365*24} hours")
print()

print("Thank You for using Age Calculator!")