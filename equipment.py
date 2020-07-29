from pyecharts.charts import Page, Radar

import csv
from pyecharts import options as opts
from pyecharts.charts import Pie
page=Page()

#-----------------------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/jidui.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------

zidian2={}
with open('../../data/data/equipment/jiandui.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            zidian2[jianxie]=zhi
# zidian已完成字典
#-------------------------------------------------------
zidian3={}
with open('../../data/data/equipment/tanke.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            zidian3[jianxie]=zhi
#zidian已完成字典
#-------------------------------------------------------
zidian4={}
with open('../../data/data/equipment/qiantin.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            zidian4[jianxie]=zhi
#zidian已完成字典
#-------------------------------------------------------
zidian5={}
with open('../../data/data/equipment/zhishengji.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            zidian5[jianxie]=zhi
#zidian已完成字典
#-------------------------------------------------------
zidian6={}
with open('../../data/data/equipment/zhuangjiace.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            zidian6[jianxie]=zhi
#zidian已完成字典
#print(zidian1)
vn=[]
for i in range(len(zidian1)):
    vn.append([[eval(zidian1[list1[i]]),eval(zidian2[list1[i]]),eval(zidian3[list1[i]]),eval(zidian4[list1[i]]),eval(zidian5[list1[i]]),eval(zidian6[list1[i]])]])
def radar_base() ->Radar:
    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name='飞机机队',max_=13500),
                opts.RadarIndicatorItem(name='海军舰队', max_=1000),
                opts.RadarIndicatorItem(name='坦克', max_=13000),
                opts.RadarIndicatorItem(name='潜艇', max_=100),
                opts.RadarIndicatorItem(name='直升机', max_=6000),
                opts.RadarIndicatorItem(name='装甲车', max_=40000),

            ]
        )
        .add(list1[0],vn[0],color='blue',
                areastyle_opts=opts.AreaStyleOpts(
                    opacity=0.5,
                    color='blue'
                ),)
        .add(list1[1], vn[1], color='red',
             areastyle_opts=opts.AreaStyleOpts(
                 opacity=0.5,
                 color='red'
             ),)
        .add(list1[2], vn[2], color='yellow',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='yellow'
            ), )
        .add(list1[3], vn[3], color='purple',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='purple'
            ), )
        .add(list1[4], vn[4], color='green',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='green'
            ), )
        .add(list1[5], vn[5], color='pink',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='pink'
            ), )
        .add(list1[6], vn[6], color='#00ae9d',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='#00ae9d'
            ), )
        .add(list1[7], vn[7], color='#90d7ec',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='#90d7ec'
            ), )
        .add(list1[8], vn[8], color='#6e6b41',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='#6e6b41'
            ), )
        .add(list1[9], vn[9], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     color='#293047'
            ),
             )
        .add(list1[10], vn[10], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     # color='#293047'
            ),
            )
        .add(list1[11], vn[11], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     # color='#293047'
            ),
            )
        .add(list1[12], vn[12], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     # color='#293047'
            ),
            )
        .add(list1[13], vn[13], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     # color='#293047'
            ),
            )
        .add(list1[14], vn[14], color='#293047',
                 areastyle_opts=opts.AreaStyleOpts(
                     opacity=0.5,
                     # color='#293047'
            ),
            )

        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='装备雷达图',pos_top='20'))
    )
    return c
page.add(radar_base())

zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/jiandui.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='海军舰队饼状图',pos_top='100'),)
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出

    )

    return c

page.add(pie_base())
#--------------------------------------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/jidui.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
#     分类  数据量   火车经济
# 假数据
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='飞机机队饼状图',pos_top='100'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出
    )

    return c
page.add(pie_base())
#-------------------------------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/qiantin.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
#     分类  数据量   火车经济
# 假数据
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='潜艇饼状图',pos_top='100'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出
    )

    return c
page.add(pie_base())
#-----------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/tanke.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
#     分类  数据量   火车经济
# 假数据
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='坦克饼状图',pos_top='100'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出
    )

    return c
page.add(pie_base())
#----------------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/zhishengji.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
#     分类  数据量   火车经济
# 假数据
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='直升机饼状图',pos_top='100'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出
    )

    return c
page.add(pie_base())
#---------------------------------
zidian1={}
list1=[]#存放jidui所有名字
with open('../../data/data/equipment/zhuangjiace.csv','r') as f:
    reader1 = csv.reader(f)
    print(reader1)
    temp=0
    for row in reader1:#第0行不用
        jianxie=row[0]
        zhi=row[2]
        #print(row) row为列表，有三个成员缩写；国名；数量
        if temp==0:
            temp+=1
            continue
        else:
            list1.append(row[0])
            zidian1[jianxie]=zhi
#zidian已完成字典
#-----------------------------------------------------------------------------
v2=[]
for i in range(15):
    v2.append(zidian1[list1[i]])
def pie_base():
#     分类  数据量   火车经济
# 假数据
    v1 = list1[:15]

    c = (
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],radius=[50,100])
        .set_global_opts(title_opts=opts.TitleOpts(title='装甲车饼状图',pos_top='100'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))   #格式化标签输出
    )

    return c
page.add(pie_base())



page.render('装备.html')
