from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("userregister",views.userregister,name="userregister")
]