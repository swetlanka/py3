#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3.5

import osa
import math


def client_soap(url, function, param):
    client = osa.client.Client(url)
    if function == 't':
        print('Средняя температура: {} по Цельсию.'.format(client.service.ConvertTemp(Temperature = param, FromUnit = 'degreeFahrenheit', ToUnit = 'degreeCelsius')))
    elif function == 'c':
        print('Общая сумма: {} рублей.'.format(math.ceil(client.service.ConvertToNum(fromCurrency = 'EUR', toCurrency = 'RUB', amount = param, rounding = False))))

def temperatura(file_name):
    temp_list = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            temp_list.append(float(line.split()[0]))
    print(temp_list)

    avg_temp = sum(temp_list) / len(temp_list)
    client_soap('http://www.webservicex.net/ConvertTemperature.asmx?WSDL', 't', avg_temp)


def currencies(file_name):
    curr_list = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            curr_list.append(float(line.split()[1]))
    print(curr_list)

    sum_curr = sum(curr_list)
    client_soap('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL', 'c', sum_curr)

def main():
    temperatura('temps.txt')
    currencies('currencies.txt')

if __name__ == '__main__':
    main()