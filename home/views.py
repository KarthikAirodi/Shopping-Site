from ast import Num
import email
from unicodedata import category
from django.http.response import HttpResponseGone
from django.shortcuts import render, HttpResponse, resolve_url, redirect
from home.models import Contact, Product
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
import random
import math
# Create your views here.


def home(request):
    content = {
        'products': Product.objects.all(),
    }
    return render(request, 'home.html', content)


def about(request):
    return render(request, 'about.html')


def Fruit(request):
    content = {
        'products': Product.objects.filter(Product_category='Fruit'),
    }
    return render(request, 'Fruit.html', content)


def Vegetables(request):
    content = {
        'products': Product.objects.filter(Product_category='Veg'),
    }
    return render(request, 'Vegetables.html', content)
    # return render(request,'Vegetables.html')


def productview(request, id):
    content = {
        'products': Product.objects.filter(Product_id=id),
    }
    return render(request, 'Productview.html', content)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        text=request.POST.get('text')
        contact = Contact(name=name, email=email, Phone=Phone,text=text)
        contact.save()
        messages.success(request, 'Thankyou for your feedback.We will reach out to you if u are facing any issue')
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # fname=request.POST.['fname']
        email = request.POST['email']
        Number=request.POST['Number']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already Used")
                return redirect('/register')
            elif User.objects.filter(id=id).exists():
               messages.info(request,"Number already exists")
               return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username, email=email,id=Number, password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, "password not same")
            return redirect('/register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "credentials invalid")
            return redirect('/login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def profiles(request):
    return render(request, 'profiles.html')


def checkout(request):
    content = {
        'products': Product.objects.all(),
         'n' :Product.objects.count(),
    }
    return render(request, 'checkout.html',content)
