from django.shortcuts import render

# Create your views here.

def index(request) :
    return render (request,'customer/index.html')

def product_details(request) :
    return render (request,'customer/product_details.html')

def change_password(request) :
    return render (request,'customer/change_password.html')





