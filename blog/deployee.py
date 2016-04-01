#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
from django.db import models


# 公司员工表
class deployee(models.Model):
    name = models.CharField(max_length=20)
    creattime = models.DateTimeField()
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    note = models.TextField()
