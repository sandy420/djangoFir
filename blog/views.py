#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


# Create your views here.
@csrf_exempt
def pretangportal(request):
    return render_to_response("web/subproduct/subpretangportal.html")


def klfportal(request):
    pass


def klfwap(request):
    pass


def klfwap(request):
    pass


def klfbackend(request):
    pass


def subkgj(request):
    pass


def subwgj(request):
    pass


def broker(request):
    pass
