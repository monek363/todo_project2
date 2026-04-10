from django.shortcuts import render



# Create your views here.

def main(request):
    return render(request, "main.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")