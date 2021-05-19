from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import HostEvent
from .models import *

#Home page for Customer
def userindex(request):
    if 'uname' in request.session:
        return render(request, 'eventmanagement/user.html')
    else:
        return render(request,'eventmanagement/userlogin.html',{
            "message":"You need to Login first."
        })

#Registration page for Customer 
def userregister(request):
    if request.method == 'POST':
        user=Customer()
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.phone=request.POST.get('phone')
        user.username=request.POST.get('username')
        user.password1=request.POST.get('password1')
        user.password2=request.POST.get('password2')
        if(user.password1==user.password2):
            user.save()
            request.session['uname'] = user.first_name
            return redirect('userlogin')
        else:
            return render(request,'eventmanagement/userregister',{
                "message":"Passwords do not match."
            })
    return render(request, 'eventmanagement/userregister.html',{
        "message":"Something went wrong!"
    })

#Login page for Customer
def userlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            user=Customer.objects.get(username=username)
            if user.password1==password1:
                request.session['uname']=username
                return render(request,"eventmanagement/user.html",{
                    "user":user  
                })
            else:
                return render(request,"eventmanagement/userlogin.html",{
                    "message":"Invalid Credentials"
                })
        except Exception as e:
            return render(request,"eventmanagement/userregister.html",{
                    "message":"User Does not exist! Register now."
                })
    else:
        return render(request,"eventmanagement/userlogin.html")

#Logout Page for Customer
def userlogout(request):
    if 'uname' in request.session:
        del request.session['uname']
    return render(request,'eventmanagement/userlogin.html')

#Home Page for Event Manager
def eventmanagerindex(request):
    if 'aname' in request.session:
        return render(request, 'eventmanagement/eventmanager.html')
    else:
        return render(request,'eventmanagement/eventmanagerlogin.html',{
            "message":"You need to Login first."
        })

#Registration page for Event Manager
def eventmanagerregister(request):
    if request.method == 'POST':
        user=Eventmanager()
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.phone=request.POST.get('phone')
        user.username=request.POST.get('username')
        user.password1=request.POST.get('password1')
        user.password2=request.POST.get('password2')
        if(user.password1==user.password2):
            user.save()
            request.session['aname'] = user.first_name
            return render(request,'eventmanagement/eventmanagerlogin.html',{
                "message":"Account Created Successfully."
            })
        else:
            return render(request,'eventmanagement/eventmanagerregister.html',{
                "message":"Passwords do not match."
            })
    return render(request, 'eventmanagement/eventmanagerregister.html',{
        "message":"Something went wrong!"
    })

#Login page for Event Manager
def eventmanagerlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            user=Eventmanager.objects.get(username=username)
            if user.password1==password1:
                request.session['aname']=username
                return render(request,"eventmanagement/eventmanager.html",{
                    "user":user  
                })
            else:
                return render(request,"eventmanagement/eventmanagerlogin.html",{
                    "message":"Invalid Credentials"
                })
        except Exception as e:
            return render(request,"eventmanagement/eventmanagerregister.html",{
                    "message":"User Does not exist! Register now."
                })
    else:
        return render(request,"eventmanagement/eventmanagerlogin.html")        
    
#Logout page for Event Manager
def eventmanagerlogout(request):
    if 'aname' in request.session:
        del request.session['aname']
    return render(request,'eventmanagement/eventmanagerlogin.html')

#Host an Event
def hostevent(request):
    if request.method=="POST":
        form=HostEvent(request.POST)
        if form.is_valid():
            event=Event()
            event.name=form.cleaned_data['name']
            event.category=form.cleaned_data['category']
            event.maxpeople=form.cleaned_data['maxpeople']
            event.date=form.cleaned_data['date']
            event.duration=form.cleaned_data['duration']
            event.location1=form.cleaned_data['location1']
            event.location2=form.cleaned_data['location2']
            event.city=form.cleaned_data['city']
            event.state=form.cleaned_data['state']
            event.pincode=form.cleaned_data['pincode']
            event.description=form.cleaned_data['description']
            event.save()
            event = form.cleaned_data.get('name')
            messages.success(request, 'Event ' + event + 'has been created.')

            return render(request,'eventmanagement/eventmanager.html',{
                "message":"Event was successfully registered"
            })
    else:
        form=HostEvent()
    context = {'form':form}
    return render(request, 'eventmanagement/hostevent.html', context) 
