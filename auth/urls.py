#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url
from django.contrib import admin
from auth import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^tables/', views.tables, name="tables"),
]