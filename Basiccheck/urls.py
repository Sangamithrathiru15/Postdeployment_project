from django.urls import path
from . import views

urlpatterns = [
    path('',views.basiccheck,name="basicchecks"),
    path('<int:store_num>/basicresult/',views.basicresult,name="basic-result")
]