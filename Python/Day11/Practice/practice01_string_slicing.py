print("=" * 40)
print("      Practice 01 - String Slicing")
print("=" * 40)
print()

text = "HELLO"

print(f"1st way - The first character of {text}   :   {text[:1]}")
print(f"2nd way - The first character of {text}   :   {text[-5::-1]}")
print(f"1st way - The last character of {text}    :   {text[-1:]}")
print(f"2nd way - The last character of {text}    :   {text[-1:-2:-1]}\n")

print(f"1st way - Remove the 1st character from {text}  :   {text[1:]}")
print(f"2nd way - Remove the 1st character from {text}  :   {text[-4:]}")
print(f"1st way - Remove the last character for {text}  :   {text[:4]}")
print(f"2nd way - Remove the last character for {text}  :   {text[-5:-1]}\n")

print(f"1st way - Take out the middle characters of {text}  :   {text[1:4]}")
print(f"2nd way - Take out the middle characters of {text}  :   {text[-4:-1]}\n")

second_text = "ABCDEFGHIJ"

print(f"1st way - Every 2nd character from the string {second_text}     :   {second_text[0::2]}")
print(f"2nd way - Every 2nd character from the string {second_text}     :   {second_text[-10::2]}\n")

print(f"Reverse of the string {text} using slicing       :   {text[::-1]}")
