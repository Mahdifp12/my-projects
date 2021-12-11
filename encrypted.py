import os
os.system("clear")

word_user = input("Enter your words: ")

def encrypt(full_name):
    result_list = []

    for i in full_name:
        result_list.append(ord(i) + 4351)

    for n in result_list:
        print(n, end=" ")

encrypt(word_user)