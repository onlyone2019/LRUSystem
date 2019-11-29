# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : SingleConnection.py
#   Author      : WangJin
#   Created date: 2019-11-29 12:22:26
#   Description : 厂商类先不用
#
#================================================================
from django.db import models


class manufacturer(models.Model):
    Mername = models.CharField(max_length=50)
    Merother =  models.CharField(max_length=50)