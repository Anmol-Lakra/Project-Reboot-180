print("=" * 40)
print("      ATM PIN Verification System")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter a blank/nothing
# 2. User can enter a alphabets/special characters
# 3. User can enter a negative number
# 4. User can enter a decimal number
# 5. User can enter a "-" in between
# 6. User can give a pin more than 4 digits or less than 4 digits
# 7. User can give a space between the pin
# 8. User can give blank spaces at the begining or the end of the pin

secret_pin = "1234"

user_attempt = 0

while user_attempt < 3:
    user_pin = input("Enter pin: ").strip()
    user_pin_length = len(user_pin)
    
    if user_pin == "":
        print("\nInvalid pin - pin cannot be blank\n")
        continue
    elif user_pin_length != 4:
        print("\nInvalid pin - the pin length should be 4 digits\n")
        continue
    elif user_pin[0] == "-":
        print("\nInvalid pin - pin cannot be a negative number\n")  
        continue   
    elif user_pin.find("-") != -1: 
        print("\nInvalid pin - pin cannot have a - in between digits\n")
        continue
    elif user_pin.find(" ") != -1:
        print("\nInvalid pin - pin cannot have a blank space between the digits\n") 
        continue 
    elif user_pin.find(".") != -1:
        print("\nInvalid pin - pin cannot be a decimal number\n")
        continue
    else:
        user_attempt += 1

        if user_pin == secret_pin:
            print("Access Granted\n")
            break
        else:
            print("Incorrect PIN\n")

            if user_attempt == 3:
                print("Card Blocked\n")
                break

            print(f"Attempts remaining {3-user_attempt}\n")

print("Thank you for using ATM PIN Verification System\n")
        