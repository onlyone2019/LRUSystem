# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : constant.py
#   Author      : WangJin
#   Created date: 2019-11-29 12:20:26
#   Description : 常量定义文件
#                 常量定义规范const.XXXXX
#================================================================
from src.Config import constant

const = constant.Const()

#这里需要改成你的数据库名
const.DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'wangjin',
    'db':'lru'
}
