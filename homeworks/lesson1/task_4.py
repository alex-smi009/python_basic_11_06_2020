'''Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
print("Поиск самой большой цифры из числа")
while True:
    number = input("Введите целое положительное число\n")
    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    else:
        print("Вы ввели некорректные данные")
var_res = 0
while number and var_res != 9:
    temp = number % 10
    if temp > var_res:
        var_res = temp
    number //= 10
print("Наибольшая цифра в числе", var_res)
