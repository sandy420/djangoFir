#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
import os.path
import uuid
def upload(request):
    # 自定义存储路径
    rollfileName = r"D:\temp"
    rollfilePath = os.path.join(basePath, rollfileName)
    # req.POST.get(text[1],'')如果获取到信息，则值不是123，如果是空，没有获取到信息结果是123
    if req.POST.get(text[1], '123') == '123':
        # 获取文件二进制流
        reqfile = req.FILES[text[1]]
        # 获取文件名后缀
        filetype = reqfile.name.split(".")[-1]
        # 生成随机字符串加后缀的文件名
        filename = str(uuid.uuid1()) + '.' + filetype
        # 打开文件存储路径
        of = open(rollfilePath + filename, 'wb+')
        # 向指定路径写入文件
        for chunk in reqfile.chunks():
            of.write(chunk)  # 写入内容
        of.close()  # 关闭连接