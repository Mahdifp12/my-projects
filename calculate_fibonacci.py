def calc_fibonacci(num):
    if num in [0, 1]:
        return num
    return calc_fibonacci(num - 1) + calc_fibonacci(num - 2)

print([calc_fibonacci(n) for n in range(6)])