import os
os.system("clear")


list_of_words = ["tree", "git", "python", "javascript", "csharp", "cpp", "oop", "java", "kotlin", "php"]

def print_stars():
    print("*" * 25)

def get_inputs():
    while True:
        user_input = input("Enter your word: ").lower()
        if user_input.isalpha():
            return user_input
        print_stars()
        print("your input invalid\nplease using accepted words")
        print_stars()

def print_info_game(words):
    print_stars()
    print("Hello, welcome to the this is game (Guess the words)")
    print(f"Please enter input word of list: {words}")
    print_stars()


def check_input_in_list_word(words):
    user_guess = get_inputs()
    
    while user_guess not in words:
        print_stars()
        print("your word input invalid\nnot in on the list words")
        print_stars()

        user_guess = get_inputs()

    return user_guess

def run_game(words, number_of_rounds):
    print_info_game(words)
    correct_word = words[2]
    
    print_stars()
    print(f"number of gusses: {number_of_rounds}")
    print_stars()
    
    for i in range(number_of_rounds):

        word_user = check_input_in_list_word(words)

        if word_user == correct_word:
            print("You Won !")
            return
        
        print_stars()        
        print(f"Your input word not correct\nTry agin your number of rounds : {number_of_rounds-1 - i}")
        print_stars()
        continue
    
    print_stars()
    print(f"You Lost!\nword is correct: {correct_word}")
    print_stars()

run_game(list_of_words, 5)