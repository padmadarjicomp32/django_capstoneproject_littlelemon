from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet



# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


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