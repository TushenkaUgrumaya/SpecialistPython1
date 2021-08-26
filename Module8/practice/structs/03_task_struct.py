# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов


import random

n = 10
lst = []
while n != 0:
    lst.append(random.randint(-10, 20))
    n -= 1
print(lst)

count_numbers = len(list(filter(lambda el: el <= 10, lst)))
print(count_numbers)
summa_positive = sum(filter(lambda el: el > 0, lst))
print(summa_positive)
average = list(filter(lambda el: el % 2 == 0 and el > 0, lst))
average = sum(average) / len(average)
print(average)
