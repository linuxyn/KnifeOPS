#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    # url(r'^tables/', views.tables, name="tables"),
]