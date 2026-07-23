# Edge cases:
# 1. Decimal numbers/Special characters/Negative numbers cannot be handled in the name input
# 2. Salary can have multiple decimal dots in a numbers which cannot be handled as we have not 
#    done try/except
# 3. Current validation allows alphabetic names only.
# 4. Names containing digits or special characters are not supported.

COMPANY = "ABC Company"

def print_title():
    print("=" * 35)
    print("     Employee Salary Calculator")
    print("=" * 35)
    print()

def get_employee_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name == "":
            print("Invalid input - Name cannot be blank.\n")
        elif name.isdigit():
            print("Invalid input - Name cannot be a number.\n")
        else:
            break
    return name

def get_monthly_salary():
    while True:
        salary = input("Enter Salary: ").strip()
        if salary == "":
            print("Invalid input - Input cannot be blank.\n")
        elif "." in salary:
            salary = float(salary)
            break
        elif not salary.isdigit():
            print("Invalid input - Input a valid positive number.\n")
        else:
            salary = int(salary)
            print()
            break
    return salary

def calculate_annual_salary(salary):
    total_salary = 12 * salary
    return total_salary

def calculate_bonus(annual_salary, percent=10):
    bonus = (percent/100) * annual_salary
    return bonus

def display_salary_report(name, salary):
    annual_salary = calculate_annual_salary(salary)
    annual_bonus = calculate_bonus(annual_salary)

    print(f"Company         :       {COMPANY}")
    print(f"Employee Name   :       {name}")
    print(f"Monthly Salary  :       {salary}")
    print(f"Annual Salary   :       {annual_salary}")
    print(f"Bonus           :       {annual_bonus}\n")

def main():
    print_title()
    employee_name = get_employee_name()
    employee_salary = get_monthly_salary()
    display_salary_report(employee_name, employee_salary)

    print("Thank you for using Employee Salary Calculator.\n")


main()