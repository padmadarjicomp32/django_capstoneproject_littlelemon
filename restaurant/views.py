from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sayHello(request):
    return HttpResponse("Welcome To Little Lemon")

def home(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,"index.html",{})

def booking(request):
    return render(request,"index.html",{})

def menu(request):
    return render(request,"index.html",{})

def display_menu_item(request,pk):
    return render(request,"index.html",{})