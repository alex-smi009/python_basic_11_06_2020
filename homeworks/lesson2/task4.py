'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове. '''

text = input('введите текст\n')

text_list = text.split(' ')
for num_str, word in enumerate(text_list):
    print (f'{num_str + 1} {word[:10]}')