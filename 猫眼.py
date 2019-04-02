#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


data  = pd.read_csv('/Users/leilianghuan/Desktop/code文件/数据处理/movie_maoyan.csv')
data_movie_box_office = data["movie_box_office(万元)"]

data1 = data[["director","screenwriter","movie_rating"]]
data1["movie_box_office"] = data_movie_box_office





def data_director(director,movie_rating,movie_box_office):
    list_derictor = []
    moive_type = {}  #每个演员擅长的电影类型
    list = []    #每个演员擅长的前几个电影类型
    mydata = pd.DataFrame()       #每个演员的电影类型及评分
    mydata["director"] = director
    mydata["movie_rating"] =movie_rating
    mydata["movie_box_office"] = movie_box_office

    #print(mydata)
    for type in director:
        for j in type.split(" / "):
            if j not in moive_type:
                moive_type.setdefault(j,1)
            else:
                   moive_type[j] += 1
        #对moive_type排序之后，moive_type变成列表了，而每次统计的过程是对字典操作，循环出错
        #moive_type = sorted(moive_type.items(),key=lambda e:e[1],reverse=True)
    #print("actor_name : " + name , "        moive_preferences : ",end = " ")
    for i in range(1,4):
        if not moive_type:
            break
        #print(max(moive_type,key=moive_type.get),end ="    ")
        list.append(max(moive_type,key=moive_type.get))
        moive_type.pop(max(moive_type,key=moive_type.get))
    #print()

    imdb_score_mean = 0
    gross_mean = 0
    count = 0
    #print("director_name: ", director.values[0])
    for type in list:
        for index,row in mydata.iterrows():
                if type in row['director']:
                    imdb_score_mean += row["movie_rating"]
                    gross_mean += row["movie_box_office"]
                    count += 1
        #print("导演: ",type,"平均评分: " , round(imdb_score_mean/count,2), "平均票房: ",round(gross_mean/count,2))
        
        list_derictor.append(type)
        list_derictor.append(round(imdb_score_mean/count,2))
        list_derictor.append(round(gross_mean/count,2))
        with open('/Users/leilianghuan/Desktop/code文件/数据处理/导演.docx','a+') as f:
            f.write(str(list_derictor)+'\n')
    #print()

director = data1['director'].value_counts()

#对actor_1擅长电影的统计分析
for name in director.index:
    director = data1[data1["director"] == name ]["director"]
    movie_rating = data1[data1["director"] == name ]["movie_rating"]
    movie_box_office = data1[data1["director"] == name]["movie_box_office"]
    data_director(director,movie_rating,movie_box_office)
