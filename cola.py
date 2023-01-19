# ----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("#----------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D: " )
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
#-----------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
    
#-----------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------------------")
    print("RESULTS")
    print("===============================================")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = ((correct_guesses/len(questions))*100)
    score_2 = int(score)
    print("Your score is :"+str(score_2)+"%")

    
#-----------------------
def play_again():

    response = input("Do you want to play again?: (yes/no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-----------------------

questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group": "C",
    "Is the earth round?(yes/no): " : "A"
}

options = [["A. Guido Van Rossum", "B. God", "C. Linus Torvald"],
            ["A. 1989", "B. 1991", "C. 1963", "D. 2002"],
            ["A. Lonely Island", "B. B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. Yes", "B. No", "C. Flat", "D. Maybe"]
]

new_game()

while play_againa():
    new_game()


print("bye bye loser")