#！/usr/bin/env python3
#coding = utf-8
import math
import requests
from bs4 import BeautifulSoup
import re
import random


#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt 


url1 = "https://www.douban.com/doulist/46410115/?start="
url2 = "&sort=time&playable=0&sub_type="
urls = []
for i in range(0,300,25):
    urls.append(url1 + str(i) +url2)

# print(a[1])
# from selenium import webdriver
import time
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(3)
# pageSource = browser.page_source

# browser.close()

# for i in range(0,13):
#     req = requests.get(a[i])
#     soup = BeautifulSoup(req.content,"lxml")
#     items_lists = soup.select('.doulist-item')
#     print(items_lists)
#     with open('/Users/leilianghuan/Desktop/python_practise/a.txt','a+') as f:
#         f.write(str(items_lists))
#     time.sleep(5)
head = {}
for i in range(0,13):
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = requests.get(urls[i],headers = head)
    soup = BeautifulSoup(req.content,"lxml")
    name = soup.select('.doulist-item > div > div.bd.doulist-subject > div.title > a')
    abstract = soup.select('.doulist-item > div > div.bd.doulist-subject > div.abstract')
    comment = soup.select('.doulist-item > div > div.ft > div.comment-item.content > blockquote')
    a = {}
    for names,abs,coms in zip(name,abstract,comment):
        names = names.get_text().replace('\n        ','').replace('\n      ','') 
        abs = abs.get_text().replace('\n      \n          ','').replace('\n            \n          ','').replace('\n            \n          ','').replace('\n    ','')
        coms = coms.get_text().replace('\n','')
        a ={
            '名字':names,
            '作者':abs,
            '评语':coms
        }
        with open('/Users/leilianghuan/Desktop/python_practise/b.txt','a+') as f:
            f.write(str(a))
    randint_1 = random.randint(3, 10)
    time.sleep(randint_1)
# print(str(name),str(abstract),str(comment))
# for ele in soup.find_all("blockquote"):
#     name = ele.text
#     print(name)
# a = {}
# for names,abs,coms in zip(name,abstract,comment):
#     names = names.get_text().replace('\n        ','').replace('\n      ','') 
#     abs = abs.get_text().replace('\n      \n          ','').replace('\n            \n          ','').replace('\n            \n          ','').replace('\n    ','')
#     coms = coms.get_text().replace('\n','')
#     a ={
#         '名字':names,
#         '作者':abs,
#         '评语':coms
#     }
#     print(a)




# for href,image in zip(hrefs,images):
#     data={
#         'href':href.get('href'),#注意，是title，没有s，是列表中的被遍历的对象：对象对应的值
#         'image':image.get('data-src')#注意，当一个标签有多个属性时，需要通过该标签对象调用get()进行获取属性的内容，img标签的获取是通过“data-src”或“src”，a标签是href属性等。
#     }