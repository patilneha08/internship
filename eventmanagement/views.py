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
            password=request.POST.get('password')
            email_qs = Customer.objects.filter(username=username)
            if not email_qs.exists():
                return render(request,"eventmanagement/userlogin.html",{
                    "message":"User does not exist"
                    })      
            else:
                user = authenticate(username=username, password=password)  
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse("userindex"))
                else:
                    return render(request,"eventmanagement/userlogin.html",{
                    "message":"Invalid Credentials"
                    })
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
        return redirect('eventmanagerindex')
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

                return redirect('eventmanagerlogin')
        else:
            form=Eventmanagerform()
    context = {'form':form}
    return render(request, 'eventmanagement/eventmanagerregister.html', context)

#Login page for Event Manager
def eventmanagerlogin(request):
    if request.user.is_authenticated:
        return redirect('eventmanagerindex')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            email_qs = Eventmanager.objects.filter(username=username)
            if not email_qs.exists():
                return render(request,"eventmanagement/eventmanagerlogin.html",{
                    "message":"User does not exist"
                    })      
            else:
                user = authenticate(username=username, password=password)  
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse("eventmanagerindex"))
                else:
                    return render(request,"eventmanagement/eventmanagerlogin.html",{
                    "message":"Invalid Credentials"
                    })
        return render(request,"eventmanagement/eventmanagerlogin.html")             
    
#Logout page for Event Manager
def eventmanagerlogout(request):
    logout(request)
    return render(request,"eventmanagement/eventmanagerlogin.html",{
        "message":"Logged out."
    })



