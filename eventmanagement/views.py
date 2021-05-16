from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userlogin"))
    return render(request,"eventmanagement/user.html")

def userlogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"eventmanagement/userlogin.html",{
                "message":"Invalid Credentials"
            })

    return render(request,"eventmanagement/userlogin.html")

def userlogout(request):
    logout(request)
    return render(request,"eventmanagement/userlogin.html",{
        "message":"Logged out"
    })
