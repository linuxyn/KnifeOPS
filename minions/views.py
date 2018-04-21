from django.shortcuts import render

# Create your views here.


def hosts(requests):
    return render(requests, "minions/hosts.html")
