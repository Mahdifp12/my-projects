import os
os.system("clear")

def decrypt():
    result_list = []
    result_decrypt = []

    print("Hey, for decrypt your word Enter number encrypted . . . \nIf you enter three to zero, you will exit the inputs and see the result")
    
    while True:
        user_num = int(input("Enter number: "))
        if user_num == 000:
            break

        result_list.append(user_num)

    for i in result_list:
        num = i - 4351
        result_decrypt.append(chr(num))

    for word in result_decrypt:
        print(word, end='')

decrypt()