# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:10:50 2024

@author: Иван
"""

import requests
from bs4 import BeautifulSoup


res = requests.get('https://habr.com/ru/feed/')




soup  = BeautifulSoup(res.text)


res.text
 