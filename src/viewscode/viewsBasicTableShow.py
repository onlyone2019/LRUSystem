# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin、WangJie、MaTao
#   Created date: 2019-11-29 20:22:26
#   Description : 数据库表基本展示视图类
#
#================================================================
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def tableshow(request):
    mysql_single, cu = MySQLSingle().getConCu()
    cu.execute(
        "SELECT * FROM `component`")
    a = cu.fetchall()
    cu.execute(
        "SELECT * FROM `manufacturer`")
    b = cu.fetchall()
    cu.execute(
        "SELECT * FROM `pmodel`")
    pmodel = cu.fetchall()
    cu.execute(
        "SELECT * FROM `cpclass`")
    cpclass = cu.fetchall()
    cu.execute(
        "SELECT * FROM `componentproperty`")
    componentproperty = cu.fetchall()
    return render(request, 'tableshow.html', {'row_list': a,'manu_list':b,'pmodel_list':pmodel,'cpclass_list':cpclass,'componentproperty_list':componentproperty})
