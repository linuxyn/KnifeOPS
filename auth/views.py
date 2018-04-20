from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        username = email.split("@")[0]
        password = request.POST.get("password")
        print(email, password)
        return render(request, "starter.html", {"username": username, "role": "ops_dev"})
    else:
        return
