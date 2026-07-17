print("=" * 45)
print("Mini Project 4 — Pattern Designer (Capstone)")
print("=" * 45)
print()

# Edge case:
# 1. User can enter blank
# 2. User can enter alphabets/special characters
# 3. User can enter 0
# 4. User can enter decimal numbers
# 5. user can enter only whitespace as input

while True:

    choice_is_invalid = True
    while choice_is_invalid:
        print("=" * 30)
        print("       Pattern Generator")
        print("=" * 30)
        print()

        print("1. Rectangle")
        print("2. Triangle")
        print("3. Inverted Triangle\n")

        user_choice = input("Enter choice: ").strip()
        if user_choice == "":
            print("Invalid choice - Choice cannot be blank.\n")
        elif user_choice.isdigit() == False:
            print("Invalid choice - Please choose option 1, option 2 or option 3.\n")
        elif user_choice == "0":
            print("Invalid choice - Please choose option 1, option 2 or option 3.\n")
        elif int(user_choice) > 3:
            print("Invalid choice - Please choose option 1, option 2 or option 3.\n")
        else:
            choice_is_invalid = False
            print()

    user_chose_rectangle = False
    user_chose_triangle = False
        
    if user_choice == "1":

        user_chose_rectangle = True
        input_invalid = True

        while input_invalid:
            rows = input("Enter rows: ").strip()
            if rows == "":
                print("Invalid input - Rows cannot be blank.\n")
            elif rows.isdigit() == False:
                print("invalid input - Rows can only be positive whole numbers.\n")
            elif rows == "0":
                print("Invalid input - Rows value should be more than zero.\n")
            else:
                input_invalid = False
                print()

            

        input_invalid = True
        while input_invalid:
            column = input("Enter columns: ").strip()
            if column == "":
                print("Invalid input - Column cannot be blank.\n")
            elif column.isdigit() == False:
                print("invalid input - Column can only be positive whole numbers.\n")
            elif column == "0":
                print("Invalid input - Column value should be more than zero.\n")
            else:
                input_invalid = False
                print()

        
        rows = int(rows)
        column = int(column)
        for row in range(rows):
            for col in range(column):
                print("*", end=" ")
            print()
        print()

        
    else:
        if  user_choice == "2":
            user_chose_triangle = True

        input_invalid = True
        while input_invalid:
            height = input("Enter height: ").strip()
            if height == "":
                print("Invalid input - Height cannot be blank.\n")
            elif height.isdigit() == False:
                print("invalid input - Height can only be positive whole numbers.\n")
            elif height == "0":
                print("Invalid input - Height value should be more than zero.\n")
            else:
                input_invalid = False
                print()
            
                
        height = int(height)
        for row in range(height):
            if user_chose_triangle:
                value = row + 1
            else:
                value = height - row
            for col in range(value):
                print("*", end=" ")
            print()
        print()

    want_to_exit = False
    exit_choice_invalid = True

    while exit_choice_invalid:
        exit_choice = input("Do you want to continue: [Y/N] ").strip().upper()
        if exit_choice != "Y" and exit_choice != "N":
            print("Invalid choice - Choose [Y/N]\n")
        elif exit_choice == "Y":
            exit_choice_invalid = False
        else:
            want_to_exit = True
            break
            

    if want_to_exit:
        print()
        break
        

print("Thank you for using Pattern Designer (Capstone)\n")