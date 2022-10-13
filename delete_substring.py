"""
 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""


def create_file(text):
    """Принимает текст и создаёт файл с этим текстом.
    """
    name = input('Задайте путь к файлу: ')
    with open(name, 'a') as my_fl:
        my_fl.writelines(text)


def read_file(name):
    """Принимает путь к файлу и
    читает его содержимое
    """
    with open(name, 'r') as my_f:
        f_string = my_f.read()
    return f_string


def delete_substr(user_str, sub_str):
    """Принимает исходную строку и подстроку удаления.
    Возвращает строку без подстроки.
    """
    user_str_list = user_str.split()
    edit_str_list = filter(lambda el: sub_str not in el, user_str_list)
    edit_str = ' '.join(edit_str_list)
    return edit_str


user_string = input('Введите текст: \n')
create_file(user_string)

input_string = read_file('qwerty.txt')
print('Входная строка: ', input_string)

sub_string = input('Введите подстоку для удаления: ')

if sub_string not in input_string:
    print('Нет такой подстроки')
else:
    edit_string = delete_substr(input_string, sub_string)
    print('Обработанная строка: ', edit_string)
    create_file(edit_string)
    