from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail

def send_email(request):

    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    ctx = {
        'message_name': name,
        'email': email,
        'subject': subject,
        'message': message,
        'phone':phone
    }
    message = render_to_string('email.html',ctx)

    if request.method == 'POST' and email and message:
        send_mail(email, 
        message,
        phone, 
        ["dex90jay@gmail.com"],  
        fail_silently=False, 
        html_message=message)
        messages.success(request, f"Thank you, We have received your Email, we'll get back to you very shortly")

    return ctx
