from django.shortcuts import render
from django.http import request

def basiccheck(request):
    return render(request,'basiccheck/basicchecks.html')
