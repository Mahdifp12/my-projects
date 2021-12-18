def print_star_line(number_of_stars, total_stars):
    number_of_spaces = (total_stars - number_of_stars) // 2
    print(f'{" " * number_of_spaces}{"*" * number_of_stars}{" " * number_of_stars}')

def diamond(num):
    print()
    for i in range(num):
        if i < num / 2:
            print_star_line((i * 2 + 1), num)

        else:
            print_star_line((num - i) * 2 - 1, num)

diamond(7)



# for i in range(num//2+1):
#     print(i * 2 + 1)


# num = 7


# for i in range(1, num, 2):
#     print(i)

# for j in range(0, num, 2):
#     print(num-j)


# user_num = int(input("Enter your number: "))

# def setting_number(input_num):
#     global user_num
    
#     while input_num % 2 == 0 or input_num <= 0:
#         print(f"your input invalid\nplease not enter even number or zero or less it")
#         user_num = int(input("Enter your number: "))  

#     else:
#         return input_num


# def print_of_stars(numbers_of_stars, numbers_all):
#     number_of_space = (numbers_all - numbers_of_stars) //2
#     print(f'{" " * number_of_space}{"*" * numbers_of_stars}{" " * numbers_of_stars}')
#     # print(f"{}{}{}")

# def draw_diamond(num):
      
#     print()
#     for i in range(num):
#         if i < num/2:
#             print_of_stars(i * 2 + 1, num)
#         else:
#             print_of_stars((num - i) * 2 - 1, num)

# draw_diamond(setting_number(user_num))


#? The second method

# def print_stars(number_of_stars, number_total):
#     number_of_space = (number_total - number_of_stars) // 2

#     print(f'{" " * number_of_space}{"*" * number_of_stars}{" " * number_of_space}')

# def diamond(num):
#     print()
#     for i in range(num//2+1):
#         print_stars(i * 2 + 1, num)

#     for j in range(num):
#         if j != 7 and j % 2 == 1:
#             print_stars((num - j) - 1, num)
    

# diamond(7)