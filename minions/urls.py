#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import url
from django.contrib import admin
from minions import views

urlpatterns = [
    url(r'^$', views.tables, name="tables"),
]