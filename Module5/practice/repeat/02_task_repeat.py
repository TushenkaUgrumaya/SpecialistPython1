# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    pass
    temp_number = number
    list_number = []
    while temp_number != 0:
        list_number.append(temp_number % 10)
        temp_number //= 10
    if list_number[::-1] == list_number:
        return True
    return False

print(palindrome(234532))
print(palindrome(764467))
print(palindrome(56765))
# print(palindrome(0023443200))
print(palindrome(9999999999))
