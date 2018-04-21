from django.shortcuts import render

# Create your views here.


def hosts(requests):
    return render(requests, "cmdb/hosts.html")
