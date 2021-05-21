from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.urls import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import datetime

#Home page for Customer
def userindex(request):
    if 'uname' in request.session:
        events=Event.objects.all()       
        username=request.session['uname']
        user=Customer.objects.get(username=username)
        return render(request, 'eventmanagement/user.html',{
            "events":events, "user":user,
        })
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
            return render(request,'eventmanagement/userlogin.html',{
                "message":"Account successfully Created."
            })
        else:
            return render(request,'eventmanagement/userregister.html',{
                "message":"Passwords do not match."
            })
    return render(request, 'eventmanagement/userregister.html')

#Login page for Customer
def userlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            user=Customer.objects.get(username=username)
            if user.password1==password1:
                request.session['uname']=username
                return redirect("userindex")
            else:
                return render(request,"eventmanagement/userlogin.html",{
                    "message":"Invalid Credentials"
                })
        except Exception as e:
            return render(request,"eventmanagement/userlogin.html",{
                "message":"Invalid Credentials."
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
        username=request.session['aname']
        user=Eventmanager.objects.get(username=username)
        events=Event.objects.filter(eventmanager=username)
        data = {'date':datetime.date.today()} 
        return render(request, 'eventmanagement/eventmanager.html',{
            "user":user, "events":events, "date":data
        })
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
                return redirect('eventmanagerindex')
            else:
                return render(request,"eventmanagement/eventmanagerlogin.html",{
                    "message":"Invalid Credentials"
                })
        except Exception as e:
            return render(request,"eventmanagement/eventmanagerlogin.html",{
                    "message":"Invalid Credentials"
                })
    else:
        return render(request,"eventmanagement/eventmanagerlogin.html")        
    
#Logout page for Event Manager
def eventmanagerlogout(request):
    if 'aname' in request.session:
        del request.session['aname']
    return render(request,'eventmanagement/eventmanagerlogin.html')

#Host an Event by Event Manager
def hostevent(request):
    if request.method=="POST":
        event=Event()   
        event.name=request.POST.get('name')
        temp2=event.name       
        temp=Event.objects.filter(name=temp2)                       
        if(temp):
            return redirect('eventmanagerindex')      
        else:
            event.name=request.POST.get('name')
            event.location2=request.POST.get('location2')
            event.category=request.POST.get('category')
            event.maxpeople=request.POST.get('maxpeople')
            event.date=request.POST.get('date')
            event.time=request.POST.get('time')
            event.location1=request.POST.get('location1')               
            event.city=request.POST.get('city')
            event.state=request.POST.get('state')
            event.pincode=request.POST.get('pincode')
            event.description=request.POST.get('description')
            event.eventmanager=request.session['aname']
            event.cost=request.POST.get('cost')
            event.count=0
            event.save()
            return redirect('eventmanagerindex')
    return render(request, 'eventmanagement/hostevent.html') 

#Lists all the events of the Customer
def userevent(request):
    username=request.session['uname']
    users=Customer.objects.get(username=username)
    events=users.events.all()
    return render(request,"eventmanagement/userevent.html",{
                "events":events
            })

#Book an event by Customer
def bookevent(request,event_id):
    if request.method == 'POST':
        temp=event_id
        event=Event.objects.get(id=temp)
        if event.count==event.maxpeople:
            return render(request,"eventmanagement/temp.html",{
                "event":event, "message":"Sorry, we are all sold out!"
            })
        else:
            return render(request,"eventmanagement/temp.html",{
                "event":event
            })
    return render(request,"eventmanagement/temp.html")

#Confirm the booked event by Customer
def confirmevent(request, event_id):
    if request.method=='POST':
        temp=event_id
        event=Event.objects.get(id=temp)
        number=int(request.POST.get('tickets'))
        if int(event.count)+int(number)>int(event.maxpeople):
            return redirect('userindex')
        else:
            participant=Customer.objects.get(username=request.session['uname'])
            participant.events.add(event)        
            total_cost=int(event.cost)*number
            event.count=int(event.count)+int(number)
            event.save()
            return render(request,"eventmanagement/confirmation.html",{
                "event":event, "total_cost":total_cost
            })
    return render(request,"eventmanagement/temp.html")

#delete event by Event Manager
def deleteevent(request, event_id):
    temp=event_id
    event=Event.objects.get(id=temp)
    event.delete()
    return redirect('eventmanagerindex')