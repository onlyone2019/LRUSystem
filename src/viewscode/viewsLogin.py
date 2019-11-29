# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin、WangJie、MaTao
#   Created date: 2019-11-29 20:22:26
#   Description : 登陆界面视图类
#
#================================================================
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        mysql_single, cu = MySQLSingle().getConCu()
        uaccount = request.POST.get('uaccount')
        upassword = request.POST.get('upassword')
        cu.execute("select upassword from user where uaccount =" + uaccount)
        a = cu.fetchall()
        # print(str(a))
        if len(a) > 0:
             if a[0]['upassword'] == upassword:
                return render(request, 'main.html')
             else:
                return render(request,'login.html',{'script':"alert",'wrong':'密码错误'})
        else:
             return render(request,'login.html',{'script':"alert",'wrong':'账号不存在'})
