import random

MOVES = {
    "Cannonball": {"wins_against": "Cutlass", "loses_against": "Parrot"},
    "Cutlass": {"wins_against": "Map", "loses_against": "Cannonball"},
    "Map": {"wins_against": "Parrot", "loses_against": "Cutlass"},
    "Parrot": {"wins_against": "Cannonball", "loses_against": "Map"},
    "Treasure Chest": {"wins_against": None, "loses_against": None},  # Wildcard
}
def display_tutorial():
    print("\nAhoy, matey! Here be the rules of High Seas Duel:")
    print("1. Cannonball sinks Cutlass, but Parrot dodges it.")
    print("2. Cutlass slices Map, but Cannonball smashes it.")
    print("3. Map traps Parrot, but Cutlass cuts through it.")
    print("4. Parrot dodges Cannonball, but Map catches it.")
    print("5. Treasure Chest be wild! It can win or lose randomly.")
    print("Now hoist the sails and prepare for battle!\n")

def get_computer_move():
    return random.choice(list(MOVES.keys()))
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    if player_move == "Treasure Chest" or computer_move == "Treasure Chest":
        return random.choice(["player", "computer"]) 
    if MOVES[player_move]["wins_against"] == computer_move:
        return "player"
    if MOVES[player_move]["loses_against"] == computer_move:
        return "computer"
    return "tie"

def pirate_message(winner, player_move, computer_move):
    if winner == "player":
        return f"Arrr! Yer {player_move} bested the computer's {computer_move}! Victory be yers!"
    elif winner == "computer":
        return f"Blimey! The computer's {computer_move} defeated yer {player_move}! Ye lost this round!"
    else:
        return f"Shiver me timbers! Yer {player_move} and the computer's {computer_move} be evenly matched! It's a tie!"

# Main game loop
def play_game():
    print("Ahoy, matey! Welcome to High Seas Duel!")
    display_tutorial()

    player_score = 0
    computer_score = 0

    while True:
        print("\nYour Move (type 'exit' to abandon ship): ")
        player_move = input("> ").capitalize()
        
        if player_move == "Exit":
            break
        if player_move not in MOVES:
            print("Avast! That be not a valid move. Try again!")
            continue
        
        computer_move = get_computer_move()
        print(f"Computer played: {computer_move}")

        winner = determine_winner(player_move, computer_move)
        print(pirate_message(winner, player_move, computer_move))

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score: Player {player_score} - {computer_score} Computer")

    print("\nGame Over! Final Scores:")
    print(f"Player: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("Yo ho ho! Ye be the Pirate King!")
    elif player_score < computer_score:
        print("Arrr... the computer bested ye. Back to swabbin' the decks!")
    else:
        print("It be a tie! The seas respect no victor today.")
    print("Thanks for playin', matey!")
play_game()
