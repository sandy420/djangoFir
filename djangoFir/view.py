#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"

from django.http import HttpResponse
from blog.models import Book, Login
import datetime
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import blog.models as md
import json
import djangoFir.util as ut


@csrf_exempt
def index(request):
    loginid = Login.objects.get(id='1')
    c = {'username': loginid.username,
         "password": loginid.password}
    return render_to_response("index.html", c)


@csrf_exempt
def main(request):
    # 需登陆后进入
    name = request.POST.get('username')
    if name:
        if Login.objects.get(username=name):
            if Login.objects.get(username=name).password == request.POST.get('password'):
                return render_to_response("web/main.html")
    else:
        return render_to_response("index.html")


@csrf_exempt
def eam(request):
    server = md.Server.objects.all()
    # obj = md.Server.objects.all()
    # t = []
    # for _x in obj:
    #     t.append([_x.id, _x.privateip, _x.internetip, str(_x.buytime), _x.position, _x.usecase, _x.configurinfo, _x.remark])
    # print(t)
    l = []
    for i in server:
        d = {"id": i.id,
             "p_ip": i.privateip,
             "i_ip": i.internetip,
             "b_time": i.buytime,
             "position": i.position,
             "u_case": i.usecase,
             "c_info": i.configurinfo,
             "remark": i.remark
             }
        l.append(d)
    return render_to_response("web/eam.html",
                              {'serverinfo': l[request.POST.get('prepagenum'):request.POST.get('laterpagenum')],
                               'total': md.Server.objects.count(),
                               'pagetotal': (md.Server.objects.count() // 10) + 1})


@csrf_exempt
def subpage(request):
    _pagenum = int(request.POST.get('prepagenum'))
    preNo = (_pagenum - 1) * 10
    obj = md.Server.objects.all()[preNo: _pagenum * 10]
    t = []
    i = -1
    for _x in obj:
        i = i + 1
        if _x.usecase is True:
            _x.usecase = 1
        else:
            _x.usecase = 0
        # t.append([_x.id, _x.privateip, str(_x.internetip), str(_x.buytime), str(_x.position), str(_x.usecase),
        #           _x.configurinfo, _x.remark])
        if i < len(obj) - 1:
            t.append("{0:'" + str(_x.id) + "',1:'" + str(_x.privateip) + "',2:'" + str(_x.internetip) + "',3:'" + str(
                _x.buytime) + "',4:'" + str(_x.position) + "',5:'" + str(_x.usecase) + "',6:'" + str(
                _x.configurinfo) + "',7:'" + _x.remark + "'},")
        else:
            t.append("{0:'" + str(_x.id) + "',1:'" + str(_x.privateip) + "',2:'" + str(_x.internetip) + "',3:'" + str(
                _x.buytime) + "',4:'" + str(_x.position) + "',5:'" + str(_x.usecase) + "',6:'" + str(
                _x.configurinfo) + "',7:'" + _x.remark + "'}")
    # d = [dict(zip(range(len(i)), i)) for i in t]
    # print(d)
    return HttpResponse(t)


@csrf_exempt
def product(request):
    return render_to_response("web/product.html")


@csrf_exempt
def operations(request):
    return render_to_response("web/operations.html")


@csrf_exempt
def logout(request):
    pass
