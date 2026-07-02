print("=" * 40)
print("         Phone Number Masking            ")
print("=" * 40)
print()

phone_number = input("Enter your phone number: ").strip()
no_of_digits = len(phone_number)

masked_digits = "*" * (no_of_digits - 4)
nos_visible = phone_number[-4:]
print()

print(f"The masked phone number : {masked_digits}{nos_visible}\n")

print("Thank you! for using Phone Number Masking to secure your privacy\n")



