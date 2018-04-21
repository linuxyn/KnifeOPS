#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import url
from django.contrib import admin
from cmdb import views

urlpatterns = [
    url(r'hosts/', views.hosts, name="hosts"),
    url(r'group/', views.group, name="group"),
]