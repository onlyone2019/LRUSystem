# coding=utf-8
# ================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Vscode
#   File name   : viewSearchInfo.py
#   Author      : WangJie、Matao
#   Created date: 2019-11-29 20:30:21
#   Description : 结构树形展示界面视图类
#
# ================================================================

from django.http import JsonResponse
from django.shortcuts import render

from src.model.SingleConnection import MySQLSingle


def structureTree(request):
    # mysql_single, cu = MySQLSingle().getConCu()
    # cu.execute('SELECT DISTINCT Mername from manufacturer')
    # fist_res = cu.fetchall()
    # result =[]
    # fist_node = {}
    # second_node = {}
    # thrid_node = {}
    # for i in range(0, len(fist_res)):
    #     fist_node['id'] = fist_res[i]['Mername']
    #     fist_node['pId'] = '-1'
    #     fist_node['name'] = fist_res[i]['Mername']
    #     fist_node['child'] =[]
    #     cu.execute('SELECT DISTINCT PModelname from pmodel where Mername="%s"' % fist_res[i]['Mername'])
    #     second_res = cu.fetchall()
    #     for j in range(0, len(second_res)):
    #         cu.execute(
    #             'SELECT DISTINCT ATA from apply INNER JOIN component on apply.prn=component.PNR where apply.PModelname="%s"' %
    #             second_res[j]['PModelname'])
    #         thrid_res = sorted(cu.fetchall(), key=lambda i : int(i['ATA']))
    #         second_node['id'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname']
    #         second_node['pId'] = fist_res[i]['Mername']
    #         second_node['name'] = second_res[j]['PModelname']
    #         second_node['child'] = []

    #         for k in range(0, len(thrid_res)):
    #             thrid_node['id'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname'] + "-" + thrid_res[k]['ATA']
    #             thrid_node['pId'] = fist_res[i]['Mername'] + "-" + second_res[j]['PModelname']
    #             thrid_node['name'] = thrid_res[k]['ATA']
    #             second_node['child'].append(thrid_node.copy())
    #         fist_node['child'].append(second_node.copy())
    #     result.append(fist_node.copy())
    result = [
        {'id': '空客',
         'pId': '-1',
         'name': '空客',
         'child': [
             {'id': '空客-A321',
              'pId': '空客',
              'name': 'A321',
              'child': [
                  {'id': '空客-A320-28',
                   'pId': '空客-A320',
                   'name': '28'},
                  {'id': '空客-A320-32',
                   'pId': '空客-A320',
                   'name': '32'},
                  {'id': '空客-A320-34',
                   'pId': '空客-A320',
                   'name': '34'}]}]}]
    return render(request, 'structureTree.html', {'node_list': result})


def alllevel(request):  # 返回整棵树内容
    mysql_single, cu = MySQLSingle().getConCu()
    cu.execute(
        'select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="28"')
    message = cu.fetchall()
    result = []
    second = []
    i = 0
    tmp = {}
    tmp['id'] = '28'
    tmp['pId'] = '0'
    tmp['name'] = '燃油'
    result.append(tmp.copy())
    for i in range(0, len(message)):
        tmp['id'] = message[i]['child_ATA']
        tmp['pId'] = '28'
        if message[i]['child_ATA_name_zh'] != None:
            tmp['name'] = message[i]['child_ATA_name_zh']
        else:
            tmp['name'] = message[i]['child_ATA_name']
        second.append(message[i]['child_ATA'])
        result.append(tmp.copy())
    for i in range(0, len(second)):
        cu.execute(
            'select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA="%s"' % second[i])
        message = cu.fetchall()
        for j in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[j]['grandson_ATA']
            tmp['pId'] = second[i]
            if message[j]['grandson_ATA_name_zh'] != None:
                tmp['name'] = message[j]['grandson_ATA_name_zh']
            else:
                tmp['name'] = message[j]['grandson_ATA_name']
            # print(tmp)
            result.append(tmp.copy())
    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


def getTree(request):  # 返回具体的树内容
    ATAnum = '28'
    plane = 'A321'
    if request.method == "GET":
        plane = request.GET.get('plane', default='A321')
        ATAnum = request.GET.get('ATAnum', default='28')
        mysql_single, cu = MySQLSingle().getConCu()
        cu.execute('select DISTINCT ATA,ATA_name,ATA_name_zh from newtree where ATA="%s" and Plane="%s"' % (
            ATAnum, plane))
        message = cu.fetchall()
        result = {}
        for i in range(0, len(message)):
            result['name'] = message[i]['ATA_name_zh']
            break
        result['children'] = []
        cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from newtree where ATA="%s" and Plane="%s"' % (
            ATAnum, plane))
        message = cu.fetchall()
        for i in range(0, len(message)):
            child1 = {}
            if message[i]['child_ATA_name_zh'] != None:
                child1['name'] = message[i]['child_ATA_name_zh']
            else:
                child1['name'] = message[i]['child_ATA_name']
            to_search = message[i]['child_ATA']
            child1['children'] = []
            cu.execute('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from newtree where child_ATA="%s" and Plane="%s"' % (
                to_search, plane))
            data = cu.fetchall()
            for item in range(0, len(data)):
                tmp = {}
                nm = ""
                if data[item]['grandson_ATA_name_zh'] != None:
                    nm = data[item]['grandson_ATA_name_zh']
                else:
                    nm = data[item]['grandson_ATA_name']
                tmp['name'] = nm
                child1['children'].append(tmp.copy())
            result['children'].append(child1.copy())
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
