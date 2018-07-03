import requests
import pymysql
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
print('curPath: ',curPath)
rootPath = os.path.split(curPath)[0]
print('rootPath: ', rootPath)
sys.path.append(rootPath)
#sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\untitled1\\databasetest\\weather_sql.py')
from databasetest.weather_sql import *
def get_city_number( url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    strs = str(r.text).split(',')
    dic = {}
    for i in strs:
        strs = i.split('|')
        if strs[1] != '省':
            dic[strs[1]] = strs[0]
    print('dic:', dic)
    return dic

def get_weather(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    print('r.text:', r.text)
    result = r.json()
    return result

def insert_province_table(curson):
    dict = get_city_number('http://m.weather.com.cn/data3/city.xml', None)
    for key, value in dict.items():
        print('key:', key)
        print('value:', value)
        print(key, value)
        insert_province(curson, key, value)

def insert_city_table(curson):
    list = select_all_province(curson)
    for i in list:
        print('i:', i)
        number = i['province_number']
        url = 'http://m.weather.com.cn/data3/city%s.xml' % number
        dic = get_city_number(url)
        for key, value in dic.items():
            insert_city_number(curson, key, value, number)

def insert_area_table(curson):
    list = select_all_city(curson)
    for i in list:
        print('i:', i)
        number = i['city_number']
        url = 'http://m.weather.com.cn/data3/city%s.xml' % number
        dic = get_city_number(url)
        for key, value in dic.items():
            insert_area_number(curson, key, value, number)


def find_weather_sql(curson, name):
    flag = True
    while flag:
        result = select_weather_sql(curson, 2, name)
        print('result_2:', result)
        if result == None:
            result = select_weather_sql(curson, 1, name)
            print('result_1:', result)
            if result == None:
                result = select_weather_sql(curson, 0, name)
                print('result_1:', result)
                if result == None:
                    name = input('你所输入的名称不正确，请重新输入：')
                else:
                    all_city_name = select_children_name_sql(curson, 0, result['province_number'])
                    print('该省对应的城市名称如下：')
                    for i in all_city_name:
                        print(i['city_name'])
                    name = input('请输入具体的城市名称：')
            else:
                all_area_name = select_children_name_sql(curson, 1, result['city_number'])
                print("该城市所对应的地区都有如下：")
                for i in all_area_name:
                    print(i['area_name'])
                new_name = input('请输入具体的地区名称：')
        else:
            flag = False
            area_number = result['area_number']
            url = 'http://www.weather.com.cn/data/cityinfo/101%s.html' % area_number
            print('url:', url)
            result = get_weather(url)
            temp1 = result['weatherinfo']['temp1']
            temp2 = result['weatherinfo']['temp2']
            weather = result['weatherinfo']['weather']
            print('温度为%s-%s' % (temp1, temp2))
            print('天气为%s' % weather)

if __name__ == '__main__':
    con = pymysql.connect(host='140.143.203.54', port=3306, user='root',
                          password='Test12345.', db='weathertest', charset='utf8',
                          cursorclass=pymysql.cursors.DictCursor)
    curson = con.cursor()
    print(os.path.realpath(__file__))
    # insert_province_table(curson)
    # con.commit()
    # con.close()
    # insert_city_table(curson)
    # insert_area_table(curson)
    #weather_sql.delete_table(curson)
    #result = weather_sql.select_weather_sql(curson, 0, '麻城')
    #name = input('please enter your adress:')
    find_weather_sql(curson, '麻城')
    con.commit()
    con.close()