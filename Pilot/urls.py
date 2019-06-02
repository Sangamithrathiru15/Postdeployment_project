from django.urls import path
from . import views

urlpatterns = [
    path('',views.pilot,name="pilotcheck"),
    path('<int:store_num>/result/',views.displaydata,name="result"),
]