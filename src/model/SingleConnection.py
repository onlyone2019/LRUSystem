# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin
#   Created date: 2019-11-29 12:22:26
#   Description : 单例模式创建数据连接类
#
#================================================================

import pymysql
from src.Config import config


#以单例模式创建数据库连接

def SingleConnection(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@SingleConnection
class MySQLSingle(object):
    def __init__(self):
        self.conn = pymysql.connect(**config.const.DB_CONFIG)
        self.conn.ping(reconnect=True)
        self.cu = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    #获取数据库链接与游标
    def getConCu(self):
        return self.conn, self.cu

    #关闭数据库链接
    def CloseConnection(self):
        self.cu.close()
        self.conn.close()