def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input(" Enter (A, B, C, or D").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        pritn ("Wrong!")
        return 0
def display_score():
    pass
def play_again():
    pass

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