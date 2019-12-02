"""LRUSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from LRUSystem import views
from src.viewscode import viewsSearchInfo, viewsLogin, viewsMain, viewsAnalysis, viewsStructureTree, viewsBasicTableShow

urlpatterns = [
    #登陆界面
    path('login/', viewsLogin.login),
    #主界面
    path('main/', viewsMain.main),
    #分析界面
    path('chart/', viewsAnalysis.chart),
    #Pnr具体信息查找页面
    path('tableSearch/', viewsSearchInfo.searchInfo), #数据查找界面
    path('getPnrs/', viewsSearchInfo.getPnrs), #获取Pnrs信息
    path('getManuPmodelATAs/', viewsSearchInfo.getManuPmodelATA), #获取ATA\制造商\机型信息
    path('getAdvancePnrs/', viewsSearchInfo.getAdvancePnrs), #高级信息获取pnrs
    path('getAllPnrs/', viewsSearchInfo.getAllPnrs), #高级信息获取pnrs
    path('getPropertysaAndClass/', viewsSearchInfo.getPropertysaAndClass), #高级信息获取pnrs
    path('getClassPropertys/', viewsSearchInfo.getClassProperty), #高级信息获取pnrs


    #结构树状图展示界面
    path('structureTree/', viewsStructureTree.structureTree),
    path('alllevel',viewsStructureTree.alllevel),

    #数据库表基本展示界面
    path('tableShow/', viewsBasicTableShow.tableshow),

    #树接口
    path('getTree/', viewsStructureTree.getTree),




    #暂时无用
    #
    #path('firstlevel/', views.firstlevel),
    #path('secondlevel', views.secondlevel),
    #path('thirdlevel',views.thirdlevel),
    #path('searchInfo/',views.searchInfo),
    #path('searchInfoforTree/',views.searchInfoforTree),
]
