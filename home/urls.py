from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('Fruit',views.Fruit),  
    path('Vegetables',views.Vegetables),
    path('contact',views.contact),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('profiles',views.profiles),
    path('Product/<str:id>',views.productview),
    path('checkout',views.checkout),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)