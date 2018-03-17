# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import chardet

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)


def get_sql_list():
    migrations_dir = os.path.join(current_dir, migrations)
    file_list = os.listdir(path=migrations_dir)
    sql_list = [i for i in file_list if i.endswith('.sql')]
    return sql_list


def decode_files(file_name):
    with open(os.path.join(current_dir, migrations, file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data.lower()
    return data


def search_in_files(sql_list):
    while True:
        search_string = input('Введите строку: ').lower()
        containing_files = [file_name for file_name in sql_list if search_string in decode_files(file_name)]
        print('\n'.join(containing_files))
        print('Всего: {}'.format(len(containing_files)))
        sql_list = containing_files


if __name__ == '__main__':
    search_in_files(get_sql_list())

    pass
