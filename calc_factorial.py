
#? 3! = 1 * 2 * 3

def calc_factorial(num):
    sum_fact = 1

    for i in range(num):
        sum_fact *= (i + 1)

    return sum_fact

print(calc_factorial(3))

###########################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from random import randint

number = randint(1, 20)

def calc_factorail(f):
    sum_factorail = 1
    
    for i in range(f):
        sum_factorail *= (i + 1)

    print(sum_factorail)

print(f'Number: {number}')
print("this is down calculate factorial:")
calc_factorail(number)


#***********************************************************

def calc_factorial(num):
    if num == 1:
        return 1
    return num * calc_factorial(num-1)

print(calc_factorial(5))