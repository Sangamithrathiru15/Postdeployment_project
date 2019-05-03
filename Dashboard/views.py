from django.shortcuts import render
from django.http import request

# Create your views here.
def login(request):
    return render(request,'dashboard/login.html')

def logout(request):
    return render(request,'dashboard/logout.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')