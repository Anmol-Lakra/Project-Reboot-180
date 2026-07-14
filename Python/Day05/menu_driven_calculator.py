print("=" * 40)
print("         Menu Driven Calculator      ")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter a alphabet/special character in menu selection and number input for calculation
# 2. User can enter a blank space in menu selection and number input for calculation
# 3. User can enter a negative number in menu selection 
# 4. User can enter a decimal number in menu selection
# 5. User can enter blank spaces between the digits or at the end or at the starting of digits
# 6. User can enter blank space between the digits of numbers input for calculation
# 6. User can enter the second number to be 0 in division

calculations_performed = 0

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")

    menu_choice = input("Enter your choice: ").strip()

    if menu_choice == "":
        print("\nInvalid choice - Menu choice cannot be blank\n")
        continue
    elif menu_choice.find(" ") != -1:
        print("\nInvalid number - Menu choice cannot have a blank space between digits\n") 
        continue    
    elif menu_choice.find(".") != -1:
        print("\nInvalid number - Menu choice cannot be decimal\n")
        continue
    else:
        menu_choice = int(menu_choice)    

        if menu_choice < 1 or menu_choice > 5:
            print("\nInvalid choice - Please choose correct menu choice\n")
            continue
        elif menu_choice == 1:
            mathemetical_operation = 1
        elif menu_choice == 2:
            mathemetical_operation = 2
        elif menu_choice == 3:
            mathemetical_operation = 3
        elif menu_choice == 4:
            mathemetical_operation = 4
        else:
            break


        # Validating number 1:        

        number1_validator = True

        while number1_validator:
            user_input1 = input("Enter first number: ").strip()
            if user_input1 == "":
                print("\nInvalid number - the number cannot be blank\n")
                continue
            elif user_input1.find(" ") != -1:
                print("\nInvalid number - the number cannot have balnk spaces between digits\n") 
                continue
            elif user_input1[0] != "-" and user_input1.find("-") != -1:
                print("\nInvalid number - the number cannot have a '-' in between\n")
                continue
            elif user_input1.find(".") != -1:
                user_input1 = float(user_input1)
                number1_validator = False
            else:
                user_input1 = int(user_input1) 
                number1_validator = False   
                       
        # Validating number 2:

        number2_validator = True

        while number2_validator:
            user_input2 = input("Enter second number: ").strip()
            if user_input2 == "":
                print("\nInvalid number - the number cannot be blank\n")
            elif user_input2.find(" ") != -1:
                print("\nInvalid number - the number cannot have blank spaces between digits\n") 
            elif user_input2[0] != "-" and user_input2.find("-") != -1:
                print("\nInvalid number - the number cannot have a '-' in between\n")
            elif user_input2.find(".") != -1:
                user_input2 = float(user_input2)
                number2_validator = False
            else:
                user_input2 = int(user_input2)     
                
                if menu_choice == 4 and user_input2 == 0:
                    print("\nInvalid number - In a division denominator cannot be 0\n")
                    continue
                else:
                    number2_validator = False

    # Performing the calculation

    if mathemetical_operation == 1:
        print(f"\nAddition of {user_input1} and {user_input2}         :       {user_input1 + user_input2}\n")
    elif mathemetical_operation == 2:
        print(f"\nSubtraction of {user_input1} and {user_input2}      :      {user_input1 - user_input2}\n")  
    elif mathemetical_operation == 3:
        print(f"\nMultiplication of {user_input1} and {user_input2}   :       {user_input1 * user_input2}\n")
    elif mathemetical_operation == 4:
        print(f"\nDivision of {user_input1} by {user_input2}          :       {user_input1/user_input2}\n")
        

    calculations_performed = calculations_performed + 1
    print("-" * 40)
    print()

    # Check if the user wants to continue or not

    check_input = True
    while check_input:
        perform_another_calculation = input("Do you want to perform another calculation? [Y/N]\n").strip().upper()
        if  perform_another_calculation != "Y" and perform_another_calculation != "N":    
            print("Invalid answer - Please enter correct choice [Y/N]\n")
            continue
        else:
            check_input = False

    if perform_another_calculation == "N":
        break


print(f"\nYou performed {calculations_performed} calculations.\n") 

print("Thank you for using Menu Driven Calculator\n")




          