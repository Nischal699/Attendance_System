from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail,EmailMultiAlternatives
from contactenquiry.models import contactEnquiry



def homePage(request):
        subject='Thanking You'
        from_email='xenobaka2@gmail.com'
        msg='<h1>Welcome to <b>My website</b></h1><p>Thank you for using my website<p>'
        to='nischal123321@gmail.com'
        msg=EmailMultiAlternatives(subject,msg,from_email,[to])
        msg.content_subtype='html'
        msg.send()
        
        send_mail(
        'Testing Mail',
        'Here is the message',
        'xenobaka2@gmail.com',
        ['nischal123321@gmail.com'],
        fail_silently=False,
    )

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

def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        en.save()
        n='Data Inserted'
        
    #subject='Testing Mail'
    #from_email='xenobaka2@gmail.com'
    #msg='<p>Welcome to <b>My website</b></p>'
    #to='nischal123321@gmail.com'
    #msg=EmailMultiAlternatives(subject,msg,from_email,[to])
    #msg.content_subtype='html'
    #msg.send()
    
    #send_mail(
    #    'Testing Mail',
    #   'Here is the message',
    #   'xenobaka2@gmail.com',
    #    ['nischal123321@gmail.com'],
    #    fail_silently=False,
    #)
        
    return render(request,"contact.html")
