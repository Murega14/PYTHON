#used because:
#1. module can be run as a standalone program
#2. module can be imported and used by other modules
# the python interpreter sets "special variables" one of which is __name__
#python will assign the __name__ variable a value of '__main__" if its the initial module being run
import random
def main():
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

if __name__ == '__main__':
    main()