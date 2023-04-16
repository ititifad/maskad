from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def it_services(request):
    return render(request, 'it.html')