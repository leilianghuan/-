#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/leilianghuan/Desktop/code文件/练习pyth/data_analysis.csv')


#处理 num_critic_for_reviews 列中的空值o
#print(data[data["num_critic_for_reviews"].isnull()].shape[0])
#num_critic_for_reviews列 有50个空值，占总数据0.99%
#删除空值
data = data[data["num_critic_for_reviews"].notnull()]


#处理 actor_1_facebook_likes 列中的空值
#print(data[data["actor_1_facebook_likes"].isnull()].shape[0])
#actor_1_facebook_likes列  有6个空值，占总数据0.12%
#删除空值
data = data[data["actor_1_facebook_likes"].notnull()]


#处理 actor_2_facebook_likes 列中的空值
#print(data[data["actor_2_facebook_likes"].isnull()].shape[0])
#actor_2_facebook_likes列  有5个空值，占总数据0.10%
#删除空值
data = data[data["actor_2_facebook_likes"].notnull()]


#处理 actor_3_facebook_likes 列中的空值
#print(data[data["actor_3_facebook_likes"].isnull()].shape[0])
#actor_3_facebook_likes列  有8个空值，占总数据0.16%
#删除空值
data = data[data["actor_3_facebook_likes"].notnull()]


#处理 facenumber_in_poster 列中的空值
#print(data[data["facenumber_in_poster"].isnull()].shape[0])
#facenumber_in_poster列  有12个空值，占总数据0.24%
data = data[data["facenumber_in_poster"].notnull()]


#处理 budget 列中的空值
#print(data[data["budget"].isnull()].shape[0])
#budget列  466个空值，占总数据9.39%
data = data[data["budget"].notnull()]

#处理 director_name 列的空值
data = data[data["director_name"].notnull()]

#处理 imdb_score  列的空值
data = data[data['imdb_score'].notnull()]

#处理 title_year 列中的空值
#print(data[data["title_year"].isnull()].shape[0])
#title_year列,6个空值，占总数据0.13%
data = data[data["title_year"].notnull()]
#print(data)





#二维数组显示赋值
director_likes = data.sort_values(by ='director_facebook_likes',ascending= False)[['director_name','director_facebook_likes','gross']]
#对导演点赞数重新列索引值
director_likes.set_index(np.arange(len(data)),inplace=True)
#print(director_likes)



#删除重复的导演
director_likes1 = director_likes.groupby(by = 'director_name',sort = False,as_index=False)['director_facebook_likes','gross'].mean()
#print(director_likes1)
#导出导演和facebook的数值.csv文件
#director_likes1.to_csv("test1.csv",index=True,sep=',')


#建立一个画框
plt.figure(figsize=(16,9))
x = director_likes1['director_name']
y = director_likes1['director_facebook_likes']
area = data['gross']
plt.scatter(range(500),y.head(500),s =area/1000000,c = 'r')
plt.ylabel("director_facebook_likes")
plt.xlabel('director_num')
plt.title("director_likes")
plt.xlim([-0.5,500])
plt.ylim([0,25000.0])
#plt.xticks(range(50),x.head(500))
plt.show()

#plt.scatter(x, y, s=area, c=colors, alpha=0.5)



#二维数组显示赋值
actor1 = data.sort_values(by ='actor_1_facebook_likes',ascending= False)[['actor_1_name','actor_1_facebook_likes']]
#对演员1号点赞数重新列索引值
actor1.set_index(np.arange(len(data)),inplace=True)
#print(director_likes)

#删除重复的演员1号
actor_num1 = actor1.groupby(by = 'actor_1_name',sort = False,as_index=False)['actor_1_facebook_likes'].mean()
#print(actor_num1)

#导出演员与点赞数.csv文件
actor_num1.to_csv("actor.csv",index=True,sep=',')


#建立一个画框
plt.figure(figsize=(16,9))
x = actor_num1['actor_1_name']
y = actor_num1['actor_1_facebook_likes']
plt.plot(range(500),y.head(500),"r-")
plt.ylabel("actor_1_facebook_likes")
plt.xlabel('actor_1_name')
plt.title("actor_number_1")
plt.xlim([-0.5,500])
plt.ylim([0,270000.0])
#plt.xticks(range(50),x.head(500))
plt.show()



#二维数组显示赋值
actor2 = data.sort_values(by ='actor_2_facebook_likes',ascending= False)[['actor_2_name','actor_2_facebook_likes']]
#对演员2号点赞数重新列索引值
actor2.set_index(np.arange(len(data)),inplace=True)
#print(director_likes)

#删除重复的演员1号
actor_num2 = actor2.groupby(by = 'actor_2_name',sort = False,as_index=False)['actor_2_facebook_likes'].mean()
#print(actor_num2)

#导出演员与点赞数.csv文件
#actor_num2.to_csv("actor.csv",index=True,sep=',')


#建立一个画框
plt.figure(figsize=(16,9))
x = actor_num2['actor_2_name']
y = actor_num2['actor_2_facebook_likes']
plt.plot(range(500),y.head(500),"r-")
plt.ylabel("actor_2_facebook_likes")
plt.xlabel('actor_2_name')
plt.title("actor_number_2")
plt.xlim([-0.5,500])
plt.ylim([0,30000.0])
#plt.xticks(range(50),x.head(500))
plt.show()


#二维数组显示赋值
actor3 = data.sort_values(by ='actor_3_facebook_likes',ascending= False)[['actor_3_name','actor_3_facebook_likes']]
#对演员2号点赞数重新列索引值
actor3.set_index(np.arange(len(data)),inplace=True)
#print(director_likes)

#删除重复的演员1号
actor_num3 = actor3.groupby(by = 'actor_3_name',sort = False,as_index=False)['actor_3_facebook_likes'].mean()
#print(actor_num2)

#导出演员与点赞数.csv文件
#actor_num2.to_csv("actor.csv",index=True,sep=',')


#建立一个画框
plt.figure(figsize=(16,9))
x = actor_num3['actor_3_name']
y = actor_num3['actor_3_facebook_likes']
plt.plot(range(500),y.head(500),"r-")
plt.ylabel("actor_3_facebook_likes")
plt.xlabel('actor_3_name')
plt.title("actor_number_3")
plt.xlim([-0.5,500])
plt.ylim([0,30000.0])
#plt.xticks(range(50),x.head(500))
plt.show()

