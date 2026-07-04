print("=" * 40)
print("             ATM Pin Checker             ")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter nothing
# 2. User can enter alphabets/special characters
# 3. User can enter only space 
# 4. User can leave a gap between the pin 
# 5. User can enter a decimal number
# 6. User can enter negative number
# 7. User can enter less than 4 digits
# 8. User can enter more than 4 digits

correct_pin = "1234"

entered_pin = input("Enter your pin number: ").strip()

pin_length = len(entered_pin) 
if pin_length == 0:
    print("\nInvalid pin - Please enter valid pin.\n")
elif entered_pin[0] == "-":
    print("\nInvalid pin - Pin cannot be negative\n") 
elif entered_pin.find(".") != -1:
    print("\nInvalid pin - Pin cannot be decimal\n") 
elif entered_pin.find(" ") != -1:
    print("\nInvalid pin - Space cannot be between pin number\n")
elif pin_length != 4:
    print("\nInvalid Pin - Please enter 4 digit pin.\n") 
     
else:
    print()

    print("     ATM Verification Report:        ")
    print("*" * 35)

    print(f"Entered pin         :       {'*' * pin_length}")
    print(f"Pin Length          :       {pin_length}")    

    if entered_pin == correct_pin:
        print("Status              :       Access Granted")
        print("Thank You for using the ATM.\n")
    else:
        print("Status              :       Access Denied")
        print("Incorrect pin\n")

print("Thank You for using ATM Pin Checker.\n")
        