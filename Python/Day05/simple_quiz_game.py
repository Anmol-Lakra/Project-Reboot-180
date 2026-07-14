print("=" * 40)
print("             Simple Quiz Game        ")
print("=" * 40)
print()

# Edge Cases:
# 1. User can enter numbers/special characters
# 2. User can enter blank space at front and back of the choice 
# 3. User can enter space between the alphabets
# 4. user can enter a blank space 

question_number = 0
correct_answers = 0


can_start_quiz = True

while True:
    print("There are 5 questions.")
    print("Each correct answer earns 1 point.")
    enter_to_start = input("Press Enter to start...\n")
    if enter_to_start == "":
        break
    else:
        print("Invalid input\n")

# Question number 1:
question_number = question_number + 1
while True: 
    print(f"Question {question_number} of 5\n")
    print("What is the capital of India?\n")
    print("A. Delhi")
    print("B. Mumbai")
    print("C. Chennai")
    print("D. Kolkata\n")
    answer = input("Your Answer: ").strip().upper()
    if answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("Invalid choice - Please enter A, B, C or D.\n")
        continue
    elif answer == "A":
        print("Correct!\n")
        correct_answers = correct_answers + 1
        break
    else:
        print("Incorrect!")
        print("\nCorrect Answer: A\n")
        break

# Question number 2:
question_number = question_number + 1
while True: 
    print(f"Question {question_number} of 5\n")
    print("What is the national animal of India?\n")
    print("A. Lion")
    print("B. Tiger")
    print("C. Elephant")
    print("D. Peacock\n")
    answer = input("Your Answer: ").strip().upper()
    if answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("Invalid choice - Please enter A, B, C or D.\n")
        continue
    elif answer == "B":
        print("Correct!\n")
        correct_answers = correct_answers + 1
        break
    else:
        print("Incorrect!")
        print("\nCorrect Answer: B\n")
        break

# Question number 3:
question_number = question_number + 1
while True: 
    print(f"Question {question_number} of 5\n")
    print("What is the national currency of India?\n")
    print("A. Dollar")
    print("B. Euro")
    print("C. Rupee")
    print("D. Yen\n")
    answer = input("Your Answer: ").strip().upper()
    if answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("Invalid choice - Please enter A, B, C or D.\n")
        continue
    elif answer == "C":
        print("Correct!\n")
        correct_answers = correct_answers + 1
        break
    else:
        print("Incorrect!")
        print("\nCorrect Answer: C\n")
        break

# Question number 4:
question_number = question_number + 1
while True: 
    print(f"Question {question_number} of 5\n")
    print("Which is the longest river in India?\n")
    print("A. Yamuna")
    print("B. Godavari")
    print("C. Ganga")
    print("D. Narmada\n")
    answer = input("Your Answer: ").strip().upper()
    if answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("Invalid choice - Please enter A, B, C or D.\n")
        continue
    elif answer == "C":
        print("Correct!\n")
        correct_answers = correct_answers + 1
        break
    else:
        print("Incorrect!")
        print("\nCorrect Answer: C\n")
        break 

# Question number 5:
question_number = question_number + 1
while True: 
    print(f"Question {question_number} of 5\n")
    print("How many states are there in India?\n")
    print("A. 28")
    print("B. 29")
    print("C. 30")
    print("D. 27\n")
    answer = input("Your Answer: ").strip().upper()
    if answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("Invalid choice - Please enter A, B, C or D.\n")
        continue
    elif answer == "A":
        print("Correct!\n")
        correct_answers = correct_answers + 1
        break
    else:
        print("Incorrect!")
        print("\nCorrect Answer: A\n")
        break 

print("=" * 40)      
print("\nQuiz Finished!\n")
print(f"Correct Answers     :       {correct_answers}")
print(f"Wrong Answers       :       {5-correct_answers}")
print(f"Final Score         :       {correct_answers}/5\n")
print("=" * 40) 

print("\nThank you for using Simple Quiz Game\n")
