from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

def index(request):
    return render(request, 'eventmanagement/user.html')

def userregister(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('userlogin')
            

        context = {'form':form}
        return render(request, 'eventmanagement/userregister.html', context)

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'eventmanagement/userlogin.html', context)

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def eventmanagerlogout(request):
    logout(request)
    return render(request,"eventmanagement/eventmanagerlogin.html",{
        "message":"Logged out."
    })


def eventmanagerlogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"eventmanagement/eventmanagerlogin.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"eventmanagement/eventmanagerlogin.html")
    
def eventmanagerregister(request):
    if request.method=="POST":
        First_name=request.POST['First_name']
        Last_name=request.POST['Last_name']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        temp=Eventmanager(First_name=First_name, Last_name=Last_name, phone=phone, username=username, password=password)
        temp.save()
    return render(request,"eventmanagement/eventmanagerlogin.html")