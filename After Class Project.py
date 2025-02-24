import random
import time

# Function to display the welcome message
def welcome_message():
    print("Welcome to the Rock, Paper, Scissors game!")
    print("You will be playing against the computer.")
    print("The rules are simple:")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")

# Function to get the player's choice
def get_player_choice():
    while True:
        print("Choose one of the following: Rock, Paper, or Scissors.")
        player_choice = input("Enter your choice: ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


def play_round():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {player_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    result = determine_winner(player_choice, computer_choice)
    print(f"Result: {result}\n")

    return result

# Function to play the entire game, including multiple rounds
def play_game():
    player_wins = 0
    computer_wins = 0
    ties = 0
    welcome_message()
    while True:
        result = play_round()
        if result == "You win!":
            player_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1
        else:
            ties += 1
        print(f"Score: You - {player_wins}, Computer - {computer_wins}, Ties - {ties}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing!")
    print(f"Final Score: You - {player_wins}, Computer - {computer_wins}, Ties - {ties}")
    if player_wins > computer_wins:
        print("You are the overall winner!")
    elif computer_wins > player_wins:
        print("The computer is the overall winner!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()
