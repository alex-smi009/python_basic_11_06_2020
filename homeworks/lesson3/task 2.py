'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def data_user(**kwargs):
    return list(kwargs.values())

def data():
    print(data_user(name = input('Enter name: '),
                s_name = input('Enter second name: '),
                b_date = input('Enter birth day: '),
                l_town = input('Enter live town: '),
                email = input('Enter email: '),
                tel = input('Enter tel number: ')))
