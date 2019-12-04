# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin、WangJie、MaTao
#   Created date: 2019-11-29 20:22:26
#   Description : 主界面视图类
#
#================================================================
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def main(request):
    mysql_single, cu = MySQLSingle().getConCu()
    cu.execute(
        'select count(*) as anumber  from component ')
    cu_comnumber = cu.fetchall()
    cu.execute(
        'select count(*) as anumber  from pmodel ')
    cu_pmodelnumber = cu.fetchall()
    cu.execute(
        'select count(*) as anumber  from manufacturer ')
    cu_mannumber = cu.fetchall()
    cu.execute(
        'select count(*) as anumber  from user ')
    cu_usernumber = cu.fetchall()
    return render(request, 'main.html',{'com':cu_comnumber[0]['anumber'],'pmo':cu_pmodelnumber[0]['anumber'],'man':cu_mannumber[0]['anumber'],'user':cu_usernumber[0]['anumber']})