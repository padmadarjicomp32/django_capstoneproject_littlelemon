from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register('tables', BookingViewSet, basename='booking')

urlpatterns =[
    # path('',views.sayHello,name="sayHello")
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    
    # path('',views.home,name="home"),
    # path('about/',views.about,name="about"),
    # path('booking/',views.booking,name="booking"),
    # path('menu/',views.menu,name="menu"),
    # path('menu_item/<int:pk>/',views.display_menu_item,name="menu_item"),
]

urlpatterns += router.urls