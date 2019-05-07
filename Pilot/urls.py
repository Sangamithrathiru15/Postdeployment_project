from django.urls import path
from . import views

urlpatterns = [
    path('',views.pilot,name="pilotcheck"),
    path('result/',views.extractdata,name="result"),
]