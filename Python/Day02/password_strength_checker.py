print("=" * 43)
print("         Password Strength Checker           ")
print("=" * 43)
print()

# Edge cases
# 1. The user can give a blank input
# 2. At this moment we cannot determine the password is strong or weak length wise
# 3. At this moment we cannot determine the password is strong or weak as we cannot check that
#   atleast 1 Capital letter, 1 number and 1 special charcter is used or not

user_password = input("Enter your password: ").strip()
print()

print(f"Password Length :   {len(user_password)}")
print(f"First Charcter  :   {user_password[0]}")
print(f"Last Character  :   {user_password[-1]}")
print(f"Reversed        :   {user_password[::-1]}\n")

print("Thank You for using Password Strength Checker!\n")