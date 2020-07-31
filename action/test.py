# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/27 15:42
@Auth ： Ching
@File ：test.py
@IDE ：PyCharm
@Desc ：--- 
"""
from utils.readexcel import ReadExcel
from autodemo.config.public_data import *
import json

testdata = ReadExcel(FILE_PATH, u"Sheet1").read_data()
print(len(testdata))
for data in testdata:
    print(data)
    rowNum = int(data["casenum"].split("_")[1])
    print(rowNum)
    # print("******* 正在执行用例 ->{0} *********".format(data['用例编号']))
    # print("请求模块: {0}----------->，用例名称: {1}".format(data['模块'], data['用例名称']))
    # print("请求地址：{0}-------》，请求头：{1}".format(data['url'], data['请求头']))
    # print(json.loads(data['请求头'])['Content-Type'])
    # print("***************************》\n 请求参数 ->{0}".format(data['请求参数']))

