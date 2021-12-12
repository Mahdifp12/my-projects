def find_max_length(*args):
    res_max = args[0]

    for s in args:
        if len(s) > len(res_max):
            res_max = s

    return res_max, len(res_max)

max_word, length = find_max_length("Mahdi", "Mahdi_f__p", "hello world")

print(f'maximum word : {max_word}  length : {length}')