import random
# List of options
options = ["rock", "paper", "scissors"]
# Computer chooses a random option
computer_choice = random.choice(options)
# Get user input
user_choice = input("Enter rock, paper, or scissors: ")
# Check for invalid input
if user_choice not in options:
    print("Invalid input")
else:
    # Print user and computer choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    # Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    # Check for user win
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    # Otherwise, computer wins
    else:
        print("Computer wins!")
