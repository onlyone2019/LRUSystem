#!/usr/bin/python3
# -*-coding:utf-8-*-
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : vscode
#   File name   : trans_txt_to_sql.py
#   Author      : WangJie
#   Created date: 2019-11-29 12:22:26
#   Description : 解析txt文件存入数据库
#
#================================================================
import re
from pymysql import connect


db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'lru'
}
filename = '28 - FUEL 燃油.txt'

ATA_regex = r'^\d+(?= -)'
child_ATA_regex = r'(?<=\s)\d+-\d+(?= -)'
grandson_ATA_regex = r'\d+-\d+-\d+(?= -)'
en_name_regex = r'(?<=\d - )[A-Z -/,]*'  # 匹配结果需要调用 strip() 方法去除空白
zh_name_regex = r'[\u4e00-\u9fa5]+[ -/]*[\u4e00-\u9fa5]*'  # 匹配结果需要调用 strip() 方法去除空白


db = connect(**db_config)
cursor = db.cursor()

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    try:
        en_name = re.search(en_name_regex, line)
        en_name = "'" + en_name.group().strip() + "'" if en_name else 'null'
        zh_name = re.search(zh_name_regex, line)
        zh_name = "'" + zh_name.group().strip() + "'" if zh_name else 'null'
        if re.search(ATA_regex, line):  # 如果是第一级
            last_ATA = {
                'ATA': "'" + re.search(ATA_regex, line).group() + "'",
                'ATA_name': en_name,
                'ATA_name_zh': zh_name
            }
        elif re.search(child_ATA_regex, line):
            last_child_ATA = {
                'child_ATA': "'" + re.search(child_ATA_regex, line).group() + "'",
                'child_ATA_name': en_name,
                'child_ATA_name_zh': zh_name
            }
        elif re.search(grandson_ATA_regex, line):
            sql = "insert into tree values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
                last_ATA['ATA'], last_ATA['ATA_name'], last_ATA['ATA_name_zh'],
                last_child_ATA['child_ATA'], last_child_ATA['child_ATA_name'], last_child_ATA['child_ATA_name_zh'],
                "'" + re.search(grandson_ATA_regex, line).group() + "'", en_name, zh_name)
            cursor.execute(sql)
        else:
            print(line)
    except:
        print(line)

db.commit()
cursor.close()
db.close()
