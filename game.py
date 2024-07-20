import random

def rps_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return "Draw"
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins"
    return "Computer wins"

print(rps_game("rock"))
print(rps_game("paper"))
print(rps_game("scissors"))
