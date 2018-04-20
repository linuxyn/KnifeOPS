from django.shortcuts import render

# Create your views here.


def tables(requests):
    return render(requests, "minions/tables.html")
