#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time

# start_url = 'https://so.gushiwen.org/authors/default.aspx?'
# heads = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}

# param = []
# for i in range(1,2):
#     param.append('p={}&c='.format(i))
# #print(param)
# sum_urls = []
# for i in param:
#     a = start_url+i
#     sum_urls.append(a)
# #print(sum_urls)
# time.sleep(1)
# for i in sum_urls:
#     req = requests.get(i,headers = heads)
#     soup = BeautifulSoup(req.text,'lxml')
#     texts = soup.select('body > div.main3 > div.left > div > div.cont > p')
#     with open('/Users/leilianghuan/Desktop/code文件/练习pyth/诗词.txt','a+') as f:
#         b = re.findall('<p style=" margin:0px;">(.*?)<a href=',str(texts))
#         # for i in range(len(b)):
#         #     #print(b[i]+'\n')
#         #     f.write(str(b[i])+'\n')
with open ('/Users/leilianghuan/Desktop/code文件/练习pyth/诗词.txt','r') as f:
    b = f.readlines()
while 1:
    input_name = input('请输入诗人的名字：')
    for i in range(len(b)):
        e = re.search('{}(.*?)'.format(input_name),b[i])
        if e is not None:
            print(b[i])
