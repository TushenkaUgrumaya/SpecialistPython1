# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.


import random

def gen_list(size, of, to):
    pass
    result_list = []
    for _ in range(size):
        result_list.append(random.randrange(of, to))
    return result_list


# gen_list(5, 1, 100)
gen_list(5, - 10, 20)

test = gen_list(5, - 10, 20)
print(test)
