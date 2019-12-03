# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : viewSearchInfo.py
#   Author      : WangJin
#   Created date: 2019-11-29 12:22:26
#   Description : 详细部件查询页面
#
#================================================================

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle



#左侧导航栏点击后获取信息
def getPnrs(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        data = request.POST
        message = data.get('message')
        print("信息查询页面请求ata部件:"+ message)
        info = message.split("-")
        '''
        cu.execute(
            'create or REPLACE view combine(mername,pmodel,pnr) as select manufacturer.Mername as a,pmodel.PModelname as b,apply.prn as c from  pmodel INNER join manufacturer on pmodel.Mername = manufacturer.Mername inner join apply on pmodel.PModelname = apply.PModelname')
        mysql_single.commit()
        '''
        cu.execute('SELECT DISTINCT * from combine inner join component on combine.pnr=component.PNR where combine.mername="%s" and combine.pmodel="%s" and component.ATA="%s"'%(info[0],info[1],info[2]))
        table_data = cu.fetchall()
        json_str = {}
        json_str['total'] = len(table_data)
        json_str['rows'] = table_data
        return JsonResponse(json_str,safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")





#左侧导航栏获取数据库信息
def searchInfo(request):
    mysql_single, cu = MySQLSingle().getConCu()
    cu.execute('SELECT DISTINCT Mername from manufacturer')
    fist_res = cu.fetchall()
    result =[]
    fist_node = {}
    second_node = {}
    thrid_node = {}
    for i in range(0, len(fist_res)):
        fist_node['id'] = fist_res[i]['Mername']
        fist_node['pId'] = '-1'
        fist_node['name'] = fist_res[i]['Mername']
        fist_node['child'] =[]
        cu.execute('SELECT DISTINCT PModelname from pmodel where Mername="%s"' % fist_res[i]['Mername'])
        second_res = cu.fetchall()
        for j in range(0, len(second_res)):
            cu.execute(
                'SELECT DISTINCT ATA from apply INNER JOIN component on apply.prn=component.PNR where apply.PModelname="%s"' %
                second_res[j]['PModelname'])
            thrid_res = cu.fetchall()
            second_node['id'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname']
            second_node['pId'] = fist_res[i]['Mername']
            second_node['name'] = second_res[j]['PModelname']
            second_node['child'] = []

            for k in range(0, len(thrid_res)):
                thrid_node['id'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname'] + "-" + thrid_res[k]['ATA']
                thrid_node['pId'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname']
                thrid_node['name'] = thrid_res[k]['ATA']
                second_node['child'].append(thrid_node.copy())
            fist_node['child'].append(second_node.copy())
        result.append(fist_node.copy())
    return render(request, 'searchInfo.html', {'node_list':result})




#高级选项框内容
def getManuPmodelATA(request):
    if request.method == "POST":
        mysql_single, cu = MySQLSingle().getConCu()
        print("信息查询页面请求各种信息列表")
        cu.execute("select distinct Mername from manufacturer")
        res_mername = cu.fetchall()
        i = 0
        result_Mername=[]
        temp={}
        for obj in range(0, len(res_mername)):
            temp['id'] = res_mername[i]['Mername']
            temp['text'] = res_mername[i]['Mername']
            result_Mername.append(temp.copy())
            i = i + 1
        cu.execute("select distinct ATA from component")
        res_ata = cu.fetchall()
        i = 0
        result_ATA = []
        temp = {}
        for obj in range(0, len(res_ata)):
            temp['id'] = res_ata[i]['ATA']
            temp['text'] = res_ata[i]['ATA']
            result_ATA.append(temp.copy())
            i = i + 1
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
        result={}
        result['ATA'] = result_ATA
        result['PModelname'] = result_pmodel
        result['Mername'] =  result_Mername
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


#高级查询按钮点击后获取信息
def getAdvancePnrs(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        data = request.POST
        atas = data.get('ATAs')
        PModelnames = data.get('PModelnames')
        Mernames = data.get('Mernames')

        print("高级信息查询页面请求ata部件:\n"+ str(atas) + "\n" + str(PModelnames) + "\n"+str(Mernames))
        '''
        cu.execute(
            'create or REPLACE view combine(mername,pmodel,pnr) as select manufacturer.Mername as a,pmodel.PModelname as b,apply.prn as c from  pmodel INNER join manufacturer on pmodel.Mername = manufacturer.Mername inner join apply on pmodel.PModelname = apply.PModelname')
        mysql_single.commit()
        '''
        #为不同的情况构建子句
        flag_ata = (0 == len(atas.strip()))
        flag_pmod = (0 == len(PModelnames.strip()))
        flag_man = (0 == len(Mernames.strip()))

        if (flag_ata) and (flag_man) and (flag_pmod):
            where_str = ''
        elif (flag_ata) and (flag_man) and (not flag_pmod):
            where_str = 'where combine.pmodel in (%s)'%('\''+str(PModelnames).replace(',','\',\'')+'\'')
        elif (flag_ata) and (not flag_man) and (flag_pmod):
            where_str = 'where combine.mername in (%s)'%('\''+str(Mernames).replace(',','\',\'')+'\'')
        elif (flag_ata) and (not flag_man) and (not flag_pmod):
            where_str = 'where combine.mername in (%s) and combine.pmodel in (%s)'%('\''+str(Mernames).replace(',','\',\'')+'\'','\''+str(PModelnames).replace(',','\',\'')+'\'')
        elif (not flag_ata) and (flag_man) and (flag_pmod):
            where_str = 'where component.ATA in (%s)' % ('\'' + str(atas).replace(',', '\',\'') + '\'')
        elif (not flag_ata) and (flag_man) and (not flag_pmod):
            where_str = 'where component.ATA in (%s) and combine.pmodel in (%s)' % (
                '\'' + str(atas).replace(',', '\',\'') + '\'', '\'' + str(PModelnames).replace(',', '\',\'') + '\'')
        elif (not flag_ata) and (not flag_man) and (flag_pmod):
            where_str = 'where component.ATA in (%s) and combine.mername in (%s)' % (
                '\'' + str(atas).replace(',', '\',\'') + '\'', '\'' + str(Mernames).replace(',', '\',\'') + '\'')
        elif (not flag_ata) and (not flag_man) and (not flag_pmod):
            where_str = 'where component.ATA in (%s) and combine.mername in (%s) and combine.pmodel in (%s)' % (
                '\'' + str(atas).replace(',', '\',\'') + '\'', '\'' + str(Mernames).replace(',', '\',\'') + '\'','\'' + str(PModelnames).replace(',', '\',\'') + '\'')
        sql_str = 'SELECT DISTINCT * from combine inner join component on combine.pnr=component.PNR %s' % where_str
        cu.execute(sql_str)
        table_data = cu.fetchall()
        json_str = {}
        json_str['total'] = len(table_data)
        json_str['rows'] = table_data
        return JsonResponse(json_str, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return HttpResponse("收到")

#获取所有零件
def getAllPnrs(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        '''
        cu.execute(
            'create or REPLACE view combine(mername,pmodel,pnr) as select manufacturer.Mername as a,pmodel.PModelname as b,apply.prn as c from  pmodel INNER join manufacturer on pmodel.Mername = manufacturer.Mername inner join apply on pmodel.PModelname = apply.PModelname')
        mysql_single.commit()
        '''
        cu.execute('SELECT DISTINCT * from combine inner join component on combine.pnr=component.PNR')
        table_data = cu.fetchall()
        json_str = {}
        json_str['total'] = len(table_data)
        json_str['rows'] = table_data
        return JsonResponse(json_str,safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")


#获取所有属性信息
def getAllPropertyInfos(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        print('前台请求属性列表')
        cu.execute('SELECT CPname, CPremark,CPother from componentproperty')
        table_data = cu.fetchall()
        json_str = {}
        json_str['total'] = len(table_data)
        json_str['rows'] = table_data
        return JsonResponse(json_str,safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")

#获取所有属性列名称
def getPropertysaAndClass(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        cu.execute('SELECT DISTINCT CPname from componentproperty ')
        table_data = cu.fetchall()
        temp = {}
        result_property = []
        i = 0
        for obj in range(0, len(table_data)):
            temp['id'] = table_data[i]['CPname']
            temp['text'] = table_data[i]['CPname']
            result_property.append(temp.copy())
            i = i + 1
        cu.execute('SELECT DISTINCT Claname from classification ')
        class_data = cu.fetchall()
        temp = {}
        result_class = []
        i = 0
        for obj in range(0, len(class_data)):
            temp['id'] = class_data[i]['Claname']
            temp['text'] = class_data[i]['Claname']
            result_class.append(temp.copy())
            i = i + 1
        result = {}
        result['CPnameList'] = result_property
        result['ClanameList'] = result_class
        return JsonResponse(result, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")


#获取分级属性列名称
def getClassProperty(request):
    if request.is_ajax():
        data = request.POST
        message = data.get('message')
        print('分级筛选:'+str(message))
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        cu.execute('SELECT DISTINCT CPname from classification where Claname in (%s)' % ('\'' + str(message).replace(',', '\',\'') + '\''))
        table_data = cu.fetchall()
        res = []
        for i in range(0, len(table_data)):
            res.append(table_data[i]['CPname'])
        return JsonResponse(res, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse("收到")
