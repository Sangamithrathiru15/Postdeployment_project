from django.shortcuts import render
from django.http import request

def pilot(request):
    return render(request,'pilot/pilotchecks.html')
