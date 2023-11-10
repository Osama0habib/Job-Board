from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.

def send_message(request):
    info = Info.objects.first()

    if request.method == 'POST' :
        subject = request.POST['subject']
        email = request.POST['email']
        content = request.POST['message'] 
        send_mail(
            subject,
            content,
            email,
            [settings.EMAIL_HOST_USER],
        )
    return render(request,'contact/contact.html',{'info' : info})
