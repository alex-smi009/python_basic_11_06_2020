# сумма чисел n+nn+nnn
# до разбора ДЗ
# var_n = input("Введите число цифрами\n")#значение будет строковое
# if var_n.isdigit():# проверяем что введено число цифрами
#     var_temp_1 = var_n + var_n# т.к. var_n изначально имеет строковое значение, то просто суммируем строки, чтобы иметь nn
#     var_temp_2= var_n + var_temp_1#т.к. var_n изначально имеет строковое значение, то просто суммируем строки, чтобы иметь nnn
#     var_sum = int(var_n) + int(var_temp_1) + int(var_temp_2)#меняем переменные с строк на целые числа и вычисляем сумму
#     print("Сумма чисел =", var_sum)
# else:
#     print("вы ввели не число")

#после разбора ДЗ
while True:
    var_n = input("Введите число цифрами\n")  # значение будет строковое
    if var_n.isdigit():  # проверяем что введено число цифрами
        break
    print("Вы ввели не число")
var_sum = int(var_n) + int(var_n * 2) + int(var_n * 3)
print("Сумма чисел =", var_sum)