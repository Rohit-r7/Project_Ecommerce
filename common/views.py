from django.shortcuts import render

# Create your views here.

def index(request) :
    return render (request,'common/index.html')

def customer_reg(request) :
    return render (request,'common/customer_reg.html')

def seller_reg(request) :
    return render (request,'common/seller_reg.html')

def seller_log(request) :
    return render (request,'common/seller_login.html')

def customer_log(request) :
    return render (request,'common/customer_login.html')



