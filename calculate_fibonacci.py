def calc_fibonacci(n):
    if n in [0, 1]:
        return n
    return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)

print([calc_fibonacci(n) for n in range(6)])