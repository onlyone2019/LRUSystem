# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin、WangJie、MaTao
#   Created date: 2019-11-29 20:22:26
#   Description : 数据分析视图类
#
#================================================================
from django.shortcuts import render


def chart(request):
    return render(request, 'analysis.html')