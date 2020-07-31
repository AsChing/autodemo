# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/23 14:53
@Auth ： Ching
@File ：sendrequest.py
@IDE ：PyCharm
@Desc ：--- 
"""
import requests
import json

class HttpClient(object):

    def request(self, ip,  apiData, **kwargs):
        try:
            # Excel中获取参数传递
            # 请求方法 post/get/update...
            method = apiData["method"]
            # 请求链接
            url = ip+apiData["url"]
            # 请求参数
            if apiData["params"] == "":
                params = None
            else:
                params = eval(apiData["params"])
            # 请求头
            if apiData["headers"] == "":
                headers = None
            else:
                headers = eval(apiData["headers"])
            # 请求体
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            # 请求体类型 data/json/url
            type = apiData["type"]

            if method == "post":
                if type == "data":
                    response = self.__post(url=url, data=json.dumps(body_data), headers=headers, **kwargs)
                    return response
                elif type == "json":
                    response = self.__post(url=url, json=body_data, headers=headers, **kwargs)
                    return response
                else:
                    print(
                        "------------------------------------参数类型：{0}-----------------------------------------".format(type))
            elif method == "get":
                response = self.__get(url=url, params=params, headers=headers, **kwargs)
                return response
            else:
                print("---------------------------------暂不支持{0}请求方法----------------------------------".format(method))
        except Exception as e:
            print("----------------报错了---------------eeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrr")
            print(e)

    def __post(self, url, data = None, json = None, headers=None, **kwargs):
        print("--------------------------->{0}<---------------------------".format("post请求"))
        response = requests.post(url=url, data=data, json=json, headers=headers).json()
        return response

    def __get(self, url, params = None, **kwargs):
        print("--------------------------->{0}<---------------------------".format("get请求"))
        response = requests.get(url, params = params, **kwargs).json()
        return response

from utils.readexcel import ReadExcel
from autodemo.config.public_data import *

if __name__ == "__main__":
    hc = HttpClient()
    headers = '{"Content-Type": "application/json;charset=UTF-8"}'
    # dat = '{"token":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MzkiLCJzdWIiOiIxNzYwNjUyNTk3NSIsImlhdCI6MTU5NTkwODI0NCwicm9sZXMiOlsi566h55CG5ZGY55So5oi3Il0sImF1dGhvcml0aWVzIjpbXSwiaG9zdCI6IjE3Mi4xOC4yNTUuMjUxOjgwIiwidXVpZCI6Ijk0YzQ0ZmZkLTFhN2UtNDhiMi04MGEwLWQzMDg5YTA2YjdiNCIsImV4cGlyZSI6MTYwMjE3Mjc5OSwiZXhwIjoxNTk1OTk0NjQ0fQ.IxbHFgd-6OKiEfFRzvLoUhEL_3FCFouPO4Gf6k7v_0o","page": "1"}'
    # res = hc.request("get", "http://172.18.255.251:8588/yc/monitor/bankruptcy/list", "url", dat, headers)
    # print(res.json())

    # data = '{"username": "17606525975", "password": "B49UhVDmrDJJ4jD+9IeWbH5rWZmdfBR+2ICkt/Q2EYOq5CIsRRYu4hhdYzVWTKxiiGS312ycg550jX9f/NBWFB4JjqsKqOCHO3drB4AQHqsnRc66UwgE3mPW7rn/mezqjrSCdXmlwH+lBkEG2k4w27iKXx8ohNl/s6T+/UC1jdk="}'
    # re = hc.request("post", "http://172.18.255.251:8588/api/auth/login", "form", data, headers)
    # print(re.json())

    testdata = ReadExcel(FILE_PATH, u"Sheet1").read_data()
    for data in testdata:
        res = hc.request("http://172.18.255.251:8588", data)
        print(res)

