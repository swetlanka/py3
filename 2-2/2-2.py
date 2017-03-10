#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3.5

import json
import datetime
from pprint import pprint
import chardet


def code_detecter(name):
    data = open(name, 'rb').read()
    result = chardet.detect(data)
    open(name).close()
    return result['encoding']

def open_file_json(name):
    code = code_detecter(name)
    print(code)
    with open(name) as _:
        return (json.load(open(name, encoding = code)))

def clean_str_from_extra_char(string):
    string = string.replace('<br>', ' ')
    string = string.replace('</a>', ' ')
    string = string.replace('«', '')
    string = string.replace('»', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('.', '')
    string = string.replace('?', '')
    string = string.replace('!', '')
    string = string.replace(',', '')
    string = string.replace('=', '')
    string = string.replace(':', '')
    string = string.replace('/', '')
    return string

def get_dict_word(data_basa_news, name):
    dict_news_item = data_basa_news['rss']['channel']['item']
    dict_word_from_description = {}
    for new in dict_news_item:
        if name == 'newsit.json':
            new['description'] = clean_str_from_extra_char(new['description'])
            description = str(new['description']).split()
        else:
            new['description']['__cdata'] = clean_str_from_extra_char(new['description']['__cdata'])
            description = str(new['description']['__cdata']).split()
        # print(description)
        for word in description:
            _, www_word, _ = word.partition('www')
            _, href_word, _ = word.partition('href')
            if href_word != '':
                _, _, word = word.partition('\">')
            if len(word) > 5 and www_word == '':
                if word not in dict_word_from_description:
                    dict_word_from_description[word] = 1
                else:
                    dict_word_from_description[word] += 1
    # pprint(dict_word_from_description)
    return dict_word_from_description

def print_10_word(word_tuples):
    now = datetime.datetime.now()
    file_name = 'word_list_from_' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.tsv'
    print()
    print('Список слов:')

    with (open(file_name, 'w', encoding='utf-8')) as file:
        rec = 'Слово\tСколько раз встречается\n'
        file.write(rec)
        for word, count in word_tuples[:10]:
            rec = '{}\t{}'.format(word, count)
            print(rec)
            file.write(rec + '\n')
    print()
    print('Сформирован файл {} со списком слов.'.format(file_name))


def main():
    while True:
        try:
            name_json = input('Введите имя json-файла: ')
            data_basa_news = open_file_json(name_json)
            #word_tuples = ()
            dict_word_from_description = get_dict_word(data_basa_news, name_json)
            word_tuples = dict_word_from_description.items()
            word_tuples = sorted(word_tuples, key = lambda word: word[1], reverse = True)
            #print(word_tuples)
            print_10_word(word_tuples)
            print()
        except FileNotFoundError:
            print('Файл {} не существует.'.format(name_json))
        except Exception as e:
            import logging
            logging.exception('asd')
            print('Что-то пошло не так: %s' % str(e))

if __name__ == '__main__':
    main()