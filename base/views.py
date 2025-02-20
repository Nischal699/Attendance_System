from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives

def homePage(request):
        #subject='Thanking You'
        #from_email='xenobaka2@gmail.com'
        #msg='<h1>Welcome to <b>My website</b></h1><p>Thank you for using my website<p>'
        #to='nischal123321@gmail.com'
        #msg=EmailMultiAlternatives(subject,msg,from_email,[to])
        #msg.content_subtype='html'
        #msg.send()
        
        #send_mail(
        #'Testing Mail',
        #'Here is the message',
        #'xenobaka2@gmail.com',
        #['nischal123321@gmail.com'],
        #fail_silently=False,
    #)

        return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")


def portfolio(request):
    data={
        'title':'Contact',
        'name':'Nischal'
    }
    return render(request,"portfolio.html",data)


