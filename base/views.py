from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

def homePage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def saveEnquiry(request):
    return render(request,"contact.html")

def portfolio(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"portfolio.html",data)

def contact(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"contact.html",data)

def login(request):
    return render(request,"login.html")

