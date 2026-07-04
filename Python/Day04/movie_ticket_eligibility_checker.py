print("=" * 42)
print("     Movie Ticket Eligibility Checker    ")
print("=" * 42)
print()

# Edge cases:
# 1. User can enter a nothing in name, age or movie rating
# 2. User can enter numbers/special characters instead of name or movie rating 
# 3. There can be gaps at the start, end or in the middle of the name, age or movie rating 
# 4. User can enter alphabets/special charcters in age
# 5. User enter more than maximum age (150 is upper age limit)
# 6. user enter negative age
# 7. User enters the exact age 0
# 8. User enters the exact age 150
# 9. User enters the exact age 13
# 10.User enters the exact age 18 
# 11.User enters age as decimal

user_name = input("Enter your name: ").strip().title()

if user_name == "":
    print("\nInvalid Name - Please enter valid name.\n")
else:

    user_age = input("Enter your age: ").strip()
    if user_age == "":
        print("\nInvalid Age - Please enter valid age.\n")
    elif user_age.find(" ") != -1:
        print("\nBlank space between age - please enter valid age.\n")
    elif user_age.find(".") != -1:
        print("\nNo decimal allowed - Please enter your valid age\n")    
    elif user_age[0] == "-":
        print("\nAge cannot be negative - Please enter valid age\n")
    elif int(user_age) > 150:
        print("\nAge cannot exceed 150 years.\n")
    else:

        movie_rating = input("Enter Movie Rating (U / UA / A): ").strip().upper()
        if movie_rating == "":
            print("\nInvalid Movie Rating - Please enter valid Movie Rating.\n")
        elif movie_rating.find(" ") != -1:
            print("\nBlank space between Movie Rating - please enter valid Movie Rating.\n")
        elif movie_rating.find("-") != -1:
            print("\nInvalid Movie Rating - Please enter valid Movie Rating\n")
        elif movie_rating != "A" and movie_rating != "UA" and movie_rating != "U":
            print("\nInvalid alphabet for rating - Please enter valid rating.\n")   
        else:

            user_age = int(user_age)

            print("     Movie Ticket Report     ")
            print("*" * 30)

            print(f"Name            :       {user_name}")
            print(f"Age             :       {user_age}")
            print(f"Movie Rating    :       {movie_rating}")

            if movie_rating == "A":
                if user_age >= 18:
                    print(f"Status          :       Eligible")
                    print("Enjoy the movie.\n") 
                else:
                    print(f"Status          :       Not Eligible")
                    print("You need to be at least 18 years old.\n")
            elif movie_rating == "UA":
                if user_age >= 13:
                    print(f"Status          :       Eligible")
                    print("Enjoy the movie.\n")
                else:
                    print(f"Status          :       Not Eligible")
                    print("You need to be at least 13 years old.\n")
            else:
                print(f"Status          :       Eligible")
                print("Enjoy the movie.\n")               
                 
print("Thank you for using Movie Ticket Eligibility Checker.\n")                 