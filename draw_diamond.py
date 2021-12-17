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
