#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
from blog.views import *
from django.conf.urls import url, include

# from django.views.generic.base import

urlpatterns = [
    url('main#pretangportal$', pretangportal, name='pretangportal'),
    url('klfportal$', klfportal, name='klfportal'),
    url('klfwap$', klfwap, name='klfwap'),
    url('klfbackend$', klfbackend, name='klfbackend'),
    url('subkgj$', subkgj, name='subkgj'),
    url('subwgj$', subwgj, name='subwgj'),
    url('broker$', broker, name='broker'),
]
