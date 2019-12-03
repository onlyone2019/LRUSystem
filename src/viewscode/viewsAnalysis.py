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
from django.http import JsonResponse
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def chart(request):
    #预先获取数据
    mysql_single, cu = MySQLSingle().getConCu()
    print("分析页面预加载...")
    cu.execute("select distinct PModelname from pmodel")
    res_pmodel = cu.fetchall()
    i = 0
    result_pmodel = []
    temp = {}
    for obj in range(0, len(res_pmodel)):
        temp['id'] = res_pmodel[i]['PModelname']
        temp['text'] = res_pmodel[i]['PModelname']
        result_pmodel.append(temp.copy())
        i = i + 1
    print(result_pmodel)
    return render(request, 'analysis.html',{'PModelname':result_pmodel})

#获取ESS
def getEss(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('message')
        print("请求ess信息列表")
        cu.execute('select ESS  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s"'% pmodel)
        cu_ess = cu.fetchall()
        re_ess = []
        temp = {}
        ESS_1 = 0
        ESS_2 = 0
        ESS_3 = 0
        for i in range(0,len(cu_ess)):
            number = cu_ess[i]['ESS']
            if  number == '1':
                ESS_1 += 1
            elif number == '2':
                ESS_2 += 1
            elif number == '3':
                ESS_3 += 1
        temp['value'] = ESS_1
        temp['name'] = 'ESS=1'
        re_ess.append(temp.copy())
        temp['value'] = ESS_2
        temp['name'] = 'ESS=2'
        re_ess.append(temp.copy())
        temp['value'] = ESS_3
        temp['name'] = 'ESS=3'
        re_ess.append(temp.copy())
        return JsonResponse(re_ess, safe=False, json_dumps_params={'ensure_ascii': False})

#获取MFR每个分组
def getMfrNumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('message')
        print("请柱状图信息列表")
        cu.execute('select component.MFR as MFRname,count(*) as lnumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" GROUP BY component.MFR ORDER BY lnumber DESC' % pmodel)
        cu_ess = cu.fetchall()
        result_MFR = []
        result_number = []
        res = {}
        number = 20 #限制数量
        for i in range(0, len(cu_ess)):
            if i >= 20:
                break
            result_MFR.append(cu_ess[i]['MFRname'])
            result_number.append(cu_ess[i]['lnumber'])
        res['MFR'] = result_MFR
        res['number'] = result_number
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


#获取ATA每个分组
def getATANumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('message')
        print("请横向柱状图信息列表")
        cu.execute('select component.ATA as ATAname,count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" GROUP BY component.ATA ' % pmodel)
        cu_ess = cu.fetchall()
        result_MFR = []
        result_number = []
        res = {}
        for i in range(0, len(cu_ess)):
            result_MFR.append("ATA" + str(cu_ess[i]['ATAname']))
            result_number.append(cu_ess[i]['anumber'])
        res['ATA'] = result_MFR
        res['number'] = result_number
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


#获取ATAESS每个分组
def getATAESSNumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('pmodel')
        ess = data.get('ess')
        ess_str = '1'
        if ess == 'NO-GO项目(ESS=1)':
            ess_str = '1'
        elif ess == 'GO-IF项目(ESS=2)':
            ess_str = '2'
        elif ess == 'GO项目(ESS=3)':
            ess_str = '3'
        print("请横向柱状图信息列表")
        cu.execute('select component.ATA as ATAname,count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "%s" GROUP BY component.ATA ' % (pmodel, ess_str))
        cu_ess = cu.fetchall()
        result_MFR = []
        result_number = []
        res = {}
        for i in range(0, len(cu_ess)):
            result_MFR.append(cu_ess[i]['ATAname'])
            result_number.append(cu_ess[i]['anumber'])
        res['ATA'] = result_MFR
        res['number'] = result_number
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


#获取SPC
def getSPC(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('message')
        print("请求SPC信息列表")
        cu.execute('select SPC  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s"'% pmodel)
        cu_ess = cu.fetchall()
        re_ess = []
        temp = {}
        SPC_1 = 0
        SPC_2 = 0
        SPC_3 = 0
        for i in range(0,len(cu_ess)):
            number = cu_ess[i]['SPC']
            if  number == '1':
                SPC_1 += 1
            elif number == '2':
                SPC_2 += 1
            elif number == '6':
                SPC_3 += 1
        temp['value'] = SPC_1
        temp['name'] = 'SPC=1'
        re_ess.append(temp.copy())
        temp['value'] = SPC_2
        temp['name'] = 'SPC=2'
        re_ess.append(temp.copy())
        temp['value'] = SPC_3
        temp['name'] = 'SPC=6'
        re_ess.append(temp.copy())
        return JsonResponse(re_ess, safe=False, json_dumps_params={'ensure_ascii': False})