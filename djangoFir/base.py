#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
import time
def log(err):
    file = r'D:\temp\log\\' + time.strftime('%Y%m%d') + '.log'
    with open(file, 'a') as l:
        l.write(str(err)+'\r')