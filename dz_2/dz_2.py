# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:09:50 2024

@author: Иван
"""


import pandas as pd

# Задание 1
# Напишите функцию, которая классифицирует фильмы из материалов занятия по правилам:

#     оценка 2 и ниже — низкий рейтинг;
#     оценка 4 и ниже — средний рейтинг;
#     оценка 4.5 и 5 — высокий рейтинг.

# Результат классификации запишите в столбец class.

rating_df = pd.read_csv('G:\sys_anal\python\my_python\ml-latest-small\\ratings.csv')


ad_campaigns = pd.read_excel('G:\sys_anal\python\my_python\ml-latest-small\\ad_campaigns.xlsx')





'''
Не подскажите, еслия я выполняю следующий код, то python возвращает ошибку: 
    
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().  
   
Я могу спользовать эту конструкция только когда присваиваю значение новому столбцу в DF? Работает только так, если убрать
операцию присваения, будет ошибка.   

if rating_df.rating <= 2:
    rating_df.classify = 'низкий рейтинг'
    
elif rating_df.rating > 2 and rating_df.rating <= 4:
    rating_df.classify = 'средний рейтинг'
    
elif  rating_df.rating == 4.5 or rating_df.rating == 5:
    rating_df.classify = 'высокий рейтинг'

'''



def classifator3000(row):
    if (row['rating'] <= 2):
        textRating = 'низкий рейтинг'
        return  textRating
        
    elif (row['rating'] > 2) and (row['rating'] <= 4):
        textRating = 'средний рейтинг'
        return  textRating
        
    elif  (row['rating'] == 4.5) or (row['rating']== 5):
        textRating = 'высокий рейтинг'
        return  textRating
    
    
    return  'рейтинг неопределен'
    
rating_df['new'] = rating_df.apply(classifator3000, axis = 1)    




 
'''
Задание 2
Используйте файл keywords.csv.

Нужно написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определённому региону. 
Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона. 
Если поисковый запрос не содержит названия города, то ставим ‘undefined’.

Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

geo_data = {

'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

}

Результат классификации запишите в отдельный столбец region.
'''
  
keywords_df = pd.read_csv('G:\sys_anal\python\my_python\ml-latest-small\\keywords.csv')

geo_data = {
        'Центр': ['москва', 'тула', 'ярославль'],
        'Северо-Запад': ['петербург', 'псков', 'мурманск'],
        'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
        }


keywords_df.columns
# Index(['keyword', 'shows'], dtype='object')

keywords_df['split'] = keywords_df['keyword'].apply(lambda x:  x.split(' '))


keywords_df['region'] 


def fund_rigion(element):  
    for x, y in geo_data.items():
        for i in range(len(y)):        
             if y[i] in element:
                 return x
    return None 
                           
                
                 
keywords_df['region'] = keywords_df['split'].apply(fund_rigion)
             












    
    