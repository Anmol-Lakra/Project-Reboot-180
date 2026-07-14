print("=" * 43)
print("     Number Guessing Game - Version 2        ")
print("=" * 43)
print()

# Edge cases:
# 1. User can enter a blank
# 2. User can enter a alphabet or a special character
# 3. User can enter a negative number
# 4. User can input a decimal number
# 5. User can input the number more than the range (range is 1-10)
# 6. User can give blank spaces at the starting or the end of the number
# 7. User can enter space between numbers

print("\n       Range of number  - 1 to 10")
print("*" * 43)
print()

secret_number = input("Enter the secret number: ").strip()

if secret_number == "":
    print("\nInvalid number - secret number cannot be blank\n")
elif secret_number.find(" ") != -1:
    print("\nInvalid number - secret number cannot have blank in between the digits\n")
elif secret_number.find(".") != -1:
    print("\nInvalid number - secret number cannot be a decimal number\n")
else:
    secret_number = int(secret_number)
    if secret_number < 1 or secret_number > 10:
        print("\nInvalid number - Secret number is out of range\n")
    else:    

        correct_guess = False
        no_of_attempts = 0

        while True:
            user_guess = input("\nGuess the number (Range 1-10): ").strip()
            if user_guess == "":
                print("\nInvalid number - number cannot be blank\n")
            elif user_guess.find(" ") != -1:
                print("\nInvalid number - number cannot have spaces between them\n")
            elif user_guess.find(".") != -1:
                print("\nInvalid number - number cannot be decimal\n")
            else:
                user_guess = int(user_guess)    
                
                if user_guess < 1 or user_guess > 10:
                    print("\nOut of range - Please guess within the range\n")
                elif user_guess == secret_number:
                    print("Correct!\n")
                    no_of_attempts = no_of_attempts + 1
                    correct_guess = True
                    break
                elif user_guess < secret_number:
                    no_of_attempts = no_of_attempts + 1
                    print("Too Low!\n")
                else:
                    no_of_attempts = no_of_attempts + 1
                    print("Too High!\n")
        if correct_guess:
            print(f"You guessed the number in {no_of_attempts} attempts\n")

            if no_of_attempts >= 5:
                print("Good Persistence!\n")
            elif no_of_attempts >= 2:
                print("Great Job!\n")
            else:
                print("Excellent!\n")         

print("Thank You for using Number Guessing Game - Version 2\n")


