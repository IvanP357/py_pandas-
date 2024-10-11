# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:33:09 2024

@author: iparkhomenko
"""

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd



''''
Задание 1
Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

    если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
    для источников paid и email из России ставим ad;
    для источников paid и email не из России ставим other;
    все остальные варианты берём из traffic_source без изменений.
'''

log = pd.read_csv('C:\my\py\\netology\pandas\\visit_log.csv', sep = ';')

log.loc[(log['traffic_source'] == 'google') | (log['traffic_source'] == 'yandex'), ['source_type']] = 'organic'        
log.loc[(log['traffic_source'] == 'paid') & (log['region'] == 'Russia'), ['source_type']] = 'ad'
log.loc[~((log['traffic_source'] == 'paid') & (log['region'] == 'Russia')), ['source_type']] = 'other'

log.loc[log['traffic_source'].isna() , ['source_type']] = log['source_type']


'''
Задание 2
В файле URLs.txt содержатся URL страниц новостного сайта. Вам нужно отфильтровать его по адресам страниц с текстами новостей. Известно,
 что шаблон страницы новостей имеет внутри URL конструкцию: /, затем 8 цифр, затем дефис. Выполните действия:

    Прочитайте содержимое файла с датафрейм.
    Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствие с заданным шаблоном.
'''


with open('C:\my\py\\netology\pandas\\URLs.txt','r') as f:
    next(f)
    table = [x.strip().split('\n') for x in f.readlines()]

file.close()

URLs = pd.DataFrame(table, columns = ['URL'])

filtered = URLs[URLs['URL'].str.contains('/\d{8}', regex=True)]

'''
Задание 3
Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок.
Под временем жизни понимается разница между максимальным и минимальным значениями столбца timestamp для данного значения userId.

'''

ratings = pd.read_csv('C:\my\py\\netology\pandas\\ml-latest-small\\ratings.csv')

diff = ratings.groupby('userId').agg({'timestamp': ['min', 'max']}).reset_index()['timestamp']['max'] - ratings.groupby('userId').agg({'timestamp': ['min', 'max']}).reset_index()['timestamp']['min']
diff.mean()


'''
Задание 4
Дана статистика услуг перевозок клиентов компании по типам
(см. файл “Python_13_join.ipynb” в разделе «Материалы для лекции “Продвинутый pandas”» ---- Ноутбуки к лекции «Продвинутый pandas»).

Нужно сформировать две таблицы:

    таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
    аналогичную таблицу по типам выручки с указанием адреса клиента.
    
К домашнему заданию №4
Дана статистика услуг перевозок клиентов компании по типам:

rzd - железнодорожные перевозки
auto - автомобильные перевозки
air - воздушные перевозки
client_base - адреса клиентов
    
'''

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)    

# Нужно сформировать две таблицы:

#     таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
#     аналогичную таблицу по типам выручки с указанием адреса клиента

df = pd.DataFrame()

rzd.merge(auto, how='outer', on='client_id').merge(air, how='outer', on='client_id')
rzd.merge(auto, how='outer', on='client_id').merge(air, how='outer', on='client_id').merge(client_base, how='outer', on='client_id')

























