#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd

def HTMLtext(url):
    r = requests.get(url)
    r.encoding = 'utf-8'#r.apparent_encoding
    return r.text
url = "http://www.zuihaodaxue.cn/shehuishengyupaiming2018.html"
html = HTMLtext(url)
soup = BeautifulSoup(html,'lxml')
#print(soup.text[:100])
list1 = []

#print("{:^10}\t{:^6}\t{:^10}".format('排名','学校','综合排名'))

#遍历树
for i in soup.find_all('tr',attrs={'class':'alt'}):
    td = i('td')
    list1.append([td[0].string,td[1].string,td[4].string])

#将综合排名为空值的用*代替
'''
for i in range(100):
    u = list1[i]
    if u[2] == None:
        u[2] = "*"
    print("{0:^10s}{1:<6s}{2:>10s}".format(u[0],u[1],u[2]))
'''


data = pd.DataFrame(list1,columns=["排名",'学校','综合'])
#把综合排名的空值删去
#data = data[data['综合'].notnull()]
#将文件写入csv文件
data.to_csv(path_or_buf='/Users/leilianghuan/Desktop/不能点开的秘密/code文件/University.csv', sep=",",index=False)
