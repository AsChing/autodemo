# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/29 17:34
@Auth ： Ching
@File ：log.py
@IDE ：PyCharm
@Desc ：--- 
"""
import logging
import logging.config
from autodemo.config.public_data import base_dir

# 读取日志配置文件
logging.config.fileConfig(base_dir + "\config\Logger.conf")
# 选择一个日志格式
logger = logging.getLogger("example02")#或者example01

def debug(message):
    # 定义dubug级别日志打印方法
    logger.debug(message)

def info(message):
    # 定义info级别日志打印方法
    logger.info(message)

def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)
