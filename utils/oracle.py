# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/22 14:29
@Auth ： Ching
@File ：mysql.py
@IDE ：PyCharm
@Desc ：--- 封装数据库操作
"""
from cx_Oracle import connect, OperationalError
import configparser as cparser

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read("../config/config.ini", encoding='UTF-8')
username = cf.get("oracle", "username")
password = cf.get("oracle", "password")
service = cf.get("oracle", "ip_host_service")


class Oracle(object):

    def __init__(self):
        try:
            self.conn = connect(username, password, service)
        except OperationalError as e:
            print("Oracle Error %d: %s" % (e.args[0], e.args[1]))

    # 查询数据
    def select(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()
            cols = [i[0] for i in cursor.description]
            result = []
            for row in data:
                result.append(dict(zip(cols, row)))
        return result

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
    oracle = Oracle()
    data = oracle.select("SELECT * from BMS_OBLIGOR where id < 1210405402496208898")
    print(data)
