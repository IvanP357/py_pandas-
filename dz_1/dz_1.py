# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:59:51 2024

@author: iparkhomenko
"""

import os
import pandas as pd

path = 'C:\\my\\py\\netology\\pandas\\10._Основы_pandas\\Файлы к заданию №1\\'
data = ['movies.csv', 'ratings.csv']

pathN = path + name
dataF = pd.read_csv(path + data[0])
dataR = pd.read_csv(path + data[1])

mdata = dataF.merge(dataR, how = 'left', on = 'movieId')
mdata = mdata[(mdata.rating == 0.5)]


test = mdata.groupby(by='movieId').count().sort_values(by = 'rating', ascending = False)
test.head  # movieId = 26683


mdata[(mdata.movieId == 2683)].title
# Austin Powers: The Spy Who Shagged Me (1999)






"""
Задание 1
Датасет для домашнего задания вы найдете:

    в материалах к лекции «Библиотека Pandas», файл “Дополнительные файлы для домашнего задания” (актуально для групп до PYDA-59)
    файлы для домашнего задания «Библиотека Pandas» ( актуально с группы PYDA-59 и далее).

Определите, какому фильму было выставлено больше всего оценок 5.0.
"""


import os
import pandas as pd

path = 'C:\\my\\py\\netology\\pandas\\10._Основы_pandas\\Файлы к заданию №1\\'
data = ['movies.csv', 'ratings.csv']

pathN = path + name
dataF = pd.read_csv(path + data[0])
dataR = pd.read_csv(path + data[1])

mdata = dataF.merge(dataR, how = 'left', on = 'movieId')
mdata = mdata[(mdata.rating == 0.5)]


test = mdata.groupby(by='movieId').count().sort_values(by = 'rating', ascending = False)
test.head  # movieId = 26683


mdata[(mdata.movieId == 2683)].title
# Austin Powers: The Spy Who Shagged Me (1999)




"""
Задание 2
По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония)
 категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.

"""

path = 'C:\\my\\py\\netology\\pandas\\10._Основы_pandas\\Файлы к заданию №2\\'
data = ['power.csv', 'transactions.csv']

dataP = pd.read_csv(path + data[0])
dataT = pd.read_csv(path + data[1])


def baltic(country, category):
    
    if country in ['Lithuania', 'Latvia', 'Estonia']:
        return 'Прибалтика'
    
    return 'Other'


dataP['baltic'] = dataP.country.apply(baltic)
test = dataP[(dataP.baltic == 'Прибалтика') & (dataP.category.isin([4,12,24])) & (dataP.year > 2005) & (dataP.year < 2010)]  

test.quantity.sum()
# 35096.0



"""
Задание 3
Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas DataFrame. Вы можете взять любые страницы.
Примеры страниц:

"""

test = pd.read_html('https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html')

