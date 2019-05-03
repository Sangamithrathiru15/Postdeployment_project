from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]