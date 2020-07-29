# -*- coding: utf-8 -*-
from flask import Flask, render_template
import get_Data
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    s = 'img/2020/ia_900000'
    a=142
    b='.jpg'
    paths = []
    for i in range(100):
        t = s + str(a + i) + b
        paths.append(t)
    data = pd.read_csv('./data/All_Data.csv', encoding='utf-8')
    table_Data = np.array(data)[0:100]
    return render_template('index.html', data=table_Data, paths=paths)

@app.route('/zhuxing/', methods=['POST', 'GET'])
def zhuxing():
    data = pd.read_csv('./data/power_Data.csv')
    name = np.array(data.long_name).tolist()[0:30]
    power = np.array(data.power).tolist()[0:30]
    data = pd.read_csv('./data/Land_Force.csv')
    name1 = np.array(data.long_name).tolist()[0:30]
    power1 = np.array(data.power).tolist()[0:30]
    data = pd.read_csv('./data/Naval_Force.csv')
    name2 = np.array(data.long_name).tolist()[0:30]
    power2 = np.array(data.power).tolist()[0:30]
    data = pd.read_csv('./data/Airpower.csv')
    name3 = np.array(data.long_name).tolist()[0:30]
    power3 = np.array(data.power).tolist()[0:30]
    return render_template('zhuxing.html',name=name,power=power, name1=name1,power1=power1, name2=name2,power2=power2,name3=name3,power3=power3)

@app.route('/zhexian/', methods=['POST', 'GET'])
def zhexian():
    return render_template('zhexian.html')

@app.route('/ditu/', methods=['POST', 'GET'])
def ditu():
    return render_template('ditu.html')

@app.route('/equipment/', methods=['POST', 'GET'])
def equipment():
    return render_template('equipment.html')

@app.route('/ciyun/', methods=['POST', 'GET'])
def ciyun():
    return render_template('ciyun.html')

@app.route('/hoqin/', methods=['POST', 'GET'])
def hoqin():
    return render_template('hoqin.html')

@app.route('/caizhen/', methods=['POST', 'GET'])
def caizhen():
    return render_template('caizhen.html')

@app.route('/people/', methods=['POST', 'GET'])
def people():
    return render_template('people.html')

@app.route('/ziyuan/', methods=['POST', 'GET'])
def ziyuan():
    return render_template('ziyuan.html')

if __name__ == '__main__':
    app.run(debug=True)


