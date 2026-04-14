from django.shortcuts import render,redirect
from django.http import HttpResponse
from my_app.forms import *
from my_app.models import *
import random


# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact")
    
    else:
        form=ContactForm()
        return render(request,'contact.html',{"form":form})

def request_product(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/request_product")
    else:
        return render(request,"request_product.html")


def about(request):
    return render(request,'about.html')

def mp(request):
    value=random.randint(1,101)
    return render(request,"project.html",{"value":value})