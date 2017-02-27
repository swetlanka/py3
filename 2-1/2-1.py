#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 3.5

import json
import datetime

def open_file_json(name):
    with (open(name, encoding='utf-8')) as _:
        return (json.load(open(name, encoding='utf-8')))

def open_file_format(name):
    data = {}
    ingridient = []
    with (open(name, encoding='utf-8')) as file:
        for name_dish in file:
            number_of_ingredients = int(file.readline())
            ingridient.clear()
            for _ in range(number_of_ingredients):
                str_ing = file.readline()
                ingridient_name = str_ing.split(' | ')[0]
                quantity = str_ing.split(' | ')[1]
                measure = str_ing.split(' | ')[2]
                ingridient.append({'ingridient_name': ingridient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})
            _ = file.readline()
            name_dish = name_dish.strip()
            data[name_dish] = ingridient[:]
        return data

def get_shop_list(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    now = datetime.datetime.now()
    file_name = 'shop_list_from_' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.csv'
    print()
    print('Список покупок:')

    with (open(file_name, 'w', encoding='utf-8')) as file:
        rec = 'Список продуктов' + '\n'
        file.write(rec)
        for shop_list_item in shop_list.values():
            rec = '{ingridient_name} {quantity} {measure}'.format(**shop_list_item)
            print(rec)
            file.write(rec + '\n')
    print()
    print('Сформирован файл {} со списком покупок.'.format(file_name))


def main():
    while True:
        try:
            # Вариант 1 c открытием файла формата json
            # data_basa_cook = open_file_json('cook_book_json')

            # Вариант 2 с открытием файла в формате из задания
            data_basa_cook = open_file_format('cook_book_format')

            person_count = int(input('Введите количество человек: '))
            dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
            shop_list = get_shop_list(data_basa_cook, dishes, person_count)
            print_shop_list(shop_list)
        except ValueError:
            print('Введено не число!')

        except Exception as e:
            print('Что-то пошло не так: %s' % str(e))

if __name__ == '__main__':
    main()