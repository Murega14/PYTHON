import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice((choices))

    player = None
    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    if computer == player:
        print("computer: ", computer)
        print("player:", player)
        print("Tie")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose haha")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you win hooray")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win hooray")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose haha")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose haha")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win hooray")
    play_again = input("do you want to play again? (yes/no?): ").lower()

    if play_again != "yes":
        break

print("bye")    