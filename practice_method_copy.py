def get_input():
    list_of_words = []
    while True:
        user_input = input("Enter your word: ")
        if user_input == "done":
            break
        elif user_input.isalpha():
            list_of_words.append(user_input)
        else:
            print("your input is invalid")

    return list_of_words

list_of_words = get_input()

def change_of_list(list_for_change):
    copied_list = list_for_change.copy()
    copied_list.reverse()

    return copied_list

print(list_of_words)
print(change_of_list(list_of_words))
print(list_of_words)