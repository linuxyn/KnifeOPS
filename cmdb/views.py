from django.shortcuts import render
from cmdb import models
from django.forms import Form
from django.forms import widgets
from django.forms import fields

# Create your views here.


class MyForm(Form):
    group = fields.CharField(
        required=True,
        error_messages={"required": "Group name cannot be empty"},
        max_length=64,
        label="group"
    )
    describe = fields.CharField(
        required=True,
        error_messages={"required": "Group name cannot be empty"},
        max_length=128,
        label="describe"
    )


def hosts(requests):
    return render(requests, "cmdb/hosts.html")


def group(requests):
    obj = MyForm()
    group_info = models.Group.objects.all()
    return render(requests, "cmdb/group.html", {"group_info": group_info, "group_obj": obj})
