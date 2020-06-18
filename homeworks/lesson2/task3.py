'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. '''

while True:
    months = input("Введите месяц года числом от 1 до 12\n")
    if months.isdigit():
        months = int(months)
        if months > 12:
            print("Неверно, в году только 12 месяцев")
            continue
        break

#  решение с помощью list
list_season = ['зима', 'весна', 'лето', 'осень', 'зима']
print ('сейчас', list_season [months // 3])


# решение с помощью dict
my_season_dic = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето',
    7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
print ('сейчас', my_season_dic[months])