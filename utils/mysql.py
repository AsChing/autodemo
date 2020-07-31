# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/22 14:29
@Auth ： Ching
@File ：mysql.py
@IDE ：PyCharm
@Desc ：--- 封装数据库操作
"""
from pymysql import connect, cursors, OperationalError
import configparser as cparser

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read("../config/config.ini", encoding='UTF-8')
username = cf.get("mysql", "username")
password = cf.get("mysql", "password")
host = cf.get("mysql", "host")
port = cf.get("mysql", "port")
dbname = cf.get("mysql", "dbname")


class MySQL(object):

    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=username,
                                password=password,
                                db=dbname,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 查询数据
    def select(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()
            # for row in data:
            #     print(type(row))
        return data

    # 清除数据
    def clear(self, sql):
        with self.conn.cursor() as cursor:
            # 取消表的外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    mysql = MySQL()
    data = mysql.select("select title,source_id from lab_model_auction where id < 1000")
    print(type(data))
    print(data)