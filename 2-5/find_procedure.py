
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

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
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path

def filter_files(list_files, substr):
    result = []
    for file_name in list_files:
        #print(file_name)
        with open(file_name) as f:
            for line in f:
                if substr in line.lower():
                    result.append(file_name)
                    print(file_name)
                    break

    return result

def main():
    migrations = 'Migrations'

    files = glob.glob(os.path.join(migrations, "*.sql"))

    #for file in files:
        #print(file)

    while True:
        substr = input('Введите строку:') .lower()
            #.encode('utf-8')
        #print(substr)
        files = filter_files(files, substr)
        print('Всего {} файлов'.format(len(files)))

if __name__ == '__main__':
    main()