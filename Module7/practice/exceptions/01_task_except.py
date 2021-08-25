# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

import math

while True:
    try:
        size = input('Size =: ')
        numbers = size.split('x')
        try:
            total = math.floor(int(numbers[0])/int(numbers[1]))
            print(total)
        except IndexError:
            print("Еще одно число через х")
        # print(total)
    except ValueError:
        print("Неккоректно ввел")
