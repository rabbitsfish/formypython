
def insert_province(curson, name, number):
    sql = "insert into tb_province (province_name, province_number) values " \
"(%s, %s)" % (repr(name), repr(number))
    print(sql)
    curson.execute(sql)

def select_all_province(curson):
    sql = 'select province_number from tb_province;'
    print(sql)
    curson.execute(sql)
    result = curson.fetchall()
    return result

def insert_city_number(curson, name, number, p_number):
    sql = "insert into tb_city (city_name, city_number, province_number) values " \
"(%s, %s, %s)" % (repr(name), repr(number), repr(p_number))
    print(sql)
    curson.execute(sql)

def select_all_city(curson):
    sql = 'select city_number from tb_city'
    print(sql)
    curson.execute(sql)
    result = curson.fetchall()
    return result

def insert_area_number(curson, name, number, c_number):
    sql = "insert into tb_area (area_name, area_number, city_number) values " \
          "(%s, %s, %s)" % (repr(name), repr(number), repr(c_number))
    print(sql)
    curson.execute(sql)

def delete_table(curson):
    sql = 'truncate tb_city'
    curson.execute(sql)
    curson.execute('truncate table tb_area')

def select_weather_sql(curson, table_number, name):
    if table_number == 0:
        sql = "select province_number from tb_province where province_name = %s" % (repr(name))
    elif table_number == 1:
        sql = "select city_number from tb_city where city_name = %s " % repr(name)
    else:
        sql = "select area_number from tb_area where area_name = %s" % repr(name)
    curson.execute(sql)
    result = curson.fetchone()
    return result

def select_children_name_sql(curson, table_number, number):
    if table_number == 0:
        sql = "select city_name from tb_city where province_number = %s" % repr(number)
    else:
        sql = "select area_name from tb_area where city_number = %s" % repr(number)
    curson.execute(sql)
    result = curson.fetchall()
    return result
