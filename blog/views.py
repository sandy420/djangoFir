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
