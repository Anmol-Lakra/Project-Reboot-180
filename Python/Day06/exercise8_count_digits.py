print("Exercise 8 — Count Digits")
print()
text = "Python123AI45"
count_digits = 0
for char in text:
    if char.isdigit():
        count_digits += 1
        
print(f"Digits = {count_digits}")