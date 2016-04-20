#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
import os
import shutil
import time

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from djangoFir.base import log

import blog.models as md


# Create your views here.
@csrf_exempt
def pretangportal(request):
    return render_to_response("web/subproduct/subpretangportal.html")


def klfportal(request):
    return render_to_response("web/subproduct/subklfport.html")


def klfwap(request):
    return render_to_response("web/subproduct/klfwap.html")


def klfbackend(request):
    return render_to_response("web/subproduct/subbacked.html")


def subkgj(request):
    return render_to_response("web/subproduct/subkgj.html")


def subwgj(request):
    return render_to_response("web/subproduct/subwgj.html")


def broker(request):
    return render_to_response("web/subproduct/subbroker.html")


# def handle_uploaded_file(f):
#     with open('./name.txt','wb+') as ft:
#         for chunk in f.chunks():
#             ft.write(chunk)




@csrf_exempt
def handle_uploaded_file(f):
    file_name = ""
    try:
        path = "upload" + time.strftime('/%Y%m%d/%H/%M/%S/')
        if not os.path.exists(path):
            os.makedirs(path)
            file_name = path + f.name
            with open(file_name, 'wb+') as ft:
                for chunk in f.chunks():
                    ft.write(chunk)
            up = md.UploadFile(filename=f.name, filepath=path, uploadtime=time.strftime('%Y-%m-%d %H:%M:%S'))
            up.save()
    except Exception as err:
        log(err)
    return file_name, path


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = md.UploadFile(request.POST, request.FILES)
        if form:
            file_path = handle_uploaded_file(request.FILES['file'])
            filename = {
                'file_path': file_path[1],
                'file_name': file_path[0],
                'back_path': ''
            }
            return render_to_response('upload.html', filename)
        else:
            form = md.UploadFile()
    return render_to_response('upload.html', filename)


def copyFiles(sourceDir):
    targetDir = r'D:\temp\2016upload'
    if sourceDir.find(".svn") > 0:
        return
    for file in os.listdir(sourceDir):
        sourcefile = os.path.join(sourceDir, file)
        targetfile = os.path.join(targetDir, file)
        if os.path.isfile(sourcefile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetfile) or (os.path.exists(targetfile)) and (
                    os.path.getsize(targetfile)) != os.path.getsize(sourcefile):
                open(targetfile, 'wb').write(open(sourcefile, 'rb').read())
        if os.path.isdir(sourcefile):
            first_directory = False
            copyfiles(sourcefile, targetfile)
    return HttpResponse(targetfile)


def CleanDir(Dir):
    if os.path.isdir(Dir):
        paths = os.listdir(Dir)
        for path in paths:
            filePath = os.path.join(Dir, path)
            if os.path.isfile(filePath):
                try:
                    log(err="清除发布目录的内容:%s" % filePath)
                    os.remove(filePath)
                except os.error:
                    autoRun.exception("remove %s error." % filePath)  # 引入logging
            elif os.path.isdir(filePath):
                if filePath[-4:].lower() == ".svn".lower():
                    continue
                log(err="清除发布目录的内容:%s" % filePath)
                shutil.rmtree(filePath, True)
    return True


@csrf_exempt
def deployFile(request):
    if request.method == 'POST':
        try:
            p_ip = md.Server.objects.get(privateip=request.POST.get('p_deploy'))
        except:
            return HttpResponse("请重新选择服务器,进行灰度发布.")
        if p_ip.internetip:
            targetDir = r"D:\temp\test\upload"  # + '\\' + str(time.strftime('%Y%m%d'))
            sourceDir = request.POST.get('full_file_path')
            backDir = r'D:\temp\test\back\\' + str(time.strftime('%Y%m%d')) + r'\pretangportal' + str(
                time.strftime('\%H%M%S'))
            print(backDir)
            log(err="备份原目录程序%s：" % backDir)
            # 备份原程序
            if not os.path.exists(backDir):
                shutil.copytree(targetDir, backDir)
                log(err="清除发布目录的内容:%s" % targetDir)
                CleanDir(targetDir)
                shutil.copy(request.POST.get('full_name'), targetDir)
            else:
                shutil.rmtree(backDir)
                shutil.copytree(targetDir, backDir)
                CleanDir(targetDir)
                shutil.copy(request.POST.get('full_name'), targetDir)
                os.system('')
                os.system('java -version')
        return HttpResponse(targetDir + ',并发布成功。')
