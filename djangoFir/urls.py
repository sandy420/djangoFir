"""djangoFir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import djangoFir.view
import blog.urls

# from django.views.generic.base import

urlpatterns = [
    # 登陆首页
    url('^$', djangoFir.view.index, name=''),
    # 登陆
    url('^main', djangoFir.view.main, name='main'),
    url('^subpage$', djangoFir.view.subpage, name='subpage'),
    # 资产管理
    url('eam$', djangoFir.view.eam, name='eam'),
    # 程序发布
    url('product$', djangoFir.view.product, name='product'),
    # url('subproduct$',include(blog.urls)),
    # 运维团队
    url('operations$', djangoFir.view.operations, name='operations'),
    # 退出登陆
    url('logout$', djangoFir.view.logout, name='logout'),
]
