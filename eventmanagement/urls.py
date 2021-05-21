from django.urls import path
from . import views

urlpatterns=[
    path('userindex',views.userindex,name="userindex"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("userregister",views.userregister,name="userregister"),
    path("userlogout",views.userlogout,name="userlogout"),
    path('eventmanagerindex',views.eventmanagerindex,name="eventmanagerindex"),
    path("eventmanagerlogin",views.eventmanagerlogin,name="eventmanagerlogin"),
    path("eventmanagerregister",views.eventmanagerregister,name="eventmanagerregister"),
    path("eventmanagerlogout",views.eventmanagerlogout,name="eventmanagerlogout"),
    path("hostevent",views.hostevent,name="hostevent"),
    path("<int:event_id>/bookevent",views.bookevent,name="bookevent"),
    path("<int:event_id>/confirmevent",views.confirmevent,name="confirmevent"),
    path("<int:event_id>/deleteevent",views.deleteevent,name="deleteevent"),
    path("userevent",views.userevent,name="userevent"),
]