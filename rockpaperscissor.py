import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of a single round."""
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def print_round_result(player_choice, computer_choice, result):
    """Print the result of the round."""
    outcomes = {
        'draw': "It's a draw!",
        'player': "You win!",
        'computer': "You lose!"
    }
    print(f"\nYou chose: {player_choice}")
    print(f"The computer chose: {computer_choice}")
    print(outcomes[result])

def play_game():
    """Play the Rock, Paper, Scissors game."""
    scores = {'player': 0, 'computer': 0}
    
    while True:
        print("\nRock, Paper, Scissors!")
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").strip().lower()
        
        if player_choice == 'quit':
            break
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        if result == 'player':
            scores['player'] += 1
        elif result == 'computer':
            scores['computer'] += 1
        
        print_round_result(player_choice, computer_choice, result)
        
        print("\nScore:")
        print(f"You: {scores['player']}")
        print(f"Computer: {scores['computer']}")
    
    print("\nFinal Score:")
    print(f"You: {scores['player']}")
    print(f"Computer: {scores['computer']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
