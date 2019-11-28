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
    'passwd': 'wangjin',
    'db':'lru2' #这里需要改成你的数据库名
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
        con.ping(reconnect=True)
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
    con.ping(reconnect=True)
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
    con.ping(reconnect=True)
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select DISTINCT ATA,ATA_name,ATA_name_zh from tree')
    message = cu.fetchall()
    cu.close()
    result = []
    i=0
    for i in range(0, len(message)):
        tmp = {}
        tmp['id'] = message[i]['ATA']
        tmp['pId']='0'
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
        con.ping(reconnect=True)
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="%s"'%ATAnum)
        message = cu.fetchall()
        cu.close()
        result = []
        i = 0
        for i in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[i]['child_ATA']
            tmp['pId']=ATAnum
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
        con.ping(reconnect=True)
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA="%s"' % child_ATAnum)
        # print('select DISTINCT grandson_ATA,grandson_ATA_name,grandson_ATA_name_zh from tree where child_ATA=%s'%child_ATAnum)
        message = cu.fetchall()
        cu.close()
        result = []
        i = 0
        for i in range(0, len(message)):
            tmp = {}
            tmp['id'] = message[i]['grandson_ATA']
            tmp['pId']=child_ATAnum
            if message[i]['grandson_ATA_name_zh'] != None:
                tmp['name'] = message[i]['grandson_ATA_name_zh']
            else:
                tmp['name'] = message[i]['grandson_ATA_name']
            # print(tmp)
            result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def alllevel(request):  #返回整棵树内容
    con.ping(reconnect=True)
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="28"')
    message = cu.fetchall()
    cu.close()
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
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
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



def alllevel(request):  #返回整棵树内容
    con.ping(reconnect=True)
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select DISTINCT child_ATA,child_ATA_name,child_ATA_name_zh from tree where ATA="28"')
    message = cu.fetchall()
    cu.close()
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
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
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


def searchInfoforTree(request):  #返回整棵树内容
    con.ping(reconnect=True)
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('SELECT DISTINCT Mername from manufacturer')
    #cu.execute('create or REPLACE view combine(mername,pmodel,pnr) as select manufacturer.Mername as a,pmodel.PModelname as b,apply.prn as c from  pmodel INNER join manufacturer on pmodel.Mername = manufacturer.Mername inner join apply on pmodel.PModelname = apply.PModelname')
    #con.commit()
   # cu.execute('SELECT DISTINCT mername,pmodel,ata from combine inner join component on combine.pnr=component.PNR')
    message = cu.fetchall()
    cu.close()
    result = []
    second=[]
    thrid=[]
    i = 0
    tmp = {}
    for i in range(0, len(message)):
        tmp['id'] = i
        tmp['pId']='-1'
        tmp['name'] = message[i]['Mername']
        second.append(message[i]['Mername'])
        result.append(tmp.copy())
    for i in range(0, len(second)):
        cu = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute('SELECT DISTINCT PModelname from pmodel where Mername="%s"' % second[i])
        second_name = cu.fetchall()
        for j in range(0, len(second_name)):
            tmp['id'] = str(i)+"-"+str(j)
            tmp['pId']= i
            tmp['name'] = second_name[j]['PModelname']
            result.append(tmp.copy())
            cu.execute('SELECT DISTINCT ATA from apply INNER JOIN component on apply.prn=component.PNR where apply.PModelname="%s"' % second_name[j]['PModelname'])
            thrid_name = cu.fetchall()
            for k in range(0, len(thrid_name)):
                tmp['id'] = str(i) + "-" + str(j)+"-"+str(k)
                tmp['pId'] = str(i)+"-"+str(j)
                tmp['name'] = thrid_name[k]['ATA']
                result.append(tmp.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})


def searchInfo(request):
    return render(request, 'searchInfo.html')