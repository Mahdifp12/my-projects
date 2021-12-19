
#? روش بلند وپیچیده

# input_num = int(input("Enter a number : "))

# def is_perfect(num, list_divisors):
#     res_num = 0

#     for i in range(1, num):
#         if num % i == 0:
#           list_divisors.append(i)

#     for j in list_divisors:
#         res_num += j
    
#     def check_perfect(n):
#         if n == res_num:
#             return True
#         return False
    
#     return list_divisors, check_perfect(input_num)


# numbers_divisors, perfect_status = is_perfect(input_num, list_divisors = [])

# print(f"divisors number: {numbers_divisors}  perfect status: {perfect_status}")

#! روش کوتاه و راحت


def divisors(num):
    list_divisors = []
    
    for i in range(1, num+1):
        if num % i == 0:
          list_divisors.append(i)
    
    return list_divisors

def is_perfect(num):
    return num == sum(divisors(num)) - num

print(is_perfect(6))