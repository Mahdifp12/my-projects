import os
os.system("clear")


list_numbers = ['114', '32', '45', '78', '10', '21']

def get_input():
    while True:
        user_input = input("Enter your guess: ")

        if user_input.isdigit():
            return user_input
        
        print("your input not correct")

def print_information_game():
    print("Hello , welcome to the game!")
    print(f"list of numbers : {list_numbers}")
    print('please enter your guess')
    print(f"your chances are is 3")

def settings(numbers, chance_user):
    print_information_game()
    correct_number = numbers[0]
    
    for i in range(chance_user):
        user_number = get_input()
        if user_number == correct_number:
            print("YOU WON !")
            return
        
        else:
            print(f"your choice is not correct && your chance for choice {chance_user - i - 1}")

settings(list_numbers, 3)