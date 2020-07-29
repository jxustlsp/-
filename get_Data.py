# -*- coding: utf-8 -*-
from lxml import etree
import re
import pandas as pd
import numpy as np


def getFirePowers():
    htmlfile = open(r'C:\Users\26578\Desktop\keshe\html\globalfirepower.html')
    htmlhandle = htmlfile.read()
    res = etree.HTML(htmlhandle)
    short_name = res.xpath('//div[@class="shortFormName"]/span/text()')
    long_name = res.xpath('//div[@class="longFormName"]/span/text()')
    powers_tmp = res.xpath('//div[@class="pwrIndexContainer"]/span/span/text()')
    powers = []
    for power in powers_tmp:
        tmp = re.findall(r'\d.\d+', str(power))
        f = float(tmp[0])
        powers.append(int(100.0 / f))
    dataframe = pd.DataFrame({'short_name': short_name,'long_name': long_name, 'power': powers})
    dataframe.to_csv("C:\\Users\\26578\\Desktop\\keshe\\data\\power_Data.csv", index=False, sep=',')

def getPowers(s):
    path = "C:\\Users\\26578\\Desktop\\keshe\\html\\" + s + ".html"
    htmlfile = open(path)
    htmlhandle = htmlfile.read()
    res = etree.HTML(htmlhandle)
    short_name = res.xpath('//div[@class="shortFormName"]/span/text()')
    long_name = res.xpath('//div[@class="longFormName"]/span/text()')
    powers = res.xpath('//div[@class="valueContainer"]/span/span/text()')
    for i in range(len(powers)):
        if(len(powers[i]) == 6):
            powers[i] = (int(powers[i][0]) * 10 + int(powers[i][1])) * 1000 + int(powers[i][3:6])
        elif(len(powers[i]) == 5):
            powers[i] = int(powers[i][0]) * 1000 + int(powers[i][2:5])
        else:
            powers[i] = int(powers[i])
    file_name = "C:\\Users\\26578\\Desktop\\keshe\\data\\" + s + ".csv"
    dataframe = pd.DataFrame({'short_name': short_name, 'long_name':long_name, 'power': powers})
    dataframe.to_csv(file_name, index=False, sep=',')

def proc():
    data1 = pd.read_csv('./data/power_Data.csv', encoding='utf-8')
    data2 = pd.read_csv('./data/Land_Force.csv', encoding='utf-8')
    data3 = pd.read_csv('./data/Naval_Force.csv', encoding='utf-8')
    data4 = pd.read_csv('./data/Airpower.csv', encoding='utf-8')
    data1 = np.array(data1)
    data2 = np.array(data2)
    data3 = np.array(data3)
    data4 = np.array(data4)
    l_name = []
    s_name = []
    all_data = []
    tank = []
    nava = []
    air = []
    for i in range(100):
        l_name.append(data1[i][1])
        s_name.append(data1[i][0])
        all_data.append(data1[i][2])
        for j in range(len(data2)):
            if data1[i][1] == data2[j][1]:
                tank.append(data2[j][2])
                break
    for i in range(100):
        j = 0
        for j in range(len(data3)):
            if data1[i][1] == data3[j][1]:
                nava.append(data3[j][2])
                break
        if j == len(data3)-1:
            nava.append(0)
    for i in range(100):
        for j in range(len(data4)):
            if data1[i][1] == data4[j][1]:
                air.append(data4[j][2])
                break
    dataframe = pd.DataFrame({'short_name': s_name, 'long_name': l_name, 'power': all_data, 'tank':tank, 'naval':nava, 'air':air})
    dataframe.to_csv('./data/All_Data.csv', index=False, sep=',')

def proc_path(s, s2):
    path = "C:\\Users\\26578\\Desktop\\keshe\\html\\" + s2 + "\\" + s + ".html"
    htmlfile = open(path)
    htmlhandle = htmlfile.read()
    res = etree.HTML(htmlhandle)
    short_name = res.xpath('//div[@class="shortFormName"]/span/text()')
    long_name = res.xpath('//div[@class="longFormName"]/span/text()')
    powers = res.xpath('//div[@class="valueContainer"]/span/span/text()')
    str = ['0','1','2','3','4','5','6','7','8','9']
    values = []
    for power in powers:
        sum = 0
        for num in power:
            if num in str:
                sum = sum * 10 + int(num)
        values.append(sum)
    file_name = "C:\\Users\\26578\\Desktop\\keshe\\data\\" + s2 + "\\" + s + ".csv"
    dataframe = pd.DataFrame({'short_name': short_name, 'long_name':long_name, 'power': values})
    dataframe.to_csv(file_name, index=False, sep=',')

def zhenli():
    data1 = pd.read_csv('./data/people/active service.csv', encoding='utf-8')
    data2 = pd.read_csv('./data/people/Available population.csv', encoding='utf-8')
    data3 = pd.read_csv('./data/people/reach age.csv', encoding='utf-8')
    data4 = pd.read_csv('./data/people/Suitable for service.csv', encoding='utf-8')
    data1 = np.array(data1)
    data2 = np.array(data2)
    data3 = np.array(data3)
    data4 = np.array(data4)
    l_name = []
    s_name = []
    huangjin_chubei = []
    purchase = []
    yusuan = []
    peo = []
    for i in range(100):
        l_name.append(data1[i][1])
        s_name.append(data1[i][0])
        huangjin_chubei.append(data1[i][2])
        for j in range(len(data2)):
            if data1[i][1] == data2[j][1]:
                purchase.append(data2[j][2])
                break
    for i in range(100):
        j = 0
        for j in range(len(data3)):
            if data1[i][1] == data3[j][1]:
                yusuan.append(data3[j][2])
                break
    for i in range(100):
        j = 0
        for j in range(len(data4)):
            if data1[i][1] == data4[j][1]:
                peo.append(data4[j][2])
                break
    dataframe = pd.DataFrame(
        {'short_name': s_name, 'long_name': l_name, 'active service': huangjin_chubei, 'Available population': purchase, 'reach age': yusuan, 'Suitable for service':peo})
    dataframe.to_csv('./data/people/All_Data.csv', index=False, sep=',')

def main():
    getFirePowers()
    s = ['Naval_Force','Land_Force','Airpower']
    for i in range(len(s)):
        getPowers(s[i])
    proc()
    path = ['hoqin', 'money', 'equipment', 'ziyuan', 'people']
    s = [['feijicang', 'gankouhematou', 'laodonlirenshu'],
        ['huangjin_chubei', 'purchase', 'yusuan'],
         ['jiandui', 'jidui', 'tanke', 'qiantin', 'zhishengji', 'zhuangjiace'],
         ['shiyoushengcang', 'shiyouchubei', 'shiyouxiaohao'],
         ['active service', 'Available population', 'reach age', 'Suitable for service']
         ]
    for i in range(len(path)):
        for j in range(len(s[i])):
            proc_path(s[i][j], path[i])
    for i in range(len(path)):
        zhenli()
main()