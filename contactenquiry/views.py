from django.shortcuts import render,redirect
from django.core.mail import send_mail
from contactenquiry.models import contactEnquiry
from . import views
from .forms import ContactForm
from django.template.loader import render_to_string
# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print('The form is valid')
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            contact = contactEnquiry(name=name,email=email,phone=phone,message=message)
            contact.save()  
            
            html = render_to_string('emails/contactForm.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            })
            
            send_mail('The contact form subject',message,'xenobaka2@gmail.com',[email],html_message=html)
            
            return redirect('contact')
        else:
            form = ContactForm()

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
        
    return render(request,'contactenquiry/contact.html', {
        'form':form
    })
    
