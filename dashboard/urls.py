#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url
from django.contrib import admin
from dashboard import views

urlpatterns = [
    url(r'^dashboard/$', views.minions, name="minions"),
    # url(r'^tables/', views.tables, name="tables"),
]