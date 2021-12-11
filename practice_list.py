
def get_number_user():
    """This is work get number of user:
    
    if user is Enter "exit" loop unlock
    """

    list_of_num = []
    
    while True:
        user_number = input("Enter your number: ")

        if user_number == "exit":
            break
        
        list_of_num.append(int(user_number)) # user_number == int

    return list_of_num


def find_max_and_min_number(user_of_numbers):
    """This is function for finding the maximum and minimum number:
    
    user_of_numbers is list : for example: find_max_and_min_number([1,2,3])

    out put : (maximum, minimum)
    """
    number_max = 0

    for num in user_of_numbers:
        
        if number_max < num:
            number_max = num


    return number_max, min(user_of_numbers)

list_user_num = get_number_user()

print(find_max_and_min_number(list_user_num))