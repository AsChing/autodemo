# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/20 11:19
@Auth ： Ching
@File ：test.py.py
@IDE ：PyCharm
@Desc ： 测试代码
"""
# https://www.cnblogs.com/ff-gaofeng/p/12071942.html
from autodemo.config.public_data import *
from autodemo.utils.encrypt import encrpt

print(AUCTION_PUBLIC_KEY)

passs = encrpt(BUSINESS_PUBLIC_KEY, "12345")
print(passs)