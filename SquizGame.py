def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    guess_validation = ["A", "B", "C", "D"]

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = None

        while guess not in guess_validation:
            guess = input(" Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print ("Wrong!")
        return 0
def display_score(correct_guesses, guesses):
    print("Results")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)

    print(str(score) + "%")

def play_again():
    
    play_again_validation = ["yes", "no"]
    response = None
    while response not in play_again_validation:
        response = input(" Do you want to play again?: (yes or no) ").lower()
    if response == "yes":
        return True
    else:
        return False

#Use a dictionary to hold the questions and answers
questions = {
    "What data set type is changeable, unordered, and a collection of key:value pairs" : "A",
    "What data set type is a collection of ordered, unchangeable, and related data" : "B",
    "What data set type is a collection of unordered, unindexed, and no duplicate values": "C"
}

options =   [["A: Dictionary", "B: 2DList", "C: Tuple", "D: Set"],
            ["A: Set", "B: Tuple", "C: 2DList", "D: Dictionary"],
            ["A: 2DList", "B: Dictionary", "C: Set", "D: Tuple"]]

new_game()

while play_again():
    new_game()