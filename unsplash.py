#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re

def getlist(keyword,pages):
    params = []
    for i in range(2,pages):
        params.append({
            'query': keyword,
            'xp':'' ,
            'per_page': 20,
            'page': i
        })
    urls = []
    url = 'https://unsplash.com/search/photos?'
    heads = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    for i in params:
        urls.append(requests.get(url,params=i,headers = heads).json().get('results'))
    return urls

lists = getlist('beauty',2)
print(lists)
# def saveimg(lists,path):
#     #lists = getlist('animal',3)
#     #path = '/Users/leilianghuan/Desktop/实训照片'
#     a = json.dumps(lists,ensure_ascii=False)
#     #b = json.loads(a,encoding='utf-8')
#     c = re.findall(r'\"thumb\"\: \"(.*?)\"',a)
#     for i in c:
#         img = requests.get(i)
#         with open(path +'/' +i[-5:]+ '.jpg','wb') as f:
#             f.write(img.content)
            
# saveimg(lists,'/Users/leilianghuan/Desktop')

# https://images.unsplash.com/photo-1440589473619-3cde28941638?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60