# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Vscode
#   File name   : viewSearchInfo.py
#   Author      : WangJie、Matao
#   Created date: 2019-11-29 20:30:21
#   Description : 结构树形展示界面视图类
#
#================================================================

from django.http import JsonResponse
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def structureTree(request):
    return render(request, 'structureTree.html')


def alllevel(request):  #返回整棵树内容
    mysql_single, cu = MySQLSingle().getConCu()
    cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="28"')
    message = cu.fetchall()
    result = []
    second=[]
    i = 0
    tmp = {}
    tmp['id'] = '28'
    tmp['pId'] = '0'
    tmp['name'] = '燃油'
    result.append(tmp.copy())
    for i in range(0, len(message)):
        tmp['id'] = message[i]['child_ATA']
        tmp['pId']='28'
        if message[i]['child_ATA_name_zh'] != None:
            tmp['name'] = message[i]['child_ATA_name_zh']
        else:
            tmp['name'] = message[i]['child_ATA_name']
        second.append(message[i]['child_ATA'])
        result.append(tmp.copy())
    for i in range(0, len(second)):
        cu.execute('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA="%s"' % second[i])
        message = cu.fetchall()
        for j in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[j]['grandson_ATA']
            tmp['pId']=second[i]
            if message[j]['grandson_ATA_name_zh'] != None:
                tmp['name'] = message[j]['grandson_ATA_name_zh']
            else:
                tmp['name'] = message[j]['grandson_ATA_name']
            # print(tmp)
            result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getTree(request):  #返回具体的树内容
    ATAnum = '28'
    plane='A321'
    if request.method == "GET":
        plane=request.GET.get('plane', default='A321')
        ATAnum = request.GET.get('ATAnum', default='28')
        mysql_single, cu = MySQLSingle().getConCu()
        cu.execute('select DISTINCT ATA,ATA_name,ATA_name_zh from newtree where ATA="%s" and Plane="%s"' %(ATAnum,plane))
        message = cu.fetchall()
        result = {}
        for i in range(0, len(message)):
            result['name'] = message[i]['ATA_name_zh']
            break
        result['children'] = []
        cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from newtree where ATA="%s" and Plane="%s"' % (ATAnum, plane))
        message = cu.fetchall()
        for i in range(0, len(message)):
            child1 = {}
            if message[i]['child_ATA_name_zh'] != None:
                child1['name'] = message[i]['child_ATA_name_zh']
            else:
                child1['name'] = message[i]['child_ATA_name']
            to_search = message[i]['child_ATA']
            child1['children'] = []
            cu.execute('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from newtree where child_ATA="%s" and Plane="%s"' % (to_search, plane))
            data = cu.fetchall()
            for item in range(0, len(data)):
                tmp={}
                nm=""
                if data[item]['grandson_ATA_name_zh'] != None:
                    nm = data[item]['grandson_ATA_name_zh']
                else:
                    nm = data[item]['grandson_ATA_name']
                tmp['name']=nm
                child1['children'].append(tmp.copy())
            result['children'].append(child1.copy())
        return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})
