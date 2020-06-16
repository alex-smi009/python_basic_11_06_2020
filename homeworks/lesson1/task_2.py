# Вариант до разбора ДЗ
# print("Конвертор времени: секунды в кол-во часов,минут, секунд")
# sec = input('Введите кол-во секунд\n')
# if sec.isdigit():
#     sec = int(sec)
#     hours = sec // 3600
#     minutes = (sec // 60) % 60
#     seconds = sec % 60
# else:
#     print('Введенно не число или число не цифрами')
# print( "%02d:%02d:%02d" % (hours,minutes,seconds)) #используется оператор % для форматирования вывода
# #or
# print(f"{hours:>02}:{minutes:>02}:{seconds:>02}") #используется f-строка

# Вариант после разбора ДЗ
print("Конвертор времени: секунды в кол-во часов,минут, секунд")
while True:
    sec = input('Введите кол-во секунд\n')
    if sec.isdigit():
        sec = int(sec)
        break
    print("введено не число, необходимо ввести число цифрами")
hours = sec // 3600
minutes = (sec // 60) % 60
seconds = sec % 60

print( "%02d:%02d:%02d" % (hours,minutes,seconds)) #используется оператор % для форматирования вывода
#or
print(f"{hours:>02}:{minutes:>02}:{seconds:>02}") #используется f-строка
