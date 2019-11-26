from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
import pymysql
from django.contrib import messages


import json
# Create your views here.

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'm1358044937',
    'db':'lru'
}

con = pymysql.connect(**db_config)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # data = request.POST
        # print(str(data))
        uaccount = request.POST.get('uaccount')
        upassword = request.POST.get('upassword')
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute("select upassword from user where uaccount =" + uaccount)
        a = cu.fetchall()
        # print(str(a))
        cu.close()
        if len(a) > 0:
             if a[0]['upassword'] == upassword:
                return render(request, 'main.html')
             else:
                return render(request,'login.html',{'script':"alert",'wrong':'密码错误'})
        else:
             return render(request,'login.html',{'script':"alert",'wrong':'账号不存在'})


def main(request):
    return render(request, 'main.html')


def chart(request):
    return render(request, 'chart-flot.html')


def table(request):
    return render(request, 'table-basic.html')

def tabletest(request):
    return render(request, 'tabletest.html')


def tableshow(request):
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute(
        "SELECT * FROM `component`")
    a = cu.fetchall()
    cu.execute(
        "SELECT * FROM `manufacturer`")
    b = cu.fetchall()
    cu.execute(
        "SELECT * FROM `pmodel`")
    pmodel = cu.fetchall()
    cu.execute(
        "SELECT * FROM `cpclass`")
    cpclass = cu.fetchall()
    cu.execute(
        "SELECT * FROM `componentproperty`")
    componentproperty = cu.fetchall()
    # print(str(a))
    # print(str(b))
    cu.close()
    return render(request, 'tableshow.html', {'row_list': a,'manu_list':b,'pmodel_list':pmodel,'cpclass_list':cpclass,'componentproperty_list':componentproperty})

def firstlevel(request):  #返回章节树的最顶层节点
                          #字典形式返回对应章节的id和name(优先中文名，没有则选英文名)
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select DISTINCT ATA,ATA_name,ATA_name_zh from tree')
    message = cu.fetchall()
    result = []
    i=0
    for i in range(0, len(message)):
        tmp = {}
        tmp['id'] = message[i]['ATA']
        if message[i]['ATA_name_zh'] != None :
            tmp['name'] = message[i]['ATA_name_zh']
        else:
            tmp['name'] = message[i]['ATA_name']
        result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def secondlevel(request):  #返回章节树 第二级节点 如28下的28-00 28-10等
                           #还是以章节id和名称形式返回
    ATAnum='28'
    if request.method == "GET":
        ATAnum = request.GET.get('ATAnum', default='28')
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="%s"'%ATAnum)
        message = cu.fetchall()
        result = []
        i = 0
        for i in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[i]['child_ATA']
            if message[i]['child_ATA_name_zh'] != None:
                tmp['name'] = message[i]['child_ATA_name_zh']
            else:
                tmp['name'] = message[i]['child_ATA_name']
            result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def thirdlevel(request):  #返回章节树 第三级节点 如28-00下的28-00-01 28-00-02等
                           #还是以章节id和名称形式返回
    child_ATAnum='28-00'
    if request.method == "GET":
        child_ATAnum = request.GET.get('child_ATAnum', default='28-00')
        # print(child_ATAnum)
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA="%s"' % child_ATAnum)
        # print('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA=%s'%child_ATAnum)
        message = cu.fetchall()
        result = []
        i = 0
        for i in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[i]['grandson_ATA']
            if message[i]['grandson_ATA_name_zh'] != None:
                tmp['name'] = message[i]['grandson_ATA_name_zh']
            else:
                tmp['name'] = message[i]['grandson_ATA_name']
            # print(tmp)
            result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})