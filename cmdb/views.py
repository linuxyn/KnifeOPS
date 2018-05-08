from django.shortcuts import render, HttpResponse, redirect
from cmdb import models
from django.forms import Form
from django.forms import widgets
from django.forms import fields
from django.contrib import messages

# Create your views here.


class MyForm(Form):
    name = fields.CharField(
        required=True,
        error_messages={"required": "Group name cannot be empty"},
        min_length=4,
        max_length=64,
        label="name",
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "group"}))
    describe = fields.CharField(
        required=True,
        error_messages={"required": "Group name cannot be empty"},
        min_length=4,
        max_length=128,
        label="describe",
        widget=widgets.TextInput(attrs={"class": "form-control","placeholder": "describe"})
    )


def hosts(request):
    return render(request, "cmdb/hosts.html")


def group(request):
    if request.method == "GET":
        obj = MyForm()
        group_info = models.Group.objects.all()
        return render(request, "cmdb/group.html", {"group_info": group_info, "obj": obj})
    elif request.method == "POST":
        print("post request is coming...")
        obj = MyForm(request.POST)
        check_data = obj.is_valid()
        if check_data:
            print("pass ok")
            print(obj.cleaned_data)
            models.Group.objects.create(**obj.cleaned_data)
            messages.success(request, "You are success")
        else:
            messages.error(request, "error")
        return redirect("/cmdb/group")
