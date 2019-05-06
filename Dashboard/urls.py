from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('',views.login,name="login"),
    path('pilot/',include('Pilot.urls'),name="pilot"),
    #path('logout/',views.logout,name="logout"),
    path('logout/', auth_view.LogoutView.as_view(template_name='dashboard/login.html'),name="logout"),
]
