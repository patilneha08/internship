from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Customerform, Eventmanagerform
from .models import *

#Home page for Customer
def userindex(request):
    return render(request, 'eventmanagement/user.html')

#Registration page for Customer 
def userregister(request):
    if request.user.is_authenticated:
        return redirect('userindex')
    else:
        if request.method == 'POST':
            form=Customerform(request.POST)
            if form.is_valid():
                user=Customer()
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.phone=form.cleaned_data['phone']
                user.username=form.cleaned_data['username']
                user.password=form.cleaned_data['password']
                user.password1=form.cleaned_data['password1']
                user.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('userlogin')
        else:
            form=Customerform()
    context = {'form':form}
    return render(request, 'eventmanagement/userregister.html', context)

#Login page for Customer
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('userindex')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password1=request.POST.get('password1')
            try:
                user=Customer.objects.get(username=username)
                if user.password1==password1:
                    return render(request,"eventmanagement/user.html",{
                        "user":user  
                    })
                else:
                    return render(request,"eventmanagement/userlogin.html",{
                        "message":"Invalid Credentials"
                    })
            except Exception as e:
                return render(request,"eventmanagement/userlogin.html",{
                        "message":"User Does not exist!"
                    })
        else:
            return render(request,"eventmanagement/userlogin.html")

#Logout Page for Customer
def userlogout(request):
    logout(request)
    return redirect('userlogin')

#Home Page for Event Manager
def eventmanagerindex(request):
    return render(request, 'eventmanagement/eventmanager.html')

#Registration page for Event Manager
def eventmanagerregister(request):
    if request.user.is_authenticated:
        return redirect('userindex')
    else:
        if request.method == 'POST':
            form=Eventmanagerform(request.POST)
            if form.is_valid():
                user=Eventmanager()
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.phone=form.cleaned_data['phone']
                user.username=form.cleaned_data['username']
                user.password=form.cleaned_data['password']
                user.password1=form.cleaned_data['password1']
                user.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('userlogin')
        else:
            form=Eventmanagerform()
    context = {'form':form}
    return render(request, 'eventmanagement/userregister.html', context)

#Login page for Event Manager
def eventmanagerlogin(request):
    if request.user.is_authenticated:
        return redirect('userindex')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password1=request.POST.get('password1')
            try:
                user=Eventmanager.objects.get(username=username)
                if user.password1==password1:
                    return render(request,"eventmanagement/eventmanager.html",{
                        "user":user
                    })
                else:
                    return render(request,"eventmanagement/eventmanagerlogin.html",{
                        "message":"Invalid Credentials"
                    })
            except Exception as e:
                return render(request,"eventmanagement/eventmanagerlogin.html",{
                        "message":"User Does not exist!"
                    })
        else:
            return render(request,"eventmanagement/eventmanagerlogin.html",{
                "message":"Something went wrong!"
            })            
    
#Logout page for Event Manager
def eventmanagerlogout(request):
    logout(request)
    return render(request,"eventmanagement/eventmanagerlogin.html",{
        "message":"Logged out."
    })



