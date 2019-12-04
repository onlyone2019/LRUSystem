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
from django.http import JsonResponse, HttpResponse
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

#获取ESS（图1）
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

#获取MFR每个分组（图2）
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


#获取ATA每个分组（图3）
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


#获取ATAESS每个分组（图4）
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


#获取SPC（图5）
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

#获取所有供应商信息
def getAllMFRCodes(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        data = request.POST
        pmodel = data.get('pmodel')
        print('前台请求供应商列表')
        cu.execute('SELECT CODE, Name,Address from MFRCode where pmodel ="%s"'%pmodel)
        table_data = cu.fetchall()
        json_str = {}
        json_str['total'] = len(table_data)
        json_str['rows'] = table_data
        return JsonResponse(json_str,safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")


#获取ATAESS每个分组（图6）
def getSPCESSNumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('pmodel')
        cu.execute('select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "1" and component.SPC = "1" ' % pmodel)
        cu_spc1_ess1 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "2" and component.SPC = "1" ' % pmodel)
        cu_spc1_ess2 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "3" and component.SPC = "1" ' % pmodel)
        cu_spc1_ess3 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "1" and component.SPC = "2" ' % pmodel)
        cu_spc2_ess1 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "2" and component.SPC = "2" ' % pmodel)
        cu_spc2_ess2 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "3" and component.SPC = "2" ' % pmodel)
        cu_spc2_ess3 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "1" and component.SPC = "6" ' % pmodel)
        cu_spc6_ess1 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "2" and component.SPC = "6" ' % pmodel)
        cu_spc6_ess2 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ESS = "3" and component.SPC = "6" ' % pmodel)
        cu_spc6_ess3 = cu.fetchall()
        #first = ['spc', 1, 2, 6]
        second = ['ESS=1', cu_spc1_ess1[0]['anumber'], cu_spc2_ess1[0]['anumber'], cu_spc6_ess1[0]['anumber']]
        thrid = ['ESS=2', cu_spc1_ess2[0]['anumber'], cu_spc2_ess2[0]['anumber'], cu_spc6_ess2[0]['anumber']]
        fourth = ['ESS=3', cu_spc1_ess3[0]['anumber'], cu_spc2_ess3[0]['anumber'], cu_spc6_ess3[0]['anumber']]
        res = []
        #res.append(first)
        res.append(second)
        res.append(thrid)
        res.append(fourth)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


#获取每个分组（图7）
def getATASPCNumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('pmodel')
        cu.execute('select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.SPC = "1" ' % pmodel)
        cu_spc1_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.SPC = "1" ' % pmodel)
        cu_spc1_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.SPC = "1" ' % pmodel)
        cu_spc1_ata34 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.SPC = "2" ' % pmodel)
        cu_spc2_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.SPC = "2" ' % pmodel)
        cu_spc2_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.SPC = "2" ' % pmodel)
        cu_spc2_ata34 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.SPC = "6" ' % pmodel)
        cu_spc6_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.SPC = "6" ' % pmodel)
        cu_spc6_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.SPC = "6" ' % pmodel)
        cu_spc6_ata34 = cu.fetchall()
        #first = ['spc', 1, 2, 6]
        second = ['ATA=28', cu_spc1_ata28[0]['anumber'], cu_spc2_ata28[0]['anumber'], cu_spc6_ata28[0]['anumber']]
        thrid = ['ATA=32', cu_spc1_ata32[0]['anumber'], cu_spc2_ata32[0]['anumber'], cu_spc6_ata32[0]['anumber']]
        fourth = ['ATA=34', cu_spc1_ata34[0]['anumber'], cu_spc2_ata34[0]['anumber'], cu_spc6_ata34[0]['anumber']]
        res = []
        #res.append(first)
        res.append(second)
        res.append(thrid)
        res.append(fourth)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


#获取每个分组（图8）
def getATA2ESSNumbers(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        data = request.POST
        pmodel = data.get('pmodel')
        cu.execute('select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.ESS = "1" ' % pmodel)
        cu_ess1_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.ESS = "1" ' % pmodel)
        cu_ess1_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.ESS = "1" ' % pmodel)
        cu_ess1_ata34 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.ESS = "2" ' % pmodel)
        cu_ess2_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.ESS = "2" ' % pmodel)
        cu_ess2_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.ESS = "2" ' % pmodel)
        cu_ess2_ata34 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "28" and component.ESS = "3" ' % pmodel)
        cu_ess3_ata28 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "32" and component.ESS = "3" ' % pmodel)
        cu_ess3_ata32 = cu.fetchall()
        cu.execute(
            'select count(*) as anumber  from component inner join apply where apply.prn = component.PNR and apply.PModelname="%s" and component.ATA = "34" and component.ESS = "3" ' % pmodel)
        cu_ess3_ata34 = cu.fetchall()
        #first = ['spc', 1, 2, 6]
        second = ['ATA=28', cu_ess1_ata28[0]['anumber'], cu_ess2_ata28[0]['anumber'], cu_ess3_ata28[0]['anumber']]
        thrid = ['ATA=32', cu_ess1_ata32[0]['anumber'], cu_ess2_ata32[0]['anumber'], cu_ess3_ata32[0]['anumber']]
        fourth = ['ATA=34', cu_ess1_ata34[0]['anumber'], cu_ess2_ata34[0]['anumber'], cu_ess3_ata34[0]['anumber']]
        res = []
        #res.append(first)
        res.append(second)
        res.append(thrid)
        res.append(fourth)
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})