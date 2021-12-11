
#? write a program : this is program get infinity input and find maximum string length

# def find_max_length(*args):
#     res_max = args[0]

#     for s in args:
#         if len(s) > len(res_max):
#             res_max = s

#     return res_max, len(res_max)

# max_word, length = find_max_length("Mahdi", "Mahdi_f__p", "hello world")

# print(f'maximum word : {max_word}  length : {length}')

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return "is not prime"

    return 'is prime'
    
print(prime_number(4))