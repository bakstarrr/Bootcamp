import random

Your_score = 0
AI_score = 0
Draws = 0

while True:
    user_action=input("Enter a choice (rock, paper, scissors): ")

    possible_actions=["rock", "paper", "scissors"]
    computer_action=random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It`s a tie!")
        Draws=Draws+1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
            Your_score=Your_score+1
        else:
            print("You lose!")
            AI_score=AI_score+1
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
            Your_score=Your_score+1
        else:
            print("You lose.")
            AI_score=AI_score+1
    elif user_action == "scissors":
        if computer_action == ("paper"):
            print("You win!")
            Your_score=Your_score+1
        else:
            print("You lose.")
            AI_score=AI_score+1
    print("Your score: "+str(Your_score))
    print("Computer score: " + str(AI_score))
    print("Ties: " + str(Draws))
    play_again = input("Play again? (y/n): ")
    if play_again.lower() !="y":
        break 
