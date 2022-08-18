# First import random
import random

user_score = 0
computer_score = 0
turns = 0

# You can change the number of turns you want to play the game from here.
total_turns = 20
print("Welcome to my rock, paper, scissors game")

while True and turns < total_turns:
    turns += 1
    game_parameters = ["rock", "paper", "scissors"]
    
    computer_turn = random.choice(game_parameters)
    
    user = input("Type rock, paper or scissors to play or type (q) to end: ").lower()

    if user in game_parameters:
        computer_turn
    elif user == "q":
        print("You quit. Bye!")
        # To prevent the while loop from running infinitely, use 
        break
    else:
        print("Please type a valid input.")
        continue
    
    if user == "rock" and computer_turn == "scissors":
        print("Computer chose", computer_turn + ". You win!")
        user_score += 1
    elif user == "paper" and computer_turn == "rock":
        print("Computer chose", computer_turn + ". You win!")
        user_score += 1
    elif user == "scissors" and computer_turn == "paper":
        print("Computer chose", computer_turn + ". You win!!")
        user_score += 1
    elif user == computer_turn:
        print("Computer chose", computer_turn + ". It's a tie!")
    else:
        print("Computer chose", computer_turn + ". Computer wins!")
        computer_score += 1
    
print("You won", str(user_score) + " times and tied", str(total_turns - (user_score + computer_score)), "times, while the computer won", str(computer_score) + " times.")
if user_score > computer_score:
    print("You win.")
elif user_score < computer_score:
    print("The computer wins")
else:
    print("It's a tie.")
