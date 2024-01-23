def new_game():
    guesses = []
    correct_guesses = 0
    current_question = 1
    
    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[current_question-1]:
            print(i)
        current_question+=1
        guess = input("Enter your answer (A/B/C/D) : ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
    display_score(correct_guesses,guesses)
    


def check_answer(answer, guess):
    if answer== guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
    
def display_score(correct_guesses,guess):
    print("---------------RESUT--------------")
    score = int((correct_guesses/len(questions)) * 100)
    print("Main Answer : ", end= "")
    
    for i in guess:
        print(i, end = " ")
    print()
    print("Your score is" , str(score), "%")
def play_again():
    pass

        
        
questions = {
    "Where was the first example of paper money used " : "A",
    "Which of the following languages has the longest alphabet ": "B",
    "The fear of insects is known as what " :"C",
    "Which horoscope sign is a fish? ": "A"
}

options = [
    ["A. China","B. Turkey", "C. Greece", "D. India"],
    ["A. Greece","B. Russian", "C. Arabic", "D. American"],
    ["A. Arachnophobia","B. Ailurophobia", "C. Entomophobia", "D. Aily"],
     ["A. Pisces","B. Cancer", "C. Arabic", "D. Aquarius"],
]

new_game()