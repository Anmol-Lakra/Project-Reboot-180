print("=" * 45)
print("       Number Guessing Game - ver.1          ")
print("=" * 45)
print()

# Edge case:
# 1. alphabets/special characters can be entered which is wrong for the game

secret_number = 7

number_guessed = input("Guess the number: ").strip()
print()

if number_guessed == "":
    print("No number was guessed - Please guess again.\n")
elif number_guessed[0] == "-":
    print("Wrong guess - the number is positive.\n")
elif number_guessed.find(" ") != -1:
    print("Invalid number - no space between numbers.\n")
elif number_guessed.find(".") != -1:
    print("It is not a Decimal number - try again.\n")
elif int(number_guessed) >=20:
    print("Very large number - guess with smaller number.\n")     
else:
    number_guessed = int(number_guessed)
    if number_guessed < secret_number:
        print("Too Low!\n")
    elif number_guessed > secret_number:
        print("Too High!\n")
    else:
        print("🎉 Congratulations!")
        print("You guessed the correct number.\n") 

print("Thank You for using Number Guessing Game - ver.1 \n")          