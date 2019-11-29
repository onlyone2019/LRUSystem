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
        cu.execute(
            'create or REPLACE view combine(mername,pmodel,pnr) as select manufacturer.Mername as a,pmodel.PModelname as b,apply.prn as c from  pmodel INNER join manufacturer on pmodel.Mername = manufacturer.Mername inner join apply on pmodel.PModelname = apply.PModelname')
        mysql_single.commit()
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


def getAtA(request):
    if request.is_ajax():
        mysql_single, cu = MySQLSingle().getConCu()
        # 直接获取所有的post请求数据
        data = request.POST
        message = data.get('message')
        print("信息查询页面请求ata号列表:" + message)
        cu.execute("select distinct from component")
        res = cu.fetchall()
        return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})