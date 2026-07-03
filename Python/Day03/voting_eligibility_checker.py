print("=" * 40)
print("     Voting Eligibility Checker      ")
print("=" * 40)
print()

# Edge case
# 1. Since the input will also be in string format, so it is difficult to find out if the user has genuinely entered a number,
#   alphabets, special characters or a blank input

age = input("Enter your age: ").strip()

if age == "":
    print("\nEmpty Input - Please retry again with valid age")
else:
    blank_space_value = age.find(" ")
    if blank_space_value != -1:
       print("\nSpace between numbers -  please retry again with valid age")
    else:
        if age[0] == "-":
           print("\nNegative input - please retry again with valid age")
        else:
            integer_age =  int(age)
            if integer_age >= 18:
                print("\nYou are eligible to vote.")
            else:
                print("\nYou are not eligible to vote.")

print("\nThank you for using Voting Eligibility Checker!\n")  
      



 
        