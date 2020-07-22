from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'main/homepage.html')

def about(request):
    return render(request, 'main/about.html')

def members(request):
    leads = Member.objects.filter(team = "Leads")
    return render(request, 'main/members.html', {'leads' :leads})

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contact.html')
