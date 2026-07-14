print("=" * 40)
print("    Rock Paper Scissors - Version 1")
print("=" * 40)
print()

# Edge cases:
# 1. User can enter a blank input
# 2. User can input a different word/number/special charcters/decimal numbers
# 3. User can enter gaps between words
# 4. User can enter special characters between words
# 5. User can enter spaces at the begining or the end of the word
# 6. User can enter in different cases 

player1_score = 0
player2_score = 0
draw_matches = 0
match_counter = 0

while True:

    is_valid_choice = True
    
    # Input Chcek for Player 1:
    while is_valid_choice:
        print("Player 1 Selection:")
        print("*" * 20)
        print("Rock")
        print("Paper")
        print("Scissors\n")

        player1_choice = input("Enter your choice Player 1: ").strip().upper()
        if player1_choice != "ROCK" and player1_choice != "PAPER" and player1_choice != "SCISSORS":
            print("Invalid choice - Choose either 'Rock' or 'Paper' or 'Scissors'\n")
        else:
            is_valid_choice = False
            print()

     # Input Chcek for Player 2:
    is_valid_choice = True

    while is_valid_choice:
        print("Player 2 Selection:")
        print("*" * 20)
        print("Rock")
        print("Paper")
        print("Scissors\n")

        player2_choice = input("Enter your choice Player 2: ").strip().upper()
        if player2_choice != "ROCK" and player2_choice != "PAPER" and player2_choice != "SCISSORS":
            print("Invalid choice - Choose either 'Rock' or 'Paper' or 'Scissors'\n")
        else:
            is_valid_choice = False
            print()

    # Match:
    match_counter = match_counter + 1
    print(f"            Match {match_counter}:")
    print("*" * 33)
    print("Rock Paper Scissors - Shoot....\n")
    print(f"Player 1 chose     :       {player1_choice}")
    print(f"Player 2 chose     :       {player2_choice}\n")

    if player1_choice == "ROCK" and player2_choice == "SCISSORS":
        print("Player 1 Wins!\n")
        player1_score = player1_score + 1
    elif player1_choice == "PAPER" and player2_choice == "ROCK":
        print("Player 1 Wins!\n")
        player1_score = player1_score + 1
    elif player1_choice == "SCISSORS" and player2_choice == "PAPER":
        print("Player 1 Wins!\n")
        player1_score = player1_score + 1
    elif player2_choice == "ROCK" and player1_choice == "SCISSORS":
        print("Player 2 Wins!\n")
        player2_score = player2_score + 1
    elif player2_choice == "PAPER" and player1_choice == "ROCK":
        print("Player 2 Wins!\n")
        player2_score = player2_score + 1
    elif player2_choice == "SCISSORS" and player1_choice == "PAPER":
        print("Player 2 Wins!\n")
        player2_score = player2_score + 1
    else:
        print("It's a Draw!\n")
        draw_matches = draw_matches + 1


    # Scores:
    print(f"            Scores:")
    print("*" * 33)
    print(f"Matches played     :       {match_counter}")
    print(f"Player 1 wins      :       {player1_score}")
    print(f"Player 2 wins      :       {player2_score}")
    print(f"Draw matches       :       {draw_matches}\n")

    if player1_score > player2_score:
        print(f"Player 1 is leading by {player1_score - player2_score} points.")
    elif player2_score > player1_score:
        print(f"Player 2 is leading by {player2_score - player1_score} points.") 
    else:
        print(f"It's a draw!")

    print("*" * 33)
    print()

    # Continue game:
    continue_game = True
    while continue_game:
        play_again = input("Play Again? [Y/N]: ").strip().upper()
        if play_again != "Y" and play_again != "N":
            print("Invalid choice - Please enter [Y/N]")
        else:
            continue_game = False
            print()

    if play_again == "N":
        if player1_score > player2_score:
            print("The Champion of 'Rock' 'Paper' 'Scissors' tournament is Player 1\n")
        elif player2_score > player1_score:        
            print("The Champion of 'Rock' 'Paper' 'Scissors' tournament is Player 2\n")
        else:
            print("The Tournament ended in a nail biting draw!\n")
        break  

print("Thank you for using Rock Paper Scissors - Version 1.\n")  