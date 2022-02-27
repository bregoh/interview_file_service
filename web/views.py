from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def upload(request):
    return render(request, "addfiles.html")
