import pymysql
con = pymysql.connect(host='140.143.203.54',port=3306, user='root',
                      password='Test12345.', db='weathertest', charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)
curson = con.cursor()

create_city_sql = "CREATE TABLE IF NOT EXISTS `tb_city`("\
   "`city_id` INT UNSIGNED AUTO_INCREMENT,"\
   "`city_name` VARCHAR(100) NOT NULL,"\
   "`city_number` VARCHAR(40) NOT NULL,"\
   "`province_number` VARCHAR(40) NOT NULL,"\
   "PRIMARY KEY ( `city_id` )"\
   ")ENGINE=InnoDB DEFAULT CHARSET=utf8;"
create_area_sql = "CREATE TABLE IF NOT EXISTS `tb_area`("\
   "`area_id` INT UNSIGNED AUTO_INCREMENT,"\
   "`area_name` VARCHAR(100) NOT NULL,"\
   "`area_number` VARCHAR(40) NOT NULL,"\
   "`city_number` VARCHAR(40) NOT NULL,"\
   "PRIMARY KEY ( `area_id` )"\
   ")ENGINE=InnoDB DEFAULT CHARSET=utf8;"
curson.execute(create_city_sql)
curson.execute(create_area_sql)
con.commit()
con.close()