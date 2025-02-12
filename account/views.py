from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout


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

def register(request):
    msg=None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form,'msg':msg})

def auth_login(request):
    form = LoginForm(request.POST or None)
    msg =  None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminPage')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('studentPage')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacherPage')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validation form'
    return render(request,'login.html',{'form':form,'msg':msg})

def logout_view(request):
    print('logout')
    logout(request)
    return render(request,'index.html')

def adminPage(request):
    return render(request,'adminLogin.html')


def teacherPage(request):
    return render(request,'teacherLogin.html')


def studentPage(request):
    return render(request,'studentLogin.html')

def loginPage(request):
    return render(request,'loginPage.html')
