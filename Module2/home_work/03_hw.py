# Задача 3. Таблица стоимости
# Одна единица некоторого товара стоит x рублей. Напечатайте таблицу стоимости 2, 3, ..., 20 единиц этого товара.
# Формат входных данных
# Вводится одно положительное вещественное число x, которое не превосходит 105 и задано с двумя знаками после запятой.

x = float(input("Введите цену товара в формате хх.хх: "))
n = 1
while n != 21:
    # print(n, int(x * n * 100) / 100)
    print(n, round(x * n, 2)) # сдаюсь! этот вариант уже нагуглил в интернете, но кроме как str я незнаю сделать! а str плохо!
    n += 1
